# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = libarchive
VERSION = 2.8.4
CATEGORIES = lib

DESCRIPTION = C library for reading and writing various archive formats
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://code.google.com/p/libarchive/

PACKAGES += CSWlibarchive2
CATALOGNAME_CSWlibarchive2 = libarchive2
SPKG_DESC_CSWlibarchive2 = $(DESCRIPTION), libarchive.so.2
PKGFILES_CSWlibarchive2 = $(call baseisadirs,$(libdir),libarchive\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWxz
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWbzip2
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWosslrt

PACKAGES += CSWlibarchive-devel
CATALOGNAME_CSWlibarchive-devel = libarchive_devel
SPKG_DESC_CSWlibarchive-devel = Development files for libarchive
RUNTIME_DEP_PKGS_CSWlibarchive-devel = CSWlibarchive2
PKGFILES_CSWlibarchive-devel = $(PKGFILES_DEVEL)

PACKAGES += CSWlibarchive
CATALOGNAME_CSWlibarchive = libarchive
SPKG_DESC_CSWlibarchive = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibarchive += CSWiconv
RUNTIME_DEP_PKGS_CSWlibarchive += CSWxz
RUNTIME_DEP_PKGS_CSWlibarchive += CSWzlib
RUNTIME_DEP_PKGS_CSWlibarchive += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibarchive += CSWbzip2
RUNTIME_DEP_PKGS_CSWlibarchive += CSWosslrt

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWlibarchive42)
BUILD_DEP_PKGS += CSWlibxml2devel CSWossldevel 

EXTRA_INC = $(includedir)/cryptopp

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
