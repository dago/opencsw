# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mechanize
VERSION = 0.2.4
CATEGORIES = python
DESCRIPTION = Stateful programmatic web browsing in Python
define BLURB
endef
SPKG_SOURCEURL = http://wwwsearch.sourceforge.net/mechanize/
MASTER_SITES = http://wwwsearch.sourceforge.net/$(NAME)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = PKG-INFO
PACKAGES = CSWpy-mechanize
ARCHALL_CSWpy-mechanize = 1
# mechanize does have tests, but they require files that we don't have in the
# package repository.
SKIPTEST = 1
include gar/category.mk
