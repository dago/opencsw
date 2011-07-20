NAME = apr
VERSION = 1.4.5
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE
PATCHFILES = 0001-Force-newly-built-libs-in-testsuite.patch

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-other-child

TEST_TARGET = check

# Make sure for the tests the local libs are preferred, especially for 'testall'.
# Otherwise these tests are failing:
#
# testfmt             : \Line 52: expected <0>, but saw <%ld>
# \Line 74: expected <0>, but saw <%ld>
# /Line 85: expected <14000000>, but saw <%lu>
# \Line 96: expected <d59f80>, but saw <%lx>
# |Line 108: expected <-42>, but saw <%ld>
# FAILED 5 of 9

LD_LIBRARY_PATH=../.lib
export LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

# TBD: This is dependent on 32/64, make sure to have both in separate pathes:
#   /opt/csw/share/build-1/apr_rules.mk

CHECKPKG_OVERRIDES_CSWapr += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/sparcv9/libapr-1.so
CHECKPKG_OVERRIDES_CSWapr += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libapr-1.so
CHECKPKG_OVERRIDES_CSWapr += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWapr += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/sparcv9/libapr-1.so
CHECKPKG_OVERRIDES_CSWapr += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libapr-1.so
CHECKPKG_OVERRIDES_CSWapr += file-with-bad-content|/usr/local|root/opt/csw/share/build-1/libtool

include gar/category.mk

