GARNAME = gd
GARVERSION = 2.0.35
CATEGORIES = lib

DESCRIPTION = A library used to create PNG images
define BLURB
  gd is a library used to create PNG, JPEG, or WBMP images. It has many nice
  features and can be used in scripts (e.g. PHP) for dynamic image generation.
endef

MASTER_SITES = http://www.libgd.org/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWgd CSWgd-devel
CATALOGNAME_CSWgd = gd
CATALOGNAME_CSWgd-devel = gd_devel
SPKG_DESC_CSWgd = $(DESCRIPTION)
SPKG_DESC_CSWgd-devel = Development headers and libraries for gd

REQUIRED_PKGS_CSWgd  = CSWexpat CSWfconfig CSWftype2 CSWiconv 
REQUIRED_PKGS_CSWgd += CSWjpeg CSWpng CSWxpm CSWzlib CSWsunmath
REQUIRED_PKGS_CSWgd-devel = CSWgd
PKGFILES_CSWgd-devel = $( PKGFILES_DEVEL)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

## fix link bug for php_gd undefined symbols
EXTRA_LINKER_FLAGS += -lsunmath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-fontconfig=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-xpm=$(prefix)


include gar/category.mk
