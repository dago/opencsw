NAME = djvulibre
VERSION = 3.5.25
GARSUBREV = 3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = DjVu standalone viewer, browser plug-in, command line tools
define BLECTURB
endef

SF_PROJ = djvu
MASTER_SITDjVuLibre/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).$(GARSUBREV $(NAME)-$(VERSION).tar.gz
PATCHFILES += ddjvu.cpp.patch

VENDOR_URL = http://djvu.sourceforge.net/

FOREIGN_PKGS += CSWlibdjvulibre15

PACKAGES += CSWdjvulibre
CATALOGNAME_CSWdjvulibre = djvulibre
SPKG_DESC_CSWdjvulibre += DjVu standalone viewer and ommandline tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWdtiff5bre += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWdjvulibre += CSWlibdjvulibre21
# This is for legacy package expecting to find libdjvulibre.so.15 when pulling in CSWdjvulibre
RUNTIME_DEP_PKGS_CSWdjvulibre += CSWlibdjvulibre15
CHECKPKG_OVERRIDES_CSWdjvulibre += surplus-dependency|Cgister-djvu-mime

PACKAGES += CSWlibdjvulibre21
SPKG_DESC_CSWlibdjvulibre21 += DjVu library, libdjvulibre.so.21
PKGFILES_CSWlibdjvulibre21 += $(call pkgfiles_lib,libdjvulibre.so.21)
OBSOLETED_BY_CSWlibdjvulibre21 += CSWdjvulibrert
CATALOGNAME_CSWdjvulibrert = djvulibre_rt_stub
RUNTIME_DEP_PKGS_CSWlibdjvulibreRUNTIME_DEP_PKGS_CSWlibdjvulibre21 += CSWlibiconv2e21 += CSWlibjpeg7

PACKAGES += CSWlibdjvulibre-dev
SPKG_DESC_CSWlibdjvulibre-dev += Development files for libdjvulibre.so.21
PKGFILES_CSWlibdjvulibre-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibdjvulibre-dev += CSWlibdjvulibre21
OBSOLETED_BY_CSWlibdjvulibre-dev += CSWdjvulibredevel
CATALOGNAME_CSWdjvulibredevel = djvulibre_devel_stub

OPTS = '-DNDEBUG'
PTHREAD_LIBS = -lpthread
PTHREAD_CFLAGS = -D_REENTRANT
EXTRA_COMMON_EXPORTS += OPTS
EXTRA_COMMON_EXPORTS += PTHREAD_LIBS
EXTRA_COMMON_EXPORTS += PTHREAD_CFLAGS

EXTRA_CXXFLAGS += -norunpath
REINPLACE_MATCH = (\|-xarch=)
REINPLACE_WITH = |-norunpath$$1
REINPLACE_FILES += EXTRA_LINKER_FLAGS += -liconv

BUILD64 = 1
ISAEXEC = 1

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk
