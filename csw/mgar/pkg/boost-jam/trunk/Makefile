# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = boost-jam
VERSION = 3.1.18
GARTYPE = v2
DESCRIPTION = Build tool from the Boost C++ libraries
define BLURB
endef
SPKG_SOURCEURL = http://www.boost.org/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT = boost
DISTFILES  = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = boost_jam
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = bjam
INSTALL_SCRIPTS = bjam
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
LICENSE = LICENSE_1_0.txt
JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

# boost-jam has also the 'sunpro' toolset, but the problem with it is that it
# ignores CFLAGS, while 'cc' honors them.
TOOLSET = cc
include gar/category.mk

build-bjam:
	( cd $(WORKSRC) && \
		$(BUILD_ENV) ./build.sh $(TOOLSET))
	@$(MAKECOOKIE)

install-bjam:
	mkdir -p $(DESTDIR)$(bindir)
	cp $(WORKSRC)/bin.$(JAMDIR)/bjam $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
