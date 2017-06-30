#!/usr/bin/python2

print "content-type:text/html"
print ""


import cgi,cgitb
import os

cgitb.enable()
data=cgi.FormContent()


x=2 
x1=data['name'][0]
z="lvcreate vg --size +"+x+"G --name "+x1
os.system(z)
format= "mkfs.ext4 /dev/vg/"+x1
os.system(format)
mkdir="mkdir /media/"+x1
os.system(mkdir)
mount= "mount /dev/vg/" + x1 +" /media/"+x1
os.system(mount)


	
 	
    	


