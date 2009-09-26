# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libxdg-basedir
GARVERSION = 1.0.2
CATEGORIES = lib
DESCRIPTION = implements functions according to the XDG Base Directory Specification
define BLURB

	The XDG Base Directory Specification defines where should user files be
	looked for by defining one or more base directories relative in with
	they should be located.

	This library implements functions to list the directories according to
	the specification and provides a few higher-level functions.

endef
SPKG_SOURCEURL = http://n.ethz.ch/student/nevillm/download/libxdg-basedir
MASTER_SITES = http://n.ethz.ch/~nevillm/download/libxdg-basedir/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWlibxdgbasedir
CATALOGNAME = libxdg_basedir
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
