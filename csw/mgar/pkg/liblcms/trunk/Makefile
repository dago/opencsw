# $Id: Makefile 11888 2010-12-12 12:43:48Z skayser $

NAME = lcms
VERSION = 1.19
GARSUBREV = 
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = The little color management system and tools
define BLURB
        LittleCMS is a CMM, a color management engine; it implements fast transforms
        between ICC profiles. "Little" stands for its small overhead. With a typical
        footprint of about 100K including C runtime, you can color-enable your
        application without the pain of ActiveX, OCX, redistributables or binaries
        of any kind. We are using little cms in several commercial projects, however,
        we are offering lcms library free for anybody under an extremely liberal
        open source license.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)$(GARSUBREV).tar.gz

PATCHFILES += 0001-Keep-norunpath-during-libtool-invocation.patch

VENDOR_URL = http://www.littlecms.com

PACKAGES += CSWliblcms1
SPKG_DESC_CSWliblcms1 = Color management library, liblcms.so.1
PKGFILES_CSWliblcms1 += $(call pkgfiles_lib,liblcms.so.1)
OBSOLETED_BY_CSWliblcms1 = CSWlcmsrt
CATALOGNAME_CSWlcmsrt = lcms_rt_stub

PACKAGES += CSWliblcms-dev
SPKG_DESC_CSWliblcms-dev = Development files for liblcms.so.1
PKGFILES_CSWliblcms-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWliblcms-dev += CSWliblcms1
OBSOLETED_BY_CSWliblcms-dev = CSWlcmsdevel
CATALOGNAME_CSWlcmsdevel = lcms_devel_stub

PACKAGES += CSWliblcms-utils
SPKG_DESC_CSWliblcms-utils = Utility programs for LCMS (Little Color Management)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliblcms-utils += CSWliblcms1
RUNTIME_DEP_PKGS_CSWliblcms-utils += CSWtiff
RUNTIME_DEP_PKGS_CSWliblcms-utils += CSWjpeg
RUNTIME_DEP_PKGS_CSWliblcms-utils += CSWzlib
OBSOLETED_BY_CSWliblcms-utils = CSWlcms
CATALOGNAME_CSWlcms = lcms_stub

PACKAGES += CSWpy-lcms
CATALOGNAME_CSWpy-lcms = py_lcms
SPKG_DESC_CSWpy-lcms += Python bindings for LCMS (Little Color Management)
PKGFILES_CSWpy-lcms = $(libdir).*/python/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-lcms += CSWliblcms1
RUNTIME_DEP_PKGS_CSWpy-lcms += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-lcms += CSWpython

EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no

CONFIGURE_ARGS-32 += --with-python
CONFIGURE_ARGS-64 += --without-python
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

CXXFLAGS += -D_RWSTD_NO_WSTR=1

