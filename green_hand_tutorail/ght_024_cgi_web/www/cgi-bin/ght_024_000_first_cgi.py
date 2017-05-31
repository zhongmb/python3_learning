# -*- coding: UTF-8 -*-
# filename:test.py
'''
cgi测试脚本
http://127.0.0.1/cgi-bin/ght_024_000_first_cgi.py
'''
import os

print("Content-type: text/html")
print()
#print("<meta charset=\"utf-8\">")
print("<b>环境变量</b><br>")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key]))
print("</ul>")
