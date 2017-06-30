#!/usr/bin/python


import mysql.connector as mariadb
import cgi,cgitb

print "content-type:text/html"
print ""




cgitb.enable()

data=cgi.FormContent()


username=data['uname'][0]
password=data['upass'][0]

mariadb_connection = mariadb.connect(user='root', password='kunal123', database='USER')
cursor = mariadb_connection.cursor()


sql1="SELECT username From cloudusr where username=%s"
cursor.execute(sql1,(username,))
result=cursor.fetchone()
trigger=str(result)
x=len(trigger)
uname=trigger[3:x-3]

	

sql2="SELECT password From cloudusr where username=%s"
cursor.execute(sql2,(username,))
result=cursor.fetchone()
trigger2=str(result)
x1=len(trigger2)
passwd=trigger2[3:x1-3]



if passwd==password and uname==username:
	print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/home.html\">\n")
else:
	print "<script>alert('Check your password')</script>"
 	print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/index.html\">\n")



	
	




