NAME = babl
VERSION = 0.1.2
CATEGORIES = gnome

DESCRIPTION = babl is a dynamic, any to any, pixel format translation library
define BLURB
  babl is a library for dynamically handling pixel formats and managing
  conversions between them.  It is being used by GEGL.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gimp/babl/0.1/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

# STRIP_LIBTOOL = 1
PATCHFILES += patch-xml_insert.sh

CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|CIE.so
CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|gimp-8bit.so
CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|gegl-fixups.so
CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|gggl.so
CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|gggl-lies.so
CHECKPKG_OVERRIDES_CSWbabl += symbol-not-found|naive-CMYK.so

TEST_SCRIPTS =

include gar/category.mk

post-configure-modulated:
	gfind $(WORKSRC) -name \*.c | xargs perl -pi \
		-e 's/stdint.h/limits.h/'
	perl -pi -e 's/-pthread/-lpthread/' $(WORKSRC)/tests/Makefile
