# $Id$
GARNAME = varnish
GARVERSION = 2.1.3
CATEGORIES = apps

DESCRIPTION = Varnish Web Cache
define BLURB
  Long description
endef

MASTER_SITES = http://www.varnish-software.com/sites/default/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# From http://www.varnish-cache.org/trac/ticket/663
PATCHFILES = varnish_autoconf_pthread.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.varnish-cache.org

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Otherwise testsuite is failing
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

pre-configure-modulated:
	-cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)
