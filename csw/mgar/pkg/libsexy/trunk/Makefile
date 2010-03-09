GARNAME = libsexy
GARVERSION = 0.1.11
CATEGORIES = lib

DESCRIPTION = Sexy URLs
define BLURB
  Long description
endef

MASTER_SITES = http://releases.chipx86.com/libsexy/libsexy/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibsexy CSWlibsexydevel

CATALOGNAME_CSWlibsexy      = libsexy
CATALOGNAME_CSWlibsexydevel = libsexy_devel

SPKG_DESC_CSWlibsexy      = $(DESCRIPTION)
SPKG_DESC_CSWlibsexydevel = Development files for libsexy

BUILD_DEP_PKGS = CSWglib2devel CSWgtk2devel

RUNTIME_DEP_PKGS_CSWlibsexy = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo CSWlibxml2 CSWpango
RUNTIME_DEP_PKGS_CSWlibsexydevel = CSWlibsexy

VENDOR_URL = http://www.chipx86.com/blog/tag/libsexy/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PKGFILES_CSWlibsexydevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsexydevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk
