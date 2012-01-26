# Copyrigh -e '/^##/d' Makefile 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = shflags
VERSION = 1.0.3
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = command-line flags module for Unix shell scripts
define BLURB
endef
SPKG_SOURCEURL = http://code.google.com/p/shflags/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz
ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = shflags
TEST_SCRIPTS = shflags

CONFIGURE_ARGS = $(DIRPATHS)

LICENSE = doc/LICENSE.shunit2

include gar/category.mk

install-shflags:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/shflags
	ginstall -m 644 $(WORKSRC)/src/shflags $(DESTDIR)$(libdir)/shflags
	ginstall -m 755 -d $(DESTDIR)$(docdir)/shflags
	for f in $(WORKSRC)/README* $(WORKSRC)/doc/*; do \
	  ginstall -m 644 $${f} $(DESTDIR)$(docdir)/shflags; \
	done
	@$(MAKECOOKIE)

test-shflags:
	$(WORKSRC)/bin/gen_test_results.sh
	@$(MAKECOOKIE)
