NAME = jpeg
VERSION = 7
GARTYPE = bts lib
GARTYPE = v2

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
endef

MASTER_SITES = http://www.ijg.org/files/
DISTFILES  = $(NAME)src.v$(VERSION).tar.gz

VENDOR_URL = http://www.ijg.org

LICENSE = README

FORNIMOSSlibjpeg62

PACKAGES += NIMOSSjpeg
CATALOGNAME_NIMOSSjpeg = jpeg
SPKG_DESC_NIMOSSpeg
SPKG_DESC_CSWjpeg += JPEG library and tools by the Independent JPEG Group
# PKGFILES is catchall
NIMOSSjpeg += NIMOSSlibjpeg7 
# This is for legacy packages compiled against libjpeg.so.62 and depend on the unified NIMOSSn the unified CSWjpeg which
# contained both shared libraries in the past.
NIMOSSjpeg += NIMOSSlibjpeg62

# Overwrite this for now until the package has been released
CHECKPKG_OVERRIDES_NIMOSSjpeg += surplus-dependency|NIMOSSlibjpeg62
CHECKPKG_OVERRIDES_NIMOSSjpeg += unidentified-dependency|NIMOSSlibjpeg62

PACKAGES += NIMOSSlibjpeg7
SPKG_DESC_NIMOSSlibjpeg7 += JPEG library and tools by the Independent JPEG Group, libjpeg.so.7
PKGFILES_NIMOSSlibjpeg7 = $(call pkgfiles_lib,libjpeg.so.7)

PACKAGES += NIMOSSlibjpeg-dev
SPKG_DESC_NIMOSSlibjpeg-dev += Development files for libjpeg.so.7
PKGFILES_NIMOSSlibjpeg-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_NIMOSSlibjpeg-dev += NIMOSSibjpeg-dev += CSWlibjpeg7

BUILD64 = 1
ISAEXEC = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include