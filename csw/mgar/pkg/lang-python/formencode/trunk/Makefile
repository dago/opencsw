# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = FormEncode
VERSION = 1.2.2
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A validation and form generation package
define BLURB
endef
DL_NAME = FormEncode
DISTNAME = $(DL_NAME)-$(VERSION)
SPKG_SOURCEURL = http://formencode.org/
MASTER_SITES = http://pypi.python.org/packages/source/F/FormEncode/
PACKAGES = CSWpy-formencode
CATALOGNAME_CSWpy-formencode = py_formencode
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = PKG-INFO
ARCHALL_CSWpy-formencode = 1

REINPLACE_USRSHARE = $(libdir)/python2.6/site-packages/formencode/api.py
REINPLACE_WHEN_USRSHARE = postinstall

include gar/category.mk
