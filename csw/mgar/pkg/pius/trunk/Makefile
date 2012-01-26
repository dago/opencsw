# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pius
VERSION = 2.0.8
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = A tool for signing and email all UIDs on a set of PGP keys.
define BLURB
endef
SPKG_SOURCEURL = http://www.phildev.net/pius/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = pgpius
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
# What about CSWgnupg2?	
RUNTIME_DEP_PKGS += CSWpython
RUNTIME_DEP_PKGS += CSWgnupg
ARCHALL = 1
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = pius
TEST_SCRIPTS =
PATCHFILES += 0001-Using-opt-csw-paths.patch
CHECKPKG_OVERRIDES_CSWpius += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWpius += surplus-dependency|CSWpython

include gar/category.mk

install-pius:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/pius $(DESTDIR)$(bindir)
	ginstall -m 755 -d $(DESTDIR)$(datadir)/doc/$(NAME)
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(datadir)/doc/$(NAME)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
