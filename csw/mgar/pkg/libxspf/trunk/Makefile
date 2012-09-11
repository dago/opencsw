# $Id$
NAME = libxspf
VERSION = 1.2.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = XSPF Playlist Reading and Writing Support for C++ Applications
define BLURB
endef

SF_PROJ = libspiff
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.lzma

PATCHFILES += 0001-Keep-norunpath-during-linkage.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.lzma

PACKAGES += CSWlibxspf4
SPKG_DESC_CSWlibxspf4 = XSPF playlist reading and writing support for C++ applications, libxspf.so.4
PKGFILES_CSWlibxspf4 += $(call pkgfiles_lib,libxspf.so.4)
RUNTIME_DEP_PKGS_CSWlibxspf4 += CSWliburiparser1
RUNTIME_DEP_PKGS_CSWlibxspf4 += CSWlibexpat1

PACKAGES += CSWlibxspf-dev
SPKG_DESC_CSWlibxspf-dev = Development files for libxspf.so.4
RUNTIME_DEP_PKGS_CSWlibxspf-dev += CSWlibxspf4
RUNTIME_DEP_PKGS_CSWlibxspf-dev += CSWliburiparser1
RUNTIME_DEP_PKGS_CSWlibxspf-dev += CSWlibexpat1
OBSOLETED_BY_CSWlibxspf-dev += CSWlibxspfdevel
CATALOGNAME_CSWlibxspfdevel = libxspf_devel_stub

EXTRA_LINKER_FLAGS += -norunpath

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
