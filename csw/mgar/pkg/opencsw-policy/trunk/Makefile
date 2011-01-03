# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = opencsw-policy
VERSION = 0.1
CATEGORIES = lib
DESCRIPTION = OpenCSW packaging policy
define BLURB
endef
SPKG_SOURCEURL = http://www.opencsw.org
MASTER_SITES = http://www.gnu.org/licenses/
DISTFILES  = fdl-1.3.txt
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = policy
INSTALL_SCRIPTS = policy
TEST_SCRIPTS =
ARCHALL_CSWopencsw-policy = 1
CATALOGNAME_CSWopencsw-policy = opencsw_policy
LICENSE = fdl-1.3.txt

BUILD_DEP_PKGS = CSWasciidoc

include gar/category.mk

%.html: %.txt
	asciidoc -o $@ $<

build-policy: \
	copy-asciidoc \
	$(WORKSRC)/index.html

copy-asciidoc:
	gcp -v $(FILEDIR)/*.txt $(WORKSRC)

install-policy:
	ginstall -m 755 -d $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy)
	for f in $(WORKSRC)/*.html $(WORKSRC)/*.txt; do \
		ginstall $${f} $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy); \
	done
	@$(MAKECOOKIE)

post-merge:
	cp $(PKGROOT)/opt/csw/share/doc/opencsw_policy/index.html $(HOME)/public_html/policy || true
