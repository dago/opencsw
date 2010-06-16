# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libev
GARVERSION = 3.9
CATEGORIES = lib
DESCRIPTION = A high performance event handling library
define BLURB
  A full-featured and high-performance (see benchmark) event loop that is
  loosely modelled after libevent, but without its limitations and bugs. It is
  used, among others, in the GNU Virtual Private Ethernet and rxvt-unicode
  packages, and in the Deliantra MORPG Server and Client.
endef
SPKG_SOURCEURL = http://software.schmorp.de/pkg/libev.html
MASTER_SITES = http://dist.schmorp.de/libev/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS  = $(DIRPATHS)
BUILD64 = 1
NOISAEXEC = 1
TEST_TARGET = check
LICENSE = LICENSE
CHECKPKG_OVERRIDES_CSWlibev += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libev.so.3.0.0
include gar/category.mk

post-install-modulated:
	mv $(DESTDIR)$(includedir)/event.h $(DESTDIR)$(includedir)/ev-event.h
	@$(MAKECOOKIE)
