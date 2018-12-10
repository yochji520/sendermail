#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#@Author:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from mailrest.readconf import *
from mailrest.logs import *

#mail配置信息
mailServerHost = ""
mailServerPort = ""
mailServerAccount = ""
mailServerPasswd = ""
mailIsTrue = True
mailReceiverUser = ""

#发送邮件
def sendmail(tomail, subject, content):
    '''
    根据配置参数执行发送邮件得方式
    :return: 将发送邮件状态记录到日志中，只有成功和失败两种状态
    '''
    isTrue =True
    cnfdata = read_cof()
    mailIsTrue = cnfdata["mail"]["enable"]
    mailServerHost = cnfdata["mail"]["mailServerHost"]
    mailServerAccount = cnfdata["mail"]["mailServerAccount"]
    mailServerPasswd = cnfdata["mail"]["mailServerPasswd"]
    tomails = tomail[4:]
    tomaillist = tomails.split(',')
    message = MIMEMultipart()
    for mailReceiverUser in tomaillist:
        if isTrue == mailIsTrue:
            message['From'] = Header("youchuanjiang@wanbei.tv", 'utf-8')
            message['To'] = Header(mailReceiverUser, 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
            # 构建文件正文
            message.attach(MIMEText(content, 'html', 'utf-8'))
            smtpObj = smtplib.SMTP_SSL(mailServerHost)
            try:
                smtpObj.login(mailServerAccount, mailServerPasswd)
                smtpObj.sendmail(mailServerAccount, mailReceiverUser, message.as_string())
            except IOError as err:
                log = LogtoLog().getlog()
                log.error("登陆失败，或者网络连接异常", err)
        else:
            pass