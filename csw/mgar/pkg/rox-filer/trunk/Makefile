# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# This software uses custom ways of executing. Gentoo portage uses wrappers to
# set icon directories.

NAME = rox-filer
VERSION = 2.10
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = A lightweight X file manager
define BLURB
endef
SPKG_SOURCEURL = http://roscidus.com/desktop/ROX-Filer
MASTER_SITES = $(SECTF_MIRRORS)
SF_PROJ = rox
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
RUNTIME_DEP_PKGS_CSWroxfiler  = CSWbash
RUNTIME_DEP_PKGS_CSWroxfiler += CSWfconfig
RUNTIME_DEP_PKGS_CSWroxfiler += CSWftype2
RUNTIME_DEP_PKGS_CSWroxfiler += CSWggettextrt
RUNTIME_DEP_PKGS_CSWroxfiler += CSWglib2
RUNTIME_DEP_PKGS_CSWroxfiler += CSWgtk2
RUNTIME_DEP_PKGS_CSWroxfiler += CSWlibatk
RUNTIME_DEP_PKGS_CSWroxfiler += CSWlibcairo
RUNTIME_DEP_PKGS_CSWroxfiler += CSWlibglade2
RUNTIME_DEP_PKGS_CSWroxfiler += CSWlibgnugetopt
RUNTIME_DEP_PKGS_CSWroxfiler += CSWlibxml2
RUNTIME_DEP_PKGS_CSWroxfiler += CSWpango

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = rox
INSTALL_SCRIPTS = rox
TEST_SCRIPTS =
PACKAGES = CSWroxfiler
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
X_EXTRA_LIBS = -lm
export X_EXTRA_LIBS

LICENSE = ROX-Filer/Help/COPYING

include gar/category.mk

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
	gcp -av $(WORKSRC)/ROX-Filer/Help $(DESTDIR)$(datadir)/ROX
	gcp -av $(WORKSRC)/ROX-Filer/Options.xml $(DESTDIR)$(datadir)/ROX
	gcp -av $(WORKSRC)/ROX-Filer/Messages $(DESTDIR)$(datadir)/ROX
	gcp -av $(WORKSRC)/ROX-Filer/AppInfo.xml $(DESTDIR)$(datadir)/ROX
	ginstall -d -m 755 $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/rox.1 $(DESTDIR)$(mandir)/man1
	gfind $(DESTDIR)$(datadir) -type d -exec chmod 0755 {} \;
	gfind $(DESTDIR)$(datadir) -type f -exec chmod 0644 {} \