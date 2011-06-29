NAME = libassuan
VERSION = 2.0.2
CATEGORIES = lib

DESCRIPTION = IPC library used by some GnuPG related software
define BLURB
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libassuan/
DISTFILES  = $(DISTNAME).tar.bz2

# Use this patch unless this is fixed:
#   https://bugs.g10code.com/gnupg/issue1282
#PATCHFILES = 0001-Add-INADDR_NONE-for-Solaris.patch

VENDOR_URL = http://www.gnupg.org/download/#libassuan

BUILD_DEP_PKGS += CSWgpgerr
BUILD_DEP_PKGS += CSWpth

PACKAGES += CSWlibassuan0
SPKG_DESC_CSWlibassuan0 = IPC library used by some GnuPG related software, libassuan.so.0
PKGFILES_CSWlibassuan0 += $(call pkgfiles_lib,libassuan.so.0)
RUNTIME_DEP_PKGS_CSWlibassuan0 += CSWlibgpg-error0
OBSOLETED_BY_CSWlibassuan0 += CSWlibassuan

PACKAGES += CSWlibassuan-dev
SPKG_DESC_CSWlibassuan-dev = Development files for libassuan.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibassuan-dev += CSWlibassuan0

BUILD64 = 1

# EXTRA_LDFLAGS = -lrt -lsocket -lnsl

# Disable tests until this is fixed:
#   https://bugs.g10code.com/gnupg/msg3633
# SKIPTEST ?= 1

include gar/category.mk
