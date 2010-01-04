GARNAME = binutils
GARVERSION = 2.20
CATEGORIES = utils

DESCRIPTION = GNU binary utilities: gas, gld, gprof, and others
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# These have been reported as
#   <http://sourceware.org/bugzilla/show_bug.cgi?id=11129>
PATCHFILES  = 0001-Remove-gcc-specific-warning-no-error.patch
PATCHFILES += 0002-Use-func-instead-of-FUNCTION.patch

REQUIRED_PKGS = CSWzlib CSWiconv CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

ifeq ($(GARCH),i386)
CONFIGURE_ARGS += --enable-targets=i386-pc-solaris2.10,i686-pc-mingw32
endif

TEST_TARGET = check

# Do not run tests until this is fixed:
#   <http://sourceware.org/bugzilla/show_bug.cgi?id=11128>
SKIPTEST ?= 1

include gar/category.mk
