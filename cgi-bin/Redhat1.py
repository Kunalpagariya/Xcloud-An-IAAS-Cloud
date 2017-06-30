#!/usr/bin/python2

print "content-type:text/html"
print ""


import cgi,cgitb
import os
import random,commands




cgitb.enable()
data=cgi.FormContent()

x=random.randint(5901,5999)
y=str(random.randint(6000,7000))


osname=data['osname'][0] 
MEMORY="1024"
hdsize="10G"
cpu="1" 
port=str(x)			




commands.getstatusoutput("sudo qemu-img create -f qcow2 /root/Desktop/OS/"+osname+".qcow2 "+hdsize)
  

commands.getstatusoutput("sudo virt-install --hvm  --name "+osname+" --memory "+MEMORY+" --disk=/root/Desktop/OS/"+osname+".qcow2 --vcpus="+cpu+"  --cdrom /root/Desktop/OS/rhel7.iso  --os-type linux --noautoconsole  --graphics vnc,listen=0.0.0.0,port="+port)
  
 
commands.getstatusoutput("sudo /root/Desktop/All/websockify-master/run -D "+y+" 127.0.0.1:"+port)  




print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.200/vnc/index.html?host=127.0.0.1&port="+y+"\">\n"
