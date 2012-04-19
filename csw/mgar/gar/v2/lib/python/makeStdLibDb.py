#!/bin/env python

"""Builds a list of standard libs and stores this in stdlib.json 
   this list/file is needed by find_missing_bins.py

"""

from os import listdir, chdir, getcwd
import re
import cjson

fnLiblst = "stdlibs.json"

def buildStdlibList():
  liblst = ['libjawt.so']
  cwd = getcwd()
  chdir('/usr/lib')
  for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
		liblst.append(lib)
  chdir('/usr/dt/lib')
  for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
	    if not lib in liblst:
	        liblst.append(lib)
  chdir('/usr/openwin/lib')
  for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
	    if not lib in liblst:
	        liblst.append(lib)
  chdir('/usr/X11/lib')
  for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
	    if not lib in liblst:
	        liblst.append(lib)
  chdir('/usr/ucblib')
  for lib in listdir('.'):
	if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
	    if not lib in liblst:
	        liblst.append(lib)
  chdir(cwd)
  with open(fnLiblst,'w') as fd:
	fd.write(cjson.encode(liblst))
  fd.close()
