NAME = log4cplus
VERSION = 1.0.4.3
GARTYPE = v2

DESCRIPTION = Logging Framework for C++
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWliblog4cplus1-0-4
CATALOGNAME_CSWliblog4cplus1-0-4 = liblog4cplus1_0_4
SPKG_DESC_CSWliblog4cplus1-0-4 += $(DESCRIPTION), liblog4cplus-1.0.so.4
PKGFILES_CSWliblog4cplus1-0-4 += $(call baseisadirs,$(libdir),liblog4cplus-1\.0\.so\.4\.0\.0)
PKGFILES_CSWliblog4cplus1-0-4 += $(call baseisadirs,$(libdir),liblog4cplus-1\.0\.so\.4(\.\d+)*)
RUNTIME_DEP_PKGS_CSWliblog4cplus1-0-4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWliblog4cplus1-0-4 += CSWlibstdc++6

PACKAGES += CSWlog4cplus-dev
CATALOGNAME_CSWlog4cplus-dev = log4cplus_dev
SPKG_DESC_CSWlog4cplus-dev += $(DESCRIPTION), development files
PKGFILES_CSWlog4cplus-dev += /opt/csw/lib/liblog4cplus.so
PKGFILES_CSWlog4cplus-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlog4cplus-dev += CSWliblog4cplus1-0-4

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

