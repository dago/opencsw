# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libev
GARVERSION = 3.9
CATEGORIES = lib
DESCRIPTION = Event loop modelled after libevent
define BLURB
endef
SPKG_SOURCEURL = http://software.schmorp.de/pkg/libev.html
MASTER_SITES = http://dist.schmorp.de/libev/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
NOISAEXEC = 1
TEST_TARGET = check
include gar/category.mk
