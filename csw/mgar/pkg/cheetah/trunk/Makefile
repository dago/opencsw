# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = cheetah
GARVERSION = 2.4.0
CATEGORIES = python
DESCRIPTION = A template engine and code generation tool
define BLURB
  Cheetah is an open source template engine and code generation tool, written
  in Python. It can be used standalone or combined with other tools and
  frameworks. Web development is its principle use, but Cheetah is very
  flexible and is also being used to generate C++ game code, Java, sql, form
  emails and even Python code.
endef
SPKG_SOURCEURL = http://www.cheetahtemplate.org/
MASTER_SITES = http://pypi.python.org/packages/source/C/Cheetah/
DL_NAME = Cheetah
DISTNAME = $(DL_NAME)-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = py_cheetah
PACKAGES = CSWpycheetah
include gar/category.mk
