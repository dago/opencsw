# Copyrigh 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = chkconfig
VERSION = 1.3.30c
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = RedHat alternatives engine with CSW customizations
define BLURB
  Alternatives system from Red Hat
endef

MASTER_SITES = http://www.sfr-fresh.com/unix/privat/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWalternatives.i.cswalternatives
DISTFILES += CSWalternatives.r.cswalternatives
PATCHFILES = alloca.patch
PATCHFILES += 0001-Add-missing-include-to-alloca.h.patch
PATCHFILES += 0002-Don-t-use-named-struct-initializers.patch
PATCHFILES += 0003-Fix-manpage-to-use-csw-pathes.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWchkconfig CSWalternatives

SPKG_DESC_CSWchkconfig = Checkconfig engine from Red Hat chkconfig-$(VERSION)
SPKG_DESC_CSWalternatives = Alternatives engine from Red Hat chkconfig-$(VERSION)

RUNTIME_DEP_PKGS  = CSWggettextrt CSWlibpopt

PKGFILES_CSWalternatives = .*alternatives.*

CONFIGURE_ARGS = $(DIRPATHS)
# The pathes are hardcoded in the manpage. If you adjust them here
# make sure to adjust it too.
CONFIGURE_ARGS += --with-alt-links-dir=/etc/opt/csw/alternatives
CONFIGURE_ARGS += --with-alt-admin-dir=/var/opt/csw/alternatives

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)/etc/opt/csw/alternatives
	ginstall -d $(PKGROOT)/etc/opt/csw/preserve/CSWalternatives/alternatives
	ginstall -d $(PKGROOT)/var/opt/csw/alternatives
	ginstall -d $(PKGROOT)/usr/sadm/install/scripts
	ginstall $(WORKDIR)/CSWalternatives.i.cswalternatives $(PKGROOT)/usr/sadm/install/scripts/i.cswalternatives
	ginstall $(WORKDIR)/CSWalternatives.r.cswalternatives $(PKGROOT)/usr/sadm/install/scripts/r.cswalternatives
	@$(MAKECOOKIE)
