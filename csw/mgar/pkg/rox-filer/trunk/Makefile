# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# This software uses custom ways of executing. Gentoo portage uses wrappers to
# set icon directories.

GARNAME = rox-filer
GARVERSION = 2.9
CATEGORIES = apps
DESCRIPTION = A lightweight X file manager
define BLURB
endef
SPKG_SOURCEURL = http://roscidus.com/desktop/ROX-Filer
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = rox
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
REQUIRED_PKGS  = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
REQUIRED_PKGS += CSWlibatk CSWlibcairo CSWlibglade2 CSWlibxml2 CSWpango
REQUIRED_PKGS += CSWbash

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = rox
INSTALL_SCRIPTS = rox
TEST_SCRIPTS =
PACKAGES = CSWroxfiler
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
X_EXTRA_LIBS = -lm
export X_EXTRA_LIBS

build-rox:
	(cd $(WORKSRC); $(BUILD_ENV) ./ROX-Filer/AppRun --compile)
	@$(MAKECOOKIE)

install-rox:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(FILEDIR)/rox-filer $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(libexecdir)
	ginstall $(WORKSRC)/ROX-Filer/ROX-Filer $(DESTDIR)$(libexecdir)
	ginstall -d $(DESTDIR)$(datadir)/ROX
	gcp -av $(WORKSRC)/ROX-Filer/ROX $(DESTDIR)$(datadir)
	gcp -av $(WORKSRC)/ROX-Filer/images $(DESTDIR)$(datadir)/ROX
	gfind $(DESTDIR)$(datadir) -type d -exec chmod 0755 {} \;
	gfind $(DESTDIR)$(datadir) -type f -exec chmod 0644 {} \;
	@$(MAKECOOKIE)

include gar/category.mk
