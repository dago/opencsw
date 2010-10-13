# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = twisted
MAJ_VERSION = 9.0
PATCHLEVEL = 0
GARVERSION = $(MAJ_VERSION).$(PATCHLEVEL)
CATEGORIES = python

DESCRIPTION = An event-driven networking engine
define BLURB
  Twisted is a networking engine written in Python, supporting numerous
  protocols. It contains a web server, numerous chat clients, chat servers,
  mail servers, and more.
endef

UPSTREAM_NAME = Twisted
DISTNAME      = $(UPSTREAM_NAME)-$(GARVERSION)
MASTER_SITES  = http://tmrc.mit.edu/mirror/$(GARNAME)/$(UPSTREAM_NAME)/$(MAJ_VERSION)/
DISTFILES     = $(DISTNAME).tar.bz2
UFILES_REGEX  = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
TEST_SCRIPTS  = 
LICENSE       = LICENSE

include gar/category.mk
