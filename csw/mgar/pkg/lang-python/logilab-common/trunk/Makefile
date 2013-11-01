# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = logilab-common
VERSION = 0.60.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Python Abstract Syntax Tree New Generation
PACKAGES = CSWpy-logilab-common
VENDOR_URL = http://www.logilab.org/project/logilab-common
MASTER_SITES = http://ftp.logilab.org/pub/common/
DISTFILES  = $(DISTNAME).tar.gz
ARCHALL_CSWpy-logilab-common = 1

REINPLACE_USRSHARE += opt/csw/lib/python/site-packages/logilab/common/optik_ext.py
REINPLACE_WHEN_USRSHARE = postinstall

CHECKPKG_OVERRIDES_CSWpy-logilab-common += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/logilab/common/optik_ext.py
CHECKPKG_OVERRIDES_CSWpy-logilab-common += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/logilab/common/optik_ext.py

include gar/category.mk
