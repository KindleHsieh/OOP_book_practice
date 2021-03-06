"""
SMTP: Simple Mail Transfer Protocol.
用做測試環境，ＳＭＴＰ可以只示捕捉任何所傳送的訊息而不發出去。

DebuggingServer，就是攔截資訊，並show在Terminal上。
"""

import smtplib
from email.mime.text import MIMEText
from collections import defaultdict


def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    # Setting header info.
    headers = {} if headers is None else headers

    # Setting mail Item.
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value
    
    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

class MailingList:
    """Manage the group of mail."""
    def __init__(self):
        self.email_map = defaultdict(set)
    
    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email( subject, message, from_addr, *emails, headers=headers)


class MailingList_W_Data(MailingList):
    def __init__(self, data_file):
        super().__init__()
        self.data_file = data_file

    def save(self):
        with open(self.data_file, 'w') as file:
            for e, g in self.email_map.items():
                file.write(f'{e} {",".join(g)} \n')

    def load(self):
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file, 'r') as file:
                for row in file:
                    email, groups = row.strip().split(" ")
                    self.email_map[email] = set(groups.split(","))
        except IOError:
            pass

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()


if __name__ == '__main__':
    # Open a new Terminal for running under CMD for SMTP server.
    #python -m smtpd -n -c DebuggingServer localhost:1025

    # THis script must run in differect terminal.
    # Step 1.
    # send_email("A model subject", "The message contents", "from@example.com", "to1@example.com", "to3@example.com")

    # Step 2.
    # m = MailingList()
    # m.add_to_group('f1@example.com', 'friends')
    # m.add_to_group('f2@example.com', 'friends')
    # m.add_to_group('family@example.com', 'family')
    # m.add_to_group('pro1@example.com', 'professional')

    # m.send_mailing("A Party", "Friends and Family only: a party",
    #                 "me@example.com", "friends", "family", headers={"Reply-TO": "me2@example.com"})

    # Step 3.
    # from pathlib import Path
    
    # m = MailingList_W_Data(str(Path(__file__).parent / 'addresses.db'))
    # m.add_to_group('f1@example.com', 'friends')
    # m.add_to_group('family1@example.com', 'friends')
    # m.add_to_group('family1@example.com', 'family')
    # m.save()

    # Step 4.
    from pathlib import Path
    with MailingList_W_Data(str(Path(__file__).parent / 'addresses.db')) as ml:
        ml.add_to_group('friend2@example.com', 'friends')
        ml.send_mailing("what's up", "hey friends, how's it going", "me@example.com", 'friends')
