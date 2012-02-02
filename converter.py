#!/usr/bin/evn python
# -*- coding: utf-8 -*-

filename = "pdf2.txt"
result = "res2.txt"
str = open(filename, 'r+').read()
res = open(result, 'wb+')
print "str:", str

leftbr = False
length = len(str)
i = 0
while (i < length):
    if str[i] == '(':
        assert str[i+1:i+5] == "cid:"
        i += 5
        codestr = ""
        while str[i] != ')':
            codestr += str[i]
            i += 1
        i += 1
        codeint = int(codestr)
        print unichr(codeint)
        res.write(unichr(codeint).encode('utf-8'))
    else:
        res.write(str[i])
        i += 1


        
