"""
SMTP: Simple Mail Transfer Protocol.
用做測試環境，ＳＭＴＰ可以只示捕捉任何所傳送的訊息而不發出去。

DebuggingServer，就是攔截資訊，並show在Terminal上。
"""

import smtplib
from email.mime.text import MIMEText

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

if __name__ == '__main__':
    # Open a new Terminal for running under CMD for SMTP server.
    #python -m smtpd -n -c DebuggingServer localhost:1025

    # THis script must run in differect terminal.
    send_email("A model subject", "The message contents", "from@example.com", "to1@example.com", "to3@example.com")
