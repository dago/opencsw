# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = reportlab
VERSION = 2.5
CATEGORIES = python
SPKG_DESC_CSWpy-reportlab = Programatically creating documents in PDF format
define BLURB
  Free Open Source PDF library is suitable for web publishers, developers
  or creative design professionals who need to quickly and easily create
  or automate complex (even data-driven) documents. It lets you create
  professional documents programmatically without being locked into one
  special technology and/or platform. It has grown over years in response
  to the real-world requirements of large financial institutions'
  reporting needs, making it the trusted proven foundation of existing
  enterprise solutions rather than a just a fancy gimmick or interesting
  library.
endef
MASTER_SITES = http://www.reportlab.com/ftp/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES += 0001-Default-location-of-hyphen.mashed.patch
RUNTIME_DEP_PKGS_CSWpy-reportlab = CSWpil
TEST_SCRIPTS =
OBSOLETED_BY_CSWpy-reportlab  = CSWreportlab
OBSOLETED_BY_CSWpy-reportlab += CSWrenderpm
RUNTIME_DEP_PKGS_CSWpy-reportlab += CSWftype2
RUNTIME_DEP_PKGS_CSWpy-reportlab += CSWlibpython2-6-1-0
# Some checks in default locations; won't do any harm.
CHECKPKG_OVERRIDES_CSWpy-reportlab += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/reportlab/rl_config.py
CHECKPKG_OVERRIDES_CSWpy-reportlab += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/reportlab/rl_config.py
# checkpkg does not detect Python deps; also the Python category causes the
# transitional packages to depend on Python (which is okay).
CHECKPKG_OVERRIDES_CSWrenderpm += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWreportlab += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpy-reportlab += surplus-dependency|CSWpil
include gar/category.mk

post-extract-modulated:
	@# The label 'ERR' confuses the compiler on i386
	perl -pi -e 's,ERR,ERRLABEL,g;' \
		$(WORKSRC)/src/rl_addons/renderPM/_renderPM.c
