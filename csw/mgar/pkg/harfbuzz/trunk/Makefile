# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = harfbuzz
VERSION = 0.9.23
GARTYPE = v2
GARCOMPILER = GNU

DESCRIPTION = OpenType text shaping engine
define BLURB
    The current HarfBuzz tree, also known as harfbuzz-ng, is under active
    development and is what is used in latest versions of Firefox, GNOME,
    ChromeOS, Chrome Linux, LibreOffice, XeTeX, and Android among other places.
endef

MASTER_SITES = http://www.freedesktop.org/software/harfbuzz/release/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES  = CSWharfbuzz-bin
SPKG_DESC_CSWharfbuzz-bin = $(DESCRIPTION), utilities
PKGFILES_CSWharfbuzz-bin = .*/bin/.*

PACKAGES += CSWlibharfbuzz-dev
SPKG_DESC_CSWlibharfbuzz-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibharfbuzz-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibharfbuzz-dev  = CSWlibharfbuzz-icu-0
RUNTIME_DEP_PKGS_CSWlibharfbuzz-dev  = CSWlibharfbuzz-0

PACKAGES += CSWlibharfbuzz-icu-0
SPKG_DESC_CSWlibharfbuzz-icu-0 = $(DESCRIPTION), libharfbuzz-icu.so.0
PKGFILES_CSWlibharfbuzz-icu-0 = $(call pkgfiles_lib,libharfbuzz-icu.so.0)
RUNTIME_DEP_PKGS_CSWlibharfbuzz-icu-0  = CSWlibharfbuzz-0

PACKAGES += CSWlibharfbuzz-0
SPKG_DESC_CSWlibharfbuzz-0 = $(DESCRIPTION), libharfbuzz.so.0
PKGFILES_CSWlibharfbuzz-0 = $(call pkgfiles_lib,libharfbuzz.so.0)

PACKAGES += CSWharfbuzz-doc
SPKG_DESC_CSWharfbuzz-doc = $(DESCRIPTION), documentation
PKGFILES_CSWharfbuzz-doc = .*/gtk-doc.*


BUILD64 = 1

BUILD_DEP_PKGS  = CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibcairo-dev

# There are test scripts in src/ such as check-c-linkage-decls.sh,
# check-symbols.sh, etc. Some of them fail, some do not fail but
# complain objdump hasn't been found.
#
# So, I use a custom target in order to cd'ing to test/ and call make
# check in there.
TEST_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

test-custom:
	cd $(WORKSRC)/test && env $(BUILD_ENV) $(MAKE) check
