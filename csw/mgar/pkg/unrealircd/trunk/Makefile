# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# Compilation with GCC fails:
# /opt/csw/gcc4/lib/gcc/sparc-sun-solaris2.8/4.3.3/include-fixed/ctype.h:58:
# error: expected ')' before '>=' token

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
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-showlistmodes
CONFIGURE_ARGS += --enable-hub
CONFIGURE_ARGS += --enable-ssl=/opt/csw
CONFIGURE_ARGS += --enable-ziplinks=/opt/csw/lib
CONFIGURE_ARGS += --enable-inet6
CONFIGURE_ARGS += --enable-prefixaq
CONFIGURE_ARGS += --with-listen=5
CONFIGURE_ARGS += --with-dpath=/etc/opt/csw
CONFIGURE_ARGS += --with-spath=/opt/csw/bin/ircd
CONFIGURE_ARGS += --with-nick-history=2000
CONFIGURE_ARGS += --with-sendq=3000000
CONFIGURE_ARGS += --with-bufferpool=18
CONFIGURE_ARGS += --with-hostname=unstable9s
CONFIGURE_ARGS += --with-permissions=0600
CONFIGURE_ARGS += --with-fd-setsize=1024
CONFIGURE_ARGS += --enable-dynamic-linking

BUILD_DEP_PKGS = CSWtre-dev
GARCOMPILER = GNU

include gar/category.mk
