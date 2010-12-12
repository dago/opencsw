NAME = gd
VERSION = 2.0.35
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWgd
CATALOGNAME_CSWgd = gd
SPKG_DESC_CSWgd = $(DESCRIPTION)

#PATCHFILES = Makefile.diff

RUNTIME_DEP_PKGS_CSWgd  = CSWexpat CSWfconfig CSWftype2 CSWiconv 
RUNTIME_DEP_PKGS_CSWgd += CSWjpeg CSWpng CSWxpm CSWzlib CSWlibx11
RUNTIME_DEP_PKGS_CSWgd += CSWlibxpm

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
STRIP_LIBTOOL = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

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

include gar/category.mk

test-skip:
	$(DONADA)

pre-configure-modulated:
	grm -f $(WORKSRC)/config/ltmain.sh
	gcp /opt/csw/share/libtool/config/ltmain.sh $(WORKSRC)/config/ltmain.sh
	cd $(WORKSRC); aclocal
	cd $(WORKSRC); automake
	@$(MAKECOOKIE)

