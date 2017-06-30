#!/usr/bin/python2

import os
import cgi,cgitb

cgitb.enable()

data=cgi.FormContent()

name=data['name'][0]
mkdir= "/media/"+name
command="mount 192.168.0.254:/dev/vg/"+name+" /media/"+name


os.system(mkdir)
os.system(command)
