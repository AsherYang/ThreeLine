# -*- coding:utf-8 -*-

import smtplib
import time
from email.utils import formatdate

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

"""
发送邮件
"""


class SendEmail():
    """
    send email content: content
    author: AsherYang
    create: 2016.11.29
    attention: sender only support qq email at now.
               if you need others, should replace some hard-code
    youdontgetme@qq.com youdontgetme123 setting POP3
    13532768544@139.com yougetme123
    """

    def __init__(self, fromaddr='15014769149@139.com', password='yougetme123', toaddrs=['13553831061@139.com'],
                 subject='微信消息'):
        self.fromaddr = fromaddr
        self.password = password
        self.toaddrs = toaddrs
        self.subject = subject

    def __call__(self, content):
        self.send(content)

    # MSG需要符合smtp协议格式, 这是拼接的方式，下面使用email库中方式更优雅
    # add the From: To: and Subject: headers at the start!
    # msg = ("From: %s\r\nTo: %s \r\nSubject: %s\r\n\r\n"
    # %(fromaddr, toaddrs, subject))

    # email 库方式，设置协议
    def mail_msg(self, toaddr, message, format='plain'):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = toaddr
        msg['Subject'] = self.subject
        msg['Date'] = formatdate(localtime=True)
        msg.attach(MIMEText(message, format, 'utf-8'))
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        return msg.as_string()

    def send(self, message):
        try:
            # ssl: smtp.qq.com smtp.139.com
            # sever = smtplib.SMTP_SSL('smtp.139.com', timeout = 30)
            # 创建一个smtp对象,在windows 下使用smtp_ssl 正常，
            # 但是在linux 下ssl配置有问题，没搞通，就换成SMTP() + connect() 形式。保证两个系统都行
            sever = smtplib.SMTP()
            sever.connect('smtp.139.com')

            sever.set_debuglevel(1)
            print '---- need Authentication ----'

            # login
            # username = prompt("Username: ")
            # password = getpass("Password: ")
            sever.login(self.fromaddr, self.password)
            # send mail
            for toaddr in self.toaddrs:
                sever.sendmail(self.fromaddr, toaddr, self.mail_msg(toaddr, message))
                time.sleep(5)
            sever.quit()
            print 'send mail success.'
        except Exception as e:
            print 'send mail fail.', e


if __name__ == '__main__':
    test_msg = 'how are you.'
    sendE = SendEmail()
    sendE(content=test_msg)
