# Copyrigh 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = chkconfig
GARVERSION = 1.3.30c
CATEGORIES = utils
DESCRIPTION = 
define BLURB
  Alternatives system from Red Hat
endef
SPKG_SOURCEURL = http://www.sfr-fresh.com/unix/privat/chkconfig-1.3.30c.tar.gz/
MASTER_SITES = http://www.sfr-fresh.com/unix/privat/
PATCHFILES = alloca.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWchkconfig CSWalternatives
SPKG_DESC_CSWalternatives = Alternatives engine from Red Hat chkconfig-$(GARVERSION)
PKGFILES_CSWalternatives = .*alternatives.*
CATALOGNAME_CSWalternatives = alternatives
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
