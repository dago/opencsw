# Copyrigh 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = chkconfig
GARVERSION = 1.3.30c
CATEGORIES = utils

DESCRIPTION = Alternatives system from Red Hat
define BLURB
  Alternatives system from Red Hat
endef

MASTER_SITES = http://www.sfr-fresh.com/unix/privat/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = alloca.patch
PATCHFILES += 0001-Add-missing-include-to-alloca.h.patch
PATCHFILES += 0002-Don-t-use-named-struct-initializers.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWchkconfig CSWalternatives

SPKG_DESC_CSWalternatives = Alternatives engine from Red Hat chkconfig-$(GARVERSION)

PKGFILES_CSWalternatives = .*alternatives.*
CATALOGNAME_CSWalternatives = alternatives

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
