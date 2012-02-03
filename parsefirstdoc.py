#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import StringIO
import re
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

def BaseName(filename):
    if filename.endswith('.pdf'):
        namear = filename.split('.')
        print "basename:", namear[0]
        return namear[0]

def GenerateTempParsedFile(filename, codec = 'utf-8'):
    outfile = BaseName(filename) + "_tempparsed.txt"
    rsrc = PDFResourceManager()
    outfp = file(outfile, 'w')
    device = TextConverter(rsrc, outfp, codec=codec, laparams=None)

    fp = file(filename, 'rb')
    process_pdf(rsrc, device, fp, None, maxpages=0, password='')
    fp.close()

    device.close()
    outfp.close()

def ConvertToChineseText(filename, codec = 'utf-8'):
    fromfile = BaseName(filename) + "_tempparse.txt"
    result = BaseName(filename) + "_parsed.txt"
    fromfd = open(fromfile, 'r+')
    str = fromfd.read()
    result = open(result, 'wb+')

    length = len(str)
    i = 0

    while (i < length):
        if str[i] == '(':
            if str[i+1:i+5] != "cid:":
                result.write(str[i])
                i += 1
                continue
            i += 5
            codestr = ""
            while str[i] != ')':
                codestr += str[i]
                i += 1
            i += 1
            codeint = int(codestr)
            #print unichr(codeint)
            result.write(unichr(codeint).encode('utf-8'))
        else:
            result.write(str[i])
            i += 1

    fromfd.close()
    result.close()

def Search(filename):
    fromfile = BaseName(filename) + "_parsed.txt"
    fromfd = open(fromfile, 'r+')
    str = fromfd.read()
    str = str.decode('utf-8')
    
    myre1 = re.compile(ur'(（\w+）)招标方式', re.UNICODE)
    m1 = myre1.search(str)

    if m1:
        print "m1 match"
        print m1.group(1)

    myre2 = re.compile(ur'开发银行', re.UNICODE)
    m2 = myre2.search(str)
    if m2:
        print "m2 match"
    else:
        print "m2 not match"

if __name__ == "__main__":
    filename = "m2.pdf"
    GenerateTempParsedFile(filename)
    ConvertToChineseText(filename)
    Search(filename)
    


            
            
    
    
