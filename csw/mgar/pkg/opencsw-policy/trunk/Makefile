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

BUILD_DEP_PKGS += CSWpy-sphinx
BUILD_DEP_PKGS += CSWrsync
BUILD_DEP_PKGS += CSWpysetuptools

include gar/category.mk

post-extract-modulated:
	rsync -r $(FILEDIR)/ $(WORKSRC)
	@$(MAKECOOKIE)

build-policy:
	(cd $(WORKSRC); gmake html)

install-policy:
	ginstall -m 755 -d $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy)
	rsync -rv $(WORKSRC)/_build/html/ $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy)
	@$(MAKECOOKIE)

post-install-modulated: copy-to-web
	@$(MAKECOOKIE)

copy-to-web: $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy)/index.html
	if [ -d $(HOME)/public_html/policy ]; then \
		rsync -r $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-policy)/ \
		$(HOME)/public_html/policy; \
	fi

.PHONY: copy-to-web
