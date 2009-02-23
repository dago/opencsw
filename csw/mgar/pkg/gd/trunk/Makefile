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
DISTFILES += fixme.sh

PACKAGES = CSWgd CSWgd-devel
CATALOGNAME_CSWgd = gd
CATALOGNAME_CSWgd-devel = gd_devel
SPKG_DESC_CSWgd = $(DESCRIPTION)
SPKG_DESC_CSWgd-devel = Development headers and libraries for gd

PATCHFILES = Makefile.diff

REQUIRED_PKGS_CSWgd  = CSWexpat CSWfconfig CSWftype2 CSWiconv 
REQUIRED_PKGS_CSWgd += CSWjpeg CSWpng CSWxpm CSWzlib
REQUIRED_PKGS_CSWgd-devel = CSWgd

PKGFILES_CSWgd-devel = $(PKGFILES_DEVEL)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-fontconfig=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-xpm=$(prefix)
CONFIGURE_ARGS += --disable-fast-install

post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

include gar/category.mk
