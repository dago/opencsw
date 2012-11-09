NAME = libpaper
VERSION = 1.1.23+nmu1
#GARSUBREV = nmu1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library and tools for handling papersize
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.us.debian.org/debian/pool/main/libp/libpaper/
#DISTFILES  = $(NAME)_$(VERSION)+$(GARSUBREV).tar.gz
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTNAME = $(NAME)-$(VERSION)
#DISTNAME = $(NAME)-$(VERSION)+$(GARSUBREV)

UFILES_REGEX = $(NAME)_(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = $(MASTER_SITES)

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWlibpaper
SPKG_DESC_CSWlibpaper += $(DESCRIPTION), docs and tools
RUNTIME_DEP_PKGS_CSWlibpaper += CSWlibpaper1

PACKAGES += CSWlibpaper1
CATALOGNAME_CSWlibpaper1 = libpaper1
PKGFILES_CSWlibpaper1 += $(call baseisadirs,$(libdir),libpaper\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibpaper1 += $(DESCRIPTION), libpaper.so.1

PACKAGES += CSWlibpaper-dev
CATALOGNAME_CSWlibpaper-dev = libpaper_dev
SPKG_DESC_CSWlibpaper-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibpaper-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibpaper-dev += CSWlibpaper1
OBSOLETED_BY_CSWlibpaper-dev += CSWlibpaperdevel

EXTRA_CFLAGS = -Xc

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
