#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText

#程序运行依赖于python，官网下载python3，安装
# win+R 打开命令窗口，输入cmd 确定
# 输入 cd + '你这个文件存放在哪个目录下' 回车 ,进入后输入 python 'hello_mail.py' 回车 成功

# 总共有两种数据模型，type = {key:'to'} or type = {key:'option'}
# 一个是to,title,content模式，这个模式下你可以一対多，意思是一封邮件你可以发给n多个人，这个模式下,三个属性必填

#type = {'key':'to'}
#to = ['ysyniko960326@163.com','827717887@qq.com']
#title = '標題'
#content = '郵件內容'
# 另一个是option对象模式,这个模式下，暂不支持to传多个值
type = {'key':'option'}
option = [
            {'to': 'ysyniko960326@163.com', 'title': '標題', 'content': '郵件內容'}, 
            {'to': '827717887@qq.com', 'title': '標題', 'content': '郵件內容'},
            {'to': 'ysyniko960326@163.com', 'title': '標題', 'content': '郵件內容'}
        ]


username = "" #你的邮箱
password = "" #你的授权码 授权码获取 163邮箱 -> 设置 -> POP3/SMTP/IMAP 根据提示开启就好 qq的申请方式一样


def send_mail(to, title, content):
    msg = MIMEText(content)
    msg["Subject"] = title
    msg["From"] = username
    msg["To"] = to

    try:
        s = smtplib.SMTP_SSL("smtp.163.com", 465)  # smtp.163.com 设置成qq or 163 ，我是用163邮箱所以设成163了
        s.login(username, password)
        s.sendmail(username, to, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied,%s" % e)


if __name__ == "__main__":
    if type['key'] == 'to' :
        for item in to:
            send_mail(item, title, content)
    elif type['key'] == 'option':
        for item in option:
            send_mail(item['to'],item['title'],item['content'])
