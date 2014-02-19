# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = south
MASTER_NAME = South
VERSION = 0.8.4
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Intelligent schema and data migrations for  Django projects
define BLURB
endef

MASTER_SITE_DIR = $(shell echo $(MASTER_NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(MASTER_NAME)/
# MASTER_SITES = http://www.aeracode.org/releases/south/
DISTFILES  = $(MASTER_NAME)-$(VERSION).tar.gz
DISTNAME = $(MASTER_NAME)-$(VERSION)

VENDOR_URL = http://south.aeracode.org/

LICENSE = LICENSE

PACKAGES += CSWpy-south
ARCHALL_CSWpy-south = 1

include gar/category.mk

post-extract: 
	[ ! -f $(WORKSRC)/LICENSE ] && echo "http://www.apache.org/licenses/" > $(WORKSRC)/LICENSE
	$(MAKECOOKIE)
