# -*- coding: utf8 -*-
import sys
import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time
import os
reload(sys)
sys.setdefaultencoding('utf8')

times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_htmlfile():
    path_name = config.report_path()
    pathname = []

    for (dirpath, dirnames, filenames) in os.walk(path_name):
        for filename in filenames:
            if 'html' in filename:
                pathname.append(os.path.join(dirpath, filename))
    return pathname[0]

def data_statistics():
    txt = '''测试情况如附件：
     
    '''
    return txt
def post_email():
    username = '13541299852@163.com'
    password = '910908HTT'
    sender = username
    receiveSTR = config.post_receiver()

    receivers = ','.join(receiveSTR)
    # 如名字所示： Multipart就是多个部分
    msg = MIMEMultipart('utf-8')
    msg['Subject'] = 'unit Test result'
    msg['From'] = sender
    msg['To'] = receivers

    # 下面是文字部分，也就是纯文本
    txt = data_statistics()
    puretext = MIMEText(txt,'plain','utf-8')
    msg.attach(puretext)

    # 类型的附件
    htmlpart = MIMEApplication(open(get_htmlfile(), 'rb').read())
    htmlpart.add_header('Content-Disposition', 'attachment', filename='testresult.html')
    msg.attach(htmlpart)

    ##发送邮件了
    try:
        '''
        exit_code = os.system('ping 192.168.1.207')
        if exit_code:
            raise Exception('connect failed.')
        '''
        post_emailll(username,password,sender,receiveSTR,msg)
    except:
        print times + '发送失败，正在尝试重新连接，，，，，'
        time.sleep(30)
        post_emailll(username, password, sender, receiveSTR, msg)

def post_emailll(username,password,sender,receiveSTR,msg):
    print times + '正在连接服务器，，，，'
    client = smtplib.SMTP()
    client.connect('smtp.163.com')
    print times + '正在连接发送邮箱'
    client.login(username, password)
    print times + '连接成功'
    client.sendmail(sender, receiveSTR, msg.as_string())
    print times + '正在发送'
    client.quit()
    print times + '邮件发送成功！'