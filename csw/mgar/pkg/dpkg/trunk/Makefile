# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# This package might provide the dpkg binary itself, but for the time being, it
# provides only update-alternatives.

GARNAME = dpkg
GARVERSION = 1.15.5.3
CATEGORIES = lib
DESCRIPTION = Debian package manager
PACKAGES = CSWalternatives
SPKG_DESC_CSWalternatives = Alternatives management for CSW, based on dpkg
define BLURB
endef
SPKG_SOURCEURL = http://wiki.debian.org/Teams/Dpkg
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/d/dpkg/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = alternatives
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk

install-alternatives:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 \
		$(WORKSRC)/scripts/update-alternatives.pl \
		$(DESTDIR)$(bindir)/update-alternatives
	ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	ginstall -m 644 \
		$(WORKSRC)/man/update-alternatives.8 \
		$(DESTDIR)$(mandir)/man8
	ginstall -m 755 -d $(DESTDIR)$(datadir)/perl/csw/Dpkg
	ginstall -m 644 \
		$(WORKSRC)/scripts/Dpkg.pm \
		$(DESTDIR)$(datadir)/perl/csw
	for f in $(WORKSRC)/scripts/Dpkg/*.pm; do \
		ginstall -m 644 $$f $(DESTDIR)$(datadir)/perl/csw/Dpkg; \
	done
	ginstall -m 755 -d $(DESTDIR)/var$(prefix)/lib/dpkg/alternatives
	ginstall -m 755 -d $(DESTDIR)/etc$(prefix)/alternatives
	@$(MAKECOOKIE)
