# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libxdg-basedir
VERSION = 1.0.2
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Implements functions according to the XDG Base Directory Specification
define BLURB

	The XDG Base Directory Specification defines where should user files be
	looked for by defining one or more base directories relative in with
	they should be located.

	This library implements functions to list the directories according to
	the specification and provides a few higher-level functions.

endef
SPKG_SOURCEURL = http://n.ethz.ch/student/nevillm/download/libxdg-basedir
MASTER_SITES = http://n.ethz.ch/~nevillm/download/libxdg-basedir/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWlibxdgbasedir
CATALOGNAME = libxdg_basedir
# These settings do not do anything.  xdg-basedir has the paths hardcoded in
# basedir.c, there's a separate patch for it.
# sysconfdir = /etc$(prefix)
# localstatedir = /var$(prefix)
#
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1
PATCHFILES += opencsw-paths.patch
include gar/category.mk
