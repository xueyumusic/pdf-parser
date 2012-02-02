#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import layout_scanner as ls

name = "m2.pdf"
rsname = "m2rs.txt"
fd = open(rsname, "wb+")

toc = ls.get_toc(name)

for u in toc:
	print "level", u[0]
	print "title", u[1]

tc = ls.get_pages(name, images_folder='img')
for u in tc:
	#fd.write(u.decode('utf-8'))
	print "type:", type(u)
	print "str:",u.decode('utf-8')
	a = u.decode('utf-8')
	print "len u:", len(u)
	print "len a:", len(a)
	#for c in u:
		#print "type c:", type(c)
		#print c.decode('utf-8')
	fd.write(u.decode('utf-8'))
