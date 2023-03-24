#执行sql函数的自定义模块 exsql.py  0813&0829开发 0917:修改print为return
#v1.1
#用法:from exsql import execute
# execute(sql语句)
def execute(sql):
	#创建连接
	import pymysql
	con =pymysql.connect(
	host = '127.0.0.1',
	port =3306,
	user = 'root',
	password = 'root',
	db = 'wk',
	charset = 'utf8'
	)
	#建立游标
	cur=con.cursor()
	#执行sql语句 导出数据库oems到sql.xlsx

	#sql='SELECT*FROM oems into OUTFILE "sql.xls" '
	cur.execute(sql)
	#提交 *无参数；commit（）在con下;执行多条语句后一次性提交
	con.commit()
	#获取反馈
	# print(cur.fetchall())
	return(cur.fetchall()) 
	#关闭连接
	con.close()