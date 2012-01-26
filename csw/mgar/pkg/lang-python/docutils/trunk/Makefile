# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = docutils
VERSION = 0.7
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Plaintext documentation processing system
SPKG_DESC_CSWpy-docutils = $(DESCRIPTION)
define BLURB
  Documentation utilities for Python
endef
PACKAGES += CSWpy-docutils
TEST_SCRIPTS =
SPKG_SOURCEURL = http://docutils.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.gz
INCOMPATIBLE_PKGS_CSWpy-docutils = CSWzope
OBSOLETED_BY_CSWpy-docutils = CSWpydocutils
CATALOGNAME_CSWpydocutils = pydocutils
ARCHALL_CSWpy-docutils = 1
CHECKPKG_OVERRIDES_CSWpydocutils += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpy-docutils += file-with-bad-content|/usr/share|root/opt/csw/share/doc/pydocutils/dev/distributing.txt
include gar/category.mk

post-install-modulated:
	ginstall -m 644 \
		$(WORKSRC)/extras/roman.py \
		$(DESTDIR)$(libdir)/python/site-packages
	ginstall -d $(DESTDIR)$(docdir)
	gcp -Rv $(WORKSRC)/docs $(DESTDIR)$(docdir)/pydocutils
	gcp -Rv $(WORKSRC)/extras $(DESTDIR)$(docdir)/pydocutils
	@$(MAKECOOKIE)
