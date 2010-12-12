# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = twisted
MAJ_VERSION = 10.1
PATCHLEVEL = 0
VERSION = $(MAJ_VERSION).$(PATCHLEVEL)
CATEGORIES = python

define BLURB
  Twisted is a networking engine written in Python, supporting numerous
  protocols. It contains a web server, numerous chat clients, chat servers,
  mail servers, and more.
endef

PACKAGES      = CSWpy-twisted CSWtwisted
UPSTREAM_NAME = Twisted
DISTNAME      = $(UPSTREAM_NAME)-$(VERSION)
MASTER_SITES  = http://tmrc.mit.edu/mirror/$(NAME)/$(UPSTREAM_NAME)/$(MAJ_VERSION)/
DISTFILES     = $(DISTNAME).tar.bz2
UFILES_REGEX  = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
TEST_SCRIPTS  = 
LICENSE       = LICENSE
PKGFILES_CSWtwisted = NONE
RUNTIME_DEP_PKGS_CSWtwisted = CSWpy-twisted
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWlibpython2-6-1-0
SPKG_DESC_CSWtwisted = An event-driven networking engine
SPKG_DESC_CSWpy-twisted = An empty transitional package
CATALOGNAME_CSWtwisted = twisted
CATALOGNAME_CSWpy-twisted = py_twisted
# CSWtwisted is now empty, so we need to tell checkpkg that it really needs to
# depend on these two packages.
ARCHALL_CSWtwisted = 1
CHECKPKG_OVERRIDES_CSWtwisted += surplus-dependency|CSWpy-twisted
CHECKPKG_OVERRIDES_CSWtwisted += surplus-dependency|CSWpython
include gar/category.mk
