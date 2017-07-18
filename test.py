#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   c.execute("select * FROM company where mingcheng like ?", ('%公司%',))  模糊查询汉字

from urllib import parse
import  sqlite3, json
from bottle import post, request, route, static_file, run 
#隐藏cmd窗口
import ctypes    
whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd)   


@route('/chaxun', method='POST')
def chaxun():
	a0 = request.forms.get('a0')
	a0 =parse.unquote(a0)#python 解码encodeurl，urllib模块
	print("chaxun : in=" + a0)
	
	#-----------数据库-----------------------
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	
	c.execute("select * FROM company where mingcheng like ?",('%'+a0+'%',))
	backdata = c.fetchone()
	conn.commit()
	conn.close()
	#-----------数据库-----------------------
	
	if backdata:
		backdata = str(list(backdata))#fetchone()返回tuple，转换位list
	else:
		print("chaxun : out=nothing")
		return
		
	return backdata
	
#///////////////////////////////////////////////////////////
@route('/dayin', method='POST')
def dayin():
	a0 = parse.unquote(request.forms.get('a0'))
	a1 = parse.unquote(request.forms.get('a1'))
	a2 = parse.unquote(request.forms.get('a2'))
	a3 = parse.unquote(request.forms.get('a3'))
	a4 = parse.unquote(request.forms.get('a4'))
	a5 = parse.unquote(request.forms.get('a5'))
	a6 = parse.unquote(request.forms.get('a6'))
	a7 = parse.unquote(request.forms.get('a7'))
	data = (a0,a1, a2, a3, a4, a5, a6, a7)
	
	#-----------数据库-----------------------
	conn2 = sqlite3.connect('test.db')
	c2 = conn2.cursor()
	c2.execute("INSERT INTO company VALUES (?, ?, ?, ?, ?, ?, ?, ?) ",data)

	conn2.commit()
	conn2.close()
	#-----------数据库-----------------------
	return "7"


#静态文件路由
@route('/<filename>')
def server_static(filename):
	return static_file(filename, root='.\\')


run(host='0.0.0.0', port=8080)




