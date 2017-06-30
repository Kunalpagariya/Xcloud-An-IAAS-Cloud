#!/usr/bin/python2

print "content-type:text/html"
print ""

import mysql.connector as mariadb


import cgi
import cgitb
import time

cgitb.enable()



data=cgi.FormContent()


username=data['uname'][0] 
password=data['upass'][0] 
repassord=data['repass'][0]
email=data['email'][0] 
contact=data['contact'][0]


mariadb_connection = mariadb.connect(user='root', password='kunal123', database='USER')


cursor = mariadb_connection.cursor()

sql1="SELECT username From cloudusr where username=%s"

cursor.execute(sql1,(username,))

result=cursor.fetchone()

trigger=str(result)
if(password==repassord):
      if trigger=='None':
	      sql="INSERT INTO cloudusr values(%s,%s,%s,%s);"
	      cursor.execute(sql,(username,password,email,contact))
	      mariadb_connection.commit()
	      print "<script>alert('Registration successful!')</script>"
	      print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/index.html\">\n"
      else:
	      print "<script>alert('Username Already Exist!')</script>"
	      print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/Register.html\">\n"
else:
      print("<script>alert('PassWords are not same!')</script>")
      print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/Register.html\">\n")
  




 
