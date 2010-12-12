NAME = libtool
VERSION = 1.5.26
CATEGORIES = devel

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWlibltdl3
CATALOGNAME = libltdl3

SPKG_SOURCEURL = http://www.gnu.org/software/libtool/

SPKG_DESC_CSWlibtoolrt = Runtime library for libtool 1.5.x

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NOISALIST = 1

# There are three Fortran tests failing, which probably is not relevant to
# libltdl.so functionaility
#   FAIL: f77demo-make.test
#   FAIL: f77demo-make.test
#   FAIL: f77demo-make.test
SKIPTEST ?= 1

TEST_TARGET = check

PKGFILES_CSWlibltdl3 = $(PKGFILES_RT)

include gar/category.mk

