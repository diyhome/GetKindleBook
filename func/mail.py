#!/usr/bin/env python3
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
from configparser import ConfigParser

class SMail:
    def __init__(self,config):
        cfmail = ConfigParser()
        cfmail.read(config)
        self.smtp_server = cfmail.get('mail','smtp_server')
        self.smtp_port = cfmail.get('mail','smtp_port')
        self.sender = cfmail.get('mail','sender')
        self.sender_passwd = cfmail.get('mail','sender_passwd')
        self.receivers = cfmail.get('mail','receivers').split(',')

    def built_attach(self,filepath):
        dirname,filename = os.path.split(filepath)
        attach = MIMEApplication(open(filepath, "rb").read())
        attach.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))
        return attach

    def send(self,filepath=None,debug=None):
        msg = MIMEMultipart()
        subject = 'EBook'
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ';'.join(self.receivers)
        msg.attach(MIMEText('Dont receive.', 'plain', 'utf-8'))

        if filepath is not None:
            msg.attach(cls.built_attach(filepath))
        try:
            s = SMTP_SSL(self.smtp_server, self.smtp_port)
            if debug:
                s.set_debuglevel(1)
            s.login(self.sender, self.sender_passwd)
            print('正在向 {} 发送 {}'.format(','.join(self.receivers), subject))
            s.sendmail(self.sender, self.receivers, msg.as_string())
            s.quit()
        except smtplib.SMTPException as e:
            print('发送 {} 邮件时出现错误！error:{}'.format(subject, e))
            raise

if __name__ == "__main__":
    m = SMail('func/config.ini')
    m.send()
