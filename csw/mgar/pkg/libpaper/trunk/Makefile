GARNAME = libpaper
GARVERSION = 1.1.23
GARSUBREV = nmu1
CATEGORIES = lib

DESCRIPTION = Library and tools for handling papersize
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.us.debian.org/debian/pool/main/libp/libpaper/
DISTFILES  = $(GARNAME)_$(GARVERSION)+$(GARSUBREV).tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)+$(GARSUBREV)

PACKAGES = CSWlibpaper CSWlibpaperdevel
CATALOGNAME_CSWlibpaper = libpaper
CATALOGNAME_CSWlibpaperdevel = libpaper_devel

SPKG_DESC_CSWlibpaper += Library and tools for handling papersize
SPKG_DESC_CSWlibpaperdevel += Library and tools for handling papersize - developer package

RUNTIME_DEP_PKGS_CSWlibpaper = 
RUNTIME_DEP_PKGS_CSWlibpaperdevel += CSWlibpaper

PKGFILES_CSWlibpaperdevel = $(PKGFILES_DEVEL)

UFILES_REGEX = $(GARNAME)_(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = $(MASTER_SITES)

EXTRA_CFLAGS = -Xc

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
