# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mpg321
VERSION = 0.3.2
GARTYPE = v2

DESCRIPTION = A Free, fast fixed-point math replacement for mpg123

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)-$(VERSION)-orig
DISTFILES += $(NAME)_$(VERSION).origLES  = $(DISTNAME).tar.gz

VENDOR_URL = http://mpg321.sourceforge.net/

RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibao4
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibmad0
RUNTIME_DEP_PKGS_CSWmpg30

BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibmad-dev
BUILD_DEP_PKGS += CSWlibid3tag-dev

EXTRA_LINKER_FLAGS += -lrt

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-mpg123-symlink=no
CONFIGURE_ARGS += --enable-ipv6=yes
CONFIGURE_ARGS += --enable-alsa=no

include gar/category.mk
