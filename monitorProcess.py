#_*_coding:utf-8_*_
import sys,os,time
import win32com.client
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from win32gui import *
from sys import executable
from subprocess import Popen,CREATE_NEW_CONSOLE

titels = []

def mails(text):
	# 设置SMTP信息
	mail_host = "email.jinyu66.com"
	mail_user = "xuhongbin@jinyu66.com"
	mail_passwd = "*IK<8ik,"
	# 发送和接收地址
	sender = 'xuhongbin@jinyu66.com'
	receivers = ['xuhongbin@jinyu66.com']

	message = MIMEText(text,'plain','utf-8')
	message['From'] = Header(text,'utf-8')
	message['To'] = Header(receivers[0],'utf-8')
	subject = text
	message['Subject'] = Header(subject,'utf-8')
	# 发送邮件
	print(u"开始发送邮件！！！")
	smtpObj = SMTP_SSL(mail_host,465)
	smtpObj.ehlo()
	smtpObj.login(mail_user, mail_passwd)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print(u"邮件发送成功！！！")

def foo(hwnd,nouse):
	titels.append(GetWindowText(hwnd))

def restart():
	# 关闭进程
	os.system('taskkill /F /IM ezd.exe')
	os.system('taskkill /F /IM ezdmon.exe')
	# 启动新的程序
	Popen(["ezd.exe -c ..\..\config\ezd.conf"], executable="c:\\ThomsonReuters\ezd1.2\win_x86_64\\bin\\",
	      creationflags=CREATE_NEW_CONSOLE)

if __name__ == "__main__":
	# process = []
	# processName = sys.argv[1]
	# wmi = win32com.client.GetObject('winmgmts:')
	# for p in wmi.InstancesOf('win32_process'):
	# 	process.append(p.Name)
	# if processName not in process:
	# 	# mails(processName+"进程已关闭！！！")
	# 	pass
	while True:
		restart()
		EnumWindows(foo,0)
		if "ezd.exe" in titels:
			mails("进程错误，正在重启进程……")
			restart()
		time.sleep(5)
