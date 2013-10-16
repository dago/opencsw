# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = FormEncode
VERSION = 1.2.6
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A validation and form generation package

SPKG_SOURCEURL = http://formencode.org/
PACKAGES = CSWpy-formencode

DISTFILES  = $(NAME)-$(VERSION).zip
ARCHALL_CSWpy-formencode = 1

DEP_PKGS += CSWpy-dns
DEP_PKGS += CSWpy-country

REINPLACE_USRSHARE = $(SITE_PACKAGES)/formencode/api.py
REINPLACE_WHEN_USRSHARE = postinstall

CHECKPKG_OVERRIDES_CSWpy-formencode += surplus-dependency|CSWpy-country
CHECKPKG_OVERRIDES_CSWpy-formencode += surplus-dependency|CSWpy-dns

include gar/category.mk
