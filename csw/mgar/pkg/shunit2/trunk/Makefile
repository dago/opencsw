# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = shunit2
GARVERSION = 2.1.5
CATEGORIES = lib
DESCRIPTION = a xUnit unit test framework for Bourne based shell scripts
define BLURB

  shUnit2 is a xUnit unit test framework for Bourne based shell scripts, and it
  is designed to work in a similar manner to JUnit, PyUnit, etc. If you have
  ever had the desire to write a unit test for a shell script, shUnit2 can do
  the job. 

endef
SPKG_SOURCEURL = http://code.google.com/p/shunit2/
MASTER_SITES = $(GOOGLE_MIRROR)
PATCHFILES  = 0001-fix-shlib-path-in-docbookPrep.sh.patch
PATCHFILES += 0002-abspath-instead-of-PWD.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz
ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = shunit2
INSTALL_SCRIPTS = shunit2
TEST_SCRIPTS =
include gar/category.mk

build-shunit2:
	(cd $(WORKSRC) && $(BUILD_ENV) gmake)
	@$(MAKECOOKIE)

install-shunit2:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/shunit2
	ginstall -m 755 -d $(DESTDIR)$(datadir)/doc/shunit2
	ginstall -m 644 $(WORKSRC)/build/shunit2 $(DESTDIR)$(libdir)/shunit2
	ginstall -m 644 $(WORKSRC)/build/shunit2.html $(DESTDIR)$(datadir)/doc/shunit2
	@$(MAKECOOKIE)
