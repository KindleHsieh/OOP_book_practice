"""
SMTP: Simple Mail Transfer Protocol.
用做測試環境，ＳＭＴＰ可以只示捕捉任何所傳送的訊息而不發出去。

DebuggingServer，就是攔截資訊，並show在Terminal上。
"""

import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, **headers):
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
    exec("python -m smtpd -n -c DebuggingServer localhost:1025")