NAME = libpaper
VERSION = 1.1.23+nmu1
#GARSUBREV = nmu1
CATEGORIES = lib

DESCRIPTION = Library and tools for handling papersize
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.us.debian.org/debian/pool/main/libp/libpaper/
#DISTFILES  = $(NAME)_$(VERSION)+$(GARSUBREV).tar.gz
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTNAME = $(NAME)-$(VERSION)
#DISTNAME = $(NAME)-$(VERSION)+$(GARSUBREV)

PACKAGES = CSWlibpaper 
#PACKAGES = CSWlibpaper CSWlibpaperdevel
CATALOGNAME_CSWlibpaper = libpaper
#CATALOGNAME_CSWlibpaperdevel = libpaper_devel

SPKG_DESC_CSWlibpaper += $(DESCRIPTION)
#SPKG_DESC_CSWlibpaperdevel += $(DESCRIPTION) - developer package

RUNTIME_DEP_PKGS_CSWlibpaper = 
#RUNTIME_DEP_PKGS_CSWlibpaperdevel += CSWlibpaper

#PKGFILES_CSWlibpaperdevel = $(PKGFILES_DEVEL)

UFILES_REGEX = $(NAME)_(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = $(MASTER_SITES)

EXTRA_CFLAGS = -Xc

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
