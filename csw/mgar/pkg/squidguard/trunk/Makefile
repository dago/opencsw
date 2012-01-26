# $Id$
NAME = squidguard
VERSION = 1.4
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = URL redirector used to use blacklists with the proxysoftware Squid
define BLURB
endef

MASTER_SITES  = http://squidguard.org/Downloads/
MASTER_SITES += http://squidguard.org/Downloads/Patches/1.4/
DISTNAME = squidGuard-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# These files do patch the source, but they are not in "patch-format"
DISTFILES += squidGuard-1.4-patch-20091015.tar.gz
DISTFILES += squidGuard-1.4-patch-20091019.tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://squidguard.org/

EXTRA_LIB = $(prefix)/bdb48/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS +=  --with-db=$(prefix)/bdb48

include gar/category.mk
