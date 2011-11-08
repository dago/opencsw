# $Id$
NAME = tardy
VERSION = 1.25
CATEGORIES = utils

DESCRIPTION = A tar(1) Postprocessor
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3170673&group_id=116896&atid=676344
PATCHFILES += 0001-Add-includes-for-va_list-on-Solaris.patch

PATCHFILES += 0002-Adjust-memchr-return-type.patch

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibexplain-dev

PACKAGES = CSWtardy
SPKG_DESC_CSWtardy = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtardy += CSWlibz1

EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

CONFIGURE_ARGS += AWK=gawk

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/man1/tardy.1 $(DESTDIR)$(mandir)/man1/tardy.1
