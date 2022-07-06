#!/usr/bin/python
#_*_coding:utf-8_*_

import xlrd
import MySQLdb

#打开excel表格
book = xlrd.open_workbook("/root/ITCMDB.xlsx")
sheet = book.sheet_by_index(0)
#建立数据库连接
database = MySQLdb.connect(host = "10.0.2.10",user = "root",passwd = "changeit",db = "CMDB")
database.set_character_set('utf8')
#获得游标对象，用于逐行遍历数据库数据
cursor = database.cursor()
#数据库默认的utf8的编码，导入时使用的是latin-1的编码
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
#创建插入sql语句
query = """INSERT INTO host ( type,mroom,status,hostname,app,ip,user,managerip,os,active,location,produce,warranty,model,serial,cpu,ram,disk,storage) 
VALUES 
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
for r in range(1,sheet.nrows):
	htype = sheet.cell(r,1).value
	mroom = sheet.cell(r,2).value
	status = sheet.cell(r,3).value
	hostname = sheet.cell(r,4).value
	app = sheet.cell(r,5).value
	ip = sheet.cell(r,6).value
	user = sheet.cell(r,7).value
	managerip = sheet.cell(r,8).value
	os = sheet.cell(r,9).value
	active = sheet.cell(r,10).value
	location = sheet.cell(r,11).value
	produce = sheet.cell(r,12).value
	warranty = sheet.cell(r,13).value
	model = sheet.cell(r,14).value
	serial = sheet.cell(r,15).value
	cpu = sheet.cell(r,16).value
	ram = sheet.cell(r,17).value
	disk = sheet.cell(r,18).value
	storage = sheet.cell(r,19).value
	values = (htype,mroom,status,hostname,app,ip,user,managerip,os,active,location,produce,warranty,model,serial,cpu,ram,disk,storage)
	cursor.execute(query,values)
cursor.close()
database.commit()
database.close()
print "导入完成！"
