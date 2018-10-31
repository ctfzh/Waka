# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import readConfig


class Email:
    def __init__(self):
        config = readConfig.ReadConfig()
        global mail_host, mail_port, mail_user, mail_pass, sender, title, content
        mail_host = config.get_email("mail_host")  # 服务器主机
        mail_port = config.get_email("mail_port")  # 服务器端口号
        mail_user = config.get_email("mail_user")  # 登录用户名
        mail_pass = config.get_email("mail_pass")  # 登录授权码
        sender = config.get_email("sender")  # 邮件的发送者
        title = config.get_email("subject")  # 邮件的标题
        content = config.get_email("content")  # 邮件的文字内容
        self.value = config.get_email("receiver")  # 邮件的接收者
        self.proDir = config.get_data("proDir")
        self.picname = config.get_data("picname")
        self.receiver = []
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for n in str(self.value).split("/"):
            self.receiver.append(n)
        self.subject = title + " " + date
        self.msg = MIMEMultipart('mixed')  # 邮件中含有附件

    def mail_header(self):
        self.msg['Subject'] = self.subject  # 邮件的主题
        self.msg['From'] = sender  # 邮件的发件人
        self.msg['To'] = ";".join(self.receiver)  # 邮件的收件人
        # self.msg['Date']='2012-3-16' # 邮件的发送时间

    def mail_content(self):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def mail_picture(self):
        resultPath = os.path.join(self.proDir, "4.jpg")
        sendimagefile = open(resultPath, 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename="testimage.png"'
        self.msg.attach(image)

    def send_email(self):
        self.mail_header()  # 构造邮件的标题
        self.mail_content()  # 构造邮件的文本
        self.mail_picture()  # 构造邮件的图片
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, int(mail_port))
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, self.receiver, self.msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
