# -*- coding: utf-8 -*-

import re
#ur'\(\w+\)招标方式'

file = "res2.txt"
str = open(file).read()

str = str.decode('utf-8')

myre = re.compile(ur'(（\w+）)招标方式', re.UNICODE)
m1 = myre.search(str)
if m1:
    print "m1 match"
    print m1.group(1)

myre2 = re.compile(ur'开发银行', re.UNICODE)
#myre2 = re.compile(ur"\u62db\u6807\u65b9\u5f0f", re.UNICODE)
m2 = myre2.search(str)
if m2:
    print "m2 match"
else:
    print "m2 not"
