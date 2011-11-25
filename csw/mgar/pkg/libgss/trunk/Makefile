NAME = gss
VERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = GNU Generic Security Service
define BLURB
endef

MASTER_SITES += $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnu.org/software/$(GNU_PROJ)

PACKAGES += CSWlibgss3
SPKG_DESC_CSWlibgss3 = GNU Generic Security Service, libgss.so.3
PKGFILES_CSWlibgss3 += $(call pkgfiles_lib,libgss.so.3)
RUNTIME_DEP_PKGS_CSWlibgss3 += CSWlibintl8

PACKAGES += CSWlibgss-dev
SPKG_DESC_CSWlibgss-dev = Development files for libgss.so.3
PKGFILES_CSWlibgss-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgss-dev += CSWlibgss3

PACKAGES += CSWgss
SPKG_DESC_CSWgss = GNU Generic Security Service
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgss += CSWlibgss3
RUNTIME_DEP_PKGS_CSWgss += CSWlibintl8

BUILD64 = 1

include gar/category.mk

