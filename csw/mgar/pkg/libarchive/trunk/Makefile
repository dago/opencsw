# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = libarchive
#VERSION = 3.1.2
VERSION = 2.8.4
GARTYPE = v2

DESCRIPTION = C library for reading and writing various archive formats

MASTER_SITES = http://www.libarchive.org/downloads/
DISTFILES += $(DISTNAME).tar.gz
# PATCHFILES += 0001-Consider-name-to-be-NULL-in-ACL-test.patch

VENDOR_URL = http://www.libarchive.org
S_CSWlibarchive2)
BUILD_DEP_PKGS += CSWliblzma-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibbz2-dev
BUILD_DEP_P-dev
BUILD_DEP_PKGS += CSWlibssl-devcom/p/libarchive/

PACKAGES += CSWlibarchive2
SPKG_DESC_CSWlibarchive2 = C library for reading and writing various archive formats, libarchive.so.2
PKGFILES_CSWlibarchive2 = $(call pkgfiles_lib,libarchive.so.2)
RUNTIME_DEP_PKGS_CSWlibalzma52 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWllibssl1-0-0ive2 += CSWosslrt

PACKAGES += CSWlibarchive-dev
SPKG_DESC_CSWlibarchive-dev = Development files for libarchive.so.2
RUNTIME_DEP_PKGS_CSWlibarchive-dev = CSWlibarchive2
PKGFILES_CSWlibarchive-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibarchive-dev += $(mandir)/man5/.*
OBSOLETED_BY_CSWlibarchive-dev += CSWlibarchive-devel

PACKAGES += CSWlibarchive-utils
SPKG_DESC_CSWlibarchive-utils = Tools for reading and writing various# PKGFILES is catchalls += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWliblzma5
RUNTIME_DEP_PKGS_CSWlibarchivbz2-1-0
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibssl1-0-0tiEXTRA_INC = $(includedir)/cryptopp

BUILD64_LIBS_ONLY = 1

BUILD_OVERRIDE_VARS += COMMON_CFLAGS
BUILD_OVERRIDE_VAR_COMMON_CFLAGS =

TEST_OVERRIDE_VARS += COMMON_CFLAGS
TEST_OVERRIDE_VAR_COMMON_CFLAGS =D64_LIBS_ONLY = 1

# There is currently one test failing. Skip until this is fixed:
#   http://code.google.com/p/libarchive/issuSKIPTEST ?= 1

include gar/category.mk
