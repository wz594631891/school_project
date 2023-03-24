#
#version:
#
info="""
开发:叶志豪
说明:用于django项目启动或者更新数据库
版本:1.0 0306 
"""
import os
option=input('输入1运行服务器,2更新数据库')
if option=="1":
	os.system('py manage.py runserver')#运行服务器
	input('回车退出:')
elif option=="2":
	os.system('py manage.py makemigrations&&py manage.py migrate')#更新数据库
	input('回车退出:')

