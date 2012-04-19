# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Testing
# =======
#
# mkdir -p ~/public_html/opencsw-manual
# mgar install copy-to-web
# point your browser at:
# http://buildfarm.opencsw.org/~${LOGNAME}/opencsw-manual/

NAME = opencsw-manual
VERSION = 0.1
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = OpenCSW manual
define BLURB
endef
SPKG_SOURCEURL = http://www.opencsw.org
MASTER_SITES = http://www.gnu.org/licenses/
DISTFILES  = fdl-1.3.txt
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = manual
INSTALL_SCRIPTS = manual
TEST_SCRIPTS =
ARCHALL_CSWopencsw-manual = 1
# This line is necessary for copy-to-web to work.
CATALOGNAME_CSWopencsw-manual = opencsw_manual
LICENSE = fdl-1.3.txt

BUILD_DEP_PKGS += CSWpy-sphinx
BUILD_DEP_PKGS += CSWrsync
BUILD_DEP_PKGS += CSWpysetuptools

include gar/category.mk

post-extract-modulated:
	rsync -r $(FILEDIR)/ $(WORKSRC)
	@$(MAKECOOKIE)

build-manual:
	(cd $(WORKSRC); gmake html)
	@$(MAKECOOKIE)

install-manual:
	ginstall -m 755 -d $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)
	rsync -rv $(WORKSRC)/_build/html/ $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)
	@$(MAKECOOKIE)

post-install-modulated: copy-to-web
	@$(MAKECOOKIE)

copy-to-web:
	if [ -d $(HOME)/public_html/opencsw-manual ]; then \
		rsync -r $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)/ \
		$(HOME)/public_html/opencsw-manual; \
	fi

.PHONY: copy-to-web
