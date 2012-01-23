# $Id$
NAME = libkate
VERSION = 0.3.8
CATEGORIES = lib

DESCRIPTION = A karaoke and text codec for embedding in ogg
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# Skip NUL test until this is fixed:
#   http://code.google.com/p/libkate/issues/detail?id=21
PATCHFILES += 0001-Reformat-null-test-string.patch

# Use inttypes.h if stdint.h is not available until this is fixed:
#   http://code.google.com/p/libkate/issues/detail?id=19
PATCHFILES += 0002-Use-inttypes-when-stdint-is-not-available.patch

VENDOR_URL = http://code.google.com/p/libkate/

PACKAGES += CSWlibkate1
CATALOGNAME_CSWlibkate1 = libkate1
SPKG_DESC_CSWlibkate1 = A karaoke and text codec for embedding in ogg, libkate.so.1
PKGFILES_CSWlibkate1 += $(call pkgfiles_lib,libkate.so.1)

PACKAGES += CSWliboggkate1
CATALOGNAME_CSWliboggkate1 = liboggkate1
SPKG_DESC_CSWliboggkate1 = A karaoke and text codec for embedding in ogg, liboggkate.so.1
PKGFILES_CSWliboggkate1 += $(call pkgfiles_lib,liboggkate.so.1)
RUNTIME_DEP_PKGS_CSWliboggkate1 += CSWlibkate1

PACKAGES += CSWlibkate-dev
CATALOGNAME_CSWlibkate-dev = libkate_dev
SPKG_DESC_CSWlibkate-dev = Development files for libkate.so.1, liboggkate.so.1
PKGFILES_CSWlibkate-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibkate-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWlibkate-dev += CSWlibkate1
RUNTIME_DEP_PKGS_CSWlibkate-dev += CSWliboggkate1

PACKAGES += CSWlibkate-utils
CATALOGNAME_CSWlibkate-utils = libkate_utils
SPKG_DESC_CSWlibkate-utils = Utility programs for libkate
PKGFILES_CSWlibkate-utils += $(bindir)/.*
PKGFILES_CSWlibkate-utils += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWlibkate-utils += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibkate-utils += CSWpng
RUNTIME_DEP_PKGS_CSWlibkate-utils += CSWlibkate1
RUNTIME_DEP_PKGS_CSWlibkate-utils += CSWliboggkate1

PACKAGES += CSWpy-libkate
CATALOGNAME_CSWpy-libkate = py_libkate
SPKG_DESC_CSWpy-libkate = Python binding for libkate.so.1
# PKGFILES is catchall
ARCHALL_CSWpy-libkate = 1
RUNTIME_DEP_PKGS_CSWpy-libkate += CSWpython
PYCOMPILE = 1

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Disable testsuite until this is fixed:
#   http://code.google.com/p/libkate/issues/detail?id=20
SKIPTEST ?= 1

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

post-configure-modulated:
	@# Replace gcc-specific flags until this is fixed:
	@#   http://code.google.com/p/libkate/issues/detail?id=18
	perl -pi -e 's,-Wall -W,,g' \
		$(WORKSRC)/Makefile \
		$(WORKSRC)/tools/Makefile
	perl -pi -e 's,/usr/local,$(prefix),g' \
		$(WORKSRC)/tools/KateDJ/kdj/tools.py
	@$(MAKECOOKIE)
