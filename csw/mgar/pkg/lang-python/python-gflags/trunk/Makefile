# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = python-gflags
VERSION = 2.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Commandline flags module for Python
define BLURB
	This project is the python equivalent of google-gflags, a Google commandline
	flag implementation for C++. It is intended to be used in situations where a
	project wants to mimic the command-line flag handling of a C++ app that uses
	google-gflags, or for a Python app that, via swig or some other means, is
	linked with a C++ app that uses google-gflags.
endef
SPKG_SOURCEURL = http://code.google.com/p/python-gflags/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

UPSTREAM_MASTER_SITES = http://code.google.com/p/$(NAME)/downloads/list
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpy-gflags
CATALOGNAME = py_gflags
ARCHALL_CSWpy-gflags = 1
include gar/category.mk
