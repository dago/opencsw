# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libev
VERSION = 4.19
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
CONFIGURE_ARGCONFIGURE_ARGS += ac_cv_header_sys_inotify_h=no
GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1
LICENSE = LICENSE

PACKAGES = CSWlibev4
CATALOGNAME_CSWlibev4 = libev4
PKGFILES_CSWlibev4 += $(call baseisadirs,$(libdir),libev\.so\.4\.0\.0)
PKGFILES_CSWlibev4 += $(call baseisadirs,$(libdir),libev\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibev4 += $(DESCRIPTION), libev.so.4
RUNTIME_DEP_PKGS_CSWlibev4 += CSWlibgcc-s1

PACKAGES += CSWlibev-dev
CATALOGNAME_CSWlibev-dev = libev_dev
SPKG_DESC_CSWlibev-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibev-dev += /opt/csw/lib/sparcv9/libev.so
PKGFILES_CSWlibev-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibev-dev += CSWlibev4
64/libev.so.3.0.0
include gar/category.mk

post-install-modulated:
	mv $(DESTDIR)$(includedir)/event.h $(DESTDIR)$(includedir)/ev-event.h