# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# Preliminary work done.  It does not compile with Sun CC, there's a syntax
# error.  With GCC, it fails when it doesn't find tre/regex.h, even though
# it's available in /opt/csw/include/tre/regex.h.  The unrealircd build system
# seems to ignore CPPFLAGS.  To be investigated.

NAME = Unreal
VERSION = 3.2.8.1
CATEGORIES = lib
DESCRIPTION = Open Source IRC Server
DISTNAME = $(NAME)3.2
define BLURB
endef
SPKG_SOURCEURL = http://www.unrealircd.com
MASTER_SITES = http://www.unrealircd.com/downloads/
DISTFILES  = $(NAME)$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
BUILD_DEP_PKGS = CSWtre-dev
GARCOMPILER = GNU
include gar/category.mk
