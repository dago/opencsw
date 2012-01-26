# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Unreal
VERSION = 3.2.8.1
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Open Source IRC Server
DISTNAME = $(NAME)3.2

define BLURB
endef

MASTER_SITES = http://www.unrealircd.com/downloads/

DISTFILES  = $(NAME)$(VERSION).tar.gz
PATCHFILES += 0001-Remove-inline-as-it-confuses-the-compiler.patch

VENDOR_URL = http://www.unrealircd.com


CONFIGURE_ARGS += --prefix=$(prefix)
#CONFIGURE_ARGS += $(DIRPATHS)
#CONFIGURE_ARGS += --with-showlistmodes
#CONFIGURE_ARGS += --enable-hub
#CONFIGURE_ARGS += --enable-ssl=/opt/csw
#CONFIGURE_ARGS += --enable-ziplinks=/opt/csw/lib
#CONFIGURE_ARGS += --enable-inet6
#CONFIGURE_ARGS += --enable-prefixaq
#CONFIGURE_ARGS += --with-listen=5
#CONFIGURE_ARGS += --with-dpath=/etc/opt/csw
#CONFIGURE_ARGS += --with-spath=/opt/csw/bin/ircd
#CONFIGURE_ARGS += --with-nick-history=2000
#CONFIGURE_ARGS += --with-sendq=3000000
#CONFIGURE_ARGS += --with-bufferpool=18
#CONFIGURE_ARGS += --with-hostname=unstable9s
#CONFIGURE_ARGS += --with-permissions=0600
#CONFIGURE_ARGS += --with-fd-setsize=1024
#CONFIGURE_ARGS += --enable-dynamic-linking

# BUILD_DEP_PKGS = CSWtre-dev
# GARCOMPILER = GNU

CFLAGS =
CPPFLAGS =
LDFLAGS = -ldl
CONFIGURE_ENV =
BUILD_ENV =

include gar/category.mk
