#!/bin/env python

from os import listdir, chdir, getcwd
import re
import cjson

fnLiblst = "stdlibs.json"

liblst = []
cwd = getcwd()
chdir('/usr/lib')
for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
		liblst.append(lib)
chdir(cwd)
with open(fnLiblst,'w') as fd:
	fd.write(cjson.encode(liblst))
fd.close()
