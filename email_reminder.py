# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time
from datetime import datetime

sender = 'reminder@auto.com'
receiver = 'taitocdt@gmail.com'

mail_host="outlook.office365.com"
mail_user="xxx"
mail_pass="xxx"
mail_port = 443


def send_email(msg):
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = formataddr(["Reminder", sender])
    message['To'] = formataddr(["Me", receiver])
    message['Subject'] = '成功提交报名表'

    try:
        server = smtplib.SMTP_SSL(mail_host, mail_port)
        server.login(mail_user, mail_pass)
        server.sendmail(sender, [receiver, ], message.as_string())
        print('Email is sent!')
        server.quit()
    except smtplib.SMTPException:
        print('Send failed...')


if __name__ == '__main__':
    submitted_time = time.time()
    readable_time = datetime.fromtimestamp(submitted_time).strftime('%Y-%m-%d %H:%M:%S:%m')
    reminder = f"Registration form is submitted at {readable_time}"

    send_email(reminder)
