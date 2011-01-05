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
PKGFILES_CSWlibarchive-devel += $(mandir)/man5/.*

PACKAGES += CSWlibarchive-utils
CATALOGNAME_CSWlibarchive-utils = libarchive_utils
SPKG_DESC_CSWlibarchive-utils = Tools for reading and writing various archive formats
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWiconv
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWxz
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWzlib
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWbzip2
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWosslrt

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWlibarchive42)
BUILD_DEP_PKGS += CSWlibxml2devel CSWossldevel 

EXTRA_INC = $(includedir)/cryptopp

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
