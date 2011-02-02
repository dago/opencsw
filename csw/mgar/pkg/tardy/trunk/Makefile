# $Id$
NAME = tardy
VERSION = 1.20
CATEGORIES = utils

DESCRIPTION = A tar(1) Postprocessor
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Add-includes-for-va_list-on-Solaris.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

PACKAGES = CSWtardy
CATALOGNAME_CSWtardy = tardy
SPKG_DESC_CSWtardy = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtardy += CSWzlib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/man1/tardy.1 $(DESTDIR)$(mandir)/man1/tardy.1
