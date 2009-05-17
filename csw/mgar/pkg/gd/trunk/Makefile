GARNAME = gd
GARVERSION = 2.0.35
CATEGORIES = lib

DESCRIPTION = A library used for dynamic image creation
define BLURB
	GD is an open source code library for the dynamic creation of 
	images by programmers. GD creates PNG, JPEG and GIF images, 
	among other formats. GD is commonly used to generate charts, 
	graphics, thumbnails, and most anything else, on the fly. 
	While not restricted to use on the web, the most common 
	applications of GD involve web site development.
endef

MASTER_SITES = http://www.libgd.org/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWgd
CATALOGNAME_CSWgd = gd
SPKG_DESC_CSWgd = $(DESCRIPTION)

#PATCHFILES = Makefile.diff

REQUIRED_PKGS_CSWgd  = CSWexpat CSWfconfig CSWftype2 CSWiconv 
REQUIRED_PKGS_CSWgd += CSWjpeg CSWpng CSWxpm CSWzlib

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-fontconfig=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-xpm=$(prefix)
CONFIGURE_ARGS += --disable-fast-install

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

post-extract-modulated:
	grm -f $(WORKSRC)/config/ltmain.sh
	gcp /opt/csw/share/libtool/config/ltmain.sh $(WORKSRC)/config/ltmain.sh
	cd $(WORKSRC); aclocal
	cd $(WORKSRC); automake

include gar/category.mk
