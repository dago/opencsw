# $Id$
NAME = libxspf
VERSION = 1.2.0
CATEGORIES = lib

DESCRIPTION = XSPF Playlist Reading and Writing Support for C++ Applications
define BLURB
endef

SF_PROJ = libspiff
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.lzma

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.lzma

PACKAGES = CSWlibxspf4 CSWlibxspfdevel

CATALOGNAME_CSWlibxspf4 = libxspf4
CATALOGNAME_CSWlibxspfdevel = libxspf_devel

SPKG_DESC_CSWlibxspf4 = $(DESCRIPTION) Runtime Libraries
SPKG_DESC_CSWlibxspfdevel = $(DESCRIPTION) Development Files

RUNTIME_DEP_PKGS_CSWlibxspf4 += CSWliburiparser1
RUNTIME_DEP_PKGS_CSWlibxspf4 += CSWexpat
RUNTIME_DEP_PKGS_CSWlibxspfdevel += CSWlibxspf4
RUNTIME_DEP_PKGS_CSWlibxspfdevel += CSWliburiparser1
RUNTIME_DEP_PKGS_CSWlibxspfdevel += CSWexpat

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxspf4 = $(PKGFILES_RT)

include gar/category.mk
