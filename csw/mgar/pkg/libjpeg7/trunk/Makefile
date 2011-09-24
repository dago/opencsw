NAME = jpeg
VERSION = 7
CATEGORIES = lib

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
endef

MASTER_SITES = http://www.ijg.org/files/
DISTFILES  = $(NAME)src.v$(VERSION).tar.gz

VENDOR_URL = http://www.ijg.org

LICENSE = README

FOREIGN_PACKAGES += CSWlibjpeg62

PACKAGES += CSWjpeg
CATALOGNAME_CSWjpeg = jpeg
SPKG_DESC_CSWjpeg += JPEG library and tools by the Independent JPEG Group
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjpeg += CSWlibjpeg7 
# This is for legacy packages compiled against libjpeg.so.62 and depend on the unified CSWjpeg which
# contained both shared libraries in the past.
RUNTIME_DEP_PKGS_CSWjpeg += CSWlibjpeg62

# Overwrite this for now until the package has been released
CHECKPKG_OVERRIDES_CSWjpeg += surplus-dependency|CSWlibjpeg62
CHECKPKG_OVERRIDES_CSWjpeg += unidentified-dependency|CSWlibjpeg62

PACKAGES += CSWlibjpeg7
SPKG_DESC_CSWlibjpeg7 += JPEG library and tools by the Independent JPEG Group, libjpeg.so.7
PKGFILES_CSWlibjpeg7 = $(call pkgfiles_lib,libjpeg.so.7)

PACKAGES += CSWlibjpeg-dev
SPKG_DESC_CSWlibjpeg-dev += Development files for libjpeg.so.7
PKGFILES_CSWlibjpeg-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibjpeg-dev += CSWlibjpeg7

BUILD64 = 1
ISAEXEC = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include gar/category.mk
