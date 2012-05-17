#!/bin/env python

"""Builds a list of standard libs and stores this in stdlib.json 
   this list/file is needed by find_missing_bins.py

"""

import os
import re
import cjson

fnLiblst = "stdlibs.json"

def buildStdlibList():
  liblst = ['libjawt.so']
  cwd_save = os.getcwd()
  std_locations = (
      '/usr/lib',
      '/usr/dt/lib',
      '/usr/openwin/lib',
      '/usr/X11/lib',
      '/usr/ucblib',
  )
  for libdir in std_locations:
    os.chdir(libdir)
    for lib in os.listdir('.'):
      if re.match('lib[a-zA-Z0-9_-]*.so.[0-9]+$',lib):
        liblst.append(lib)
  os.chdir(cwd_save)
  with open(fnLiblst, 'w') as fd:
    fd.write(cjson.encode(liblst))
    fd.close()
