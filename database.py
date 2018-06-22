#!/usr/bin/python2

import mysql.connector as mysql # pip install mysql-connector

conn=mysql.connect(user='root',password='123',host='localhost',database='adhoc2')

cur=conn.cursor()
cur.execute("select name,email from student")
output=cur.fetchall()
print output

print "1. insert,   2. exit"

value=raw_input("enter choice")

if value=='1':
	#cur=conn.cursor()
	cur.execute("insert into student (name,email) values ('abhi','gmail.com')")
	print ('one row inserted')
	print(cur.rowcount)
	conn.commit()

else:
	exit()


	




