# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libev
VERSION = 3.9
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = A high performance event handling library
define BLURB
  A full-featured and high-performance (see benchmark) event loop that is
  loosely modelled after libevent, but without its limitations and bugs. It is
  used, among others, in the GNU Virtual Private Ethernet and rxvt-unicode
  packages, and in the Deliantra MORPG Server aVENDOR_endef
SPKG_SOURCEURL = http://software.schmorp.de/pkg/libev.h+= http://dist.schmorp.de/libev/
MASTER_SITES += http://dist.schmorp.de/libev/Attic.schmorp.de/libev/
DISTFILES  = $(NAME)-$:\.\d+)*).tar.gz
CONFIGURE_ARGS  = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1
LICENSE = LICENSE
CHECKPKG_OVERRIDES_CSWlibev += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd6
PACKAGES = CSWlibev3
CATALOGNAME_CSWlibev3 = libev3
PKGFILES_CSWlibev3 += $(call baseisadirs,$(libdir),libev\.so\.3\.0\.0)
PKGFILES_CSWlibev3 += $(call baseisadirs,$(libdir),libev\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibev3 += $(DESCRIPTION), libev.so.3
OBSOLETED_BY_CSWlibev3 = CSWlibev

PACKAGES += CSWlibev-dev
CATALOGNAME_CSWlibev-dev = libev_dev
SPKG_DESC_CSWlibev-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibev-dev += /opt/csw/lib/sparcv9/libev.so
RUNTIME_DEP_PKGS_CSWlibev-dev += CSWlibev3
OBSOLETED_BY_CSWlibev-dev = CSWlibev
64/libev.so.3.0.0
include gar/category.mk

post-install-modulated:
	mv $(DESTDIR)$(includedir)/event.h $(DESTDIR)$(includedir)/ev-event.h