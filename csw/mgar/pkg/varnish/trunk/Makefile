# $Id$
NAME = varnish
VERSION = 3.0.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Varnish Web Cache
define BLURB
endef

MASTER_SITES = http://repo.varnish-cache.org/source/
DISTFILES += $(DISTNAME).tar.gz

# From http://www.varnish-cache.org/trac/ticket/663
#PATCHFILES = varnish_autoconf_pthread.patch

VENDOR_URL = http://www.varnish-cache.org

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibpcre-dev

# TBD: http://www.gossamer-threads.com/lists/varnish/bugs/2283

# Otherwise testsuite is failing
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1

EXTRA_CPPFLAGS = -D__inline=

EXTRA_CONFIGURE_EXPORTS = VCC_CC
VCC_CC = $(CC) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) -o %o %s

include gar/category.mk

#pre-configure-modulated:
#	-cd $(WORKSRC) && autoreconf -fi
#	@$(MAKECOOKIE)
