# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mixer
VERSION = 1.3
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = A command line utility to set audio volume
define BLURB
  <please fill in>
endef
SPKG_SOURCEURL = http://www.softagalleria.net/mixer.php
MASTER_SITES = http://www.softagalleria.net/download/mixer/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = mixer
INSTALL_SCRIPTS = mixer
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk

build-mixer:
	(cd $(WORKSRC); cc -o mixer mixer.c)
	@$(MAKECOOKIE)

install-mixer:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/mixer $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
