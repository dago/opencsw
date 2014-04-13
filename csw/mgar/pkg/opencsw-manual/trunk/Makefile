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
DESCRIPTION 
VENDOR_endef
SPKG_SOURCEURL = http://www.opencsw.o
DISTFILES  = fdl-1.3.txt
DISTFILES += check.shES  = fdl-1.3.txt
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
BUILD_DEP_PKGS += # This is a documentation package, so references to /usr are fine.
CHECKPKG_OVERRIDES_CSWopencsw-manual += file-with-bad-content= CSWpysetuptools

include gar/category.mk

post-extract-modulated:
	rsync -r $(FILEDIR)/ $(WORKSRC)
	@$(MAKECOOKIE)

build-manual:
	(cd $(WORKSRC); gmake html)
	@$(MAKECOOKIE)

install-manual:
	ginsDESTDIR 755 -d $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)
	rsync -rv $(WORKSRCDESTDIRd/html/ $(PKGROOT)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)
	@$(MAKECOOKinstall-modulat$(WORKSRC)/check.sh $(WORKSRC)/conf.pyated: copy-to-web
# define HTDOCS such as to be possible to install anywhere:
copy-to-web: HTDOCS = $(HOME)/public_html
copy-to-web:
	if echo $(DESTDIR) | grep global >/dev/null; then :; else \
	  if [ -d $(HTDOCS)/opencsw-manual ]; then \
		rsync -rv --delete $(DESTDIR)$(docdir)/$(CATALOGNAME_CSWopencsw-manual)/ \
		$(HTDOCS)/opencsw-manual; \
	  fi; \
	fi

.PHONY: copy-to-web
