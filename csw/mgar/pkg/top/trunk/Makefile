GARNAME = top
GARVERSION = 3.7
CATEGORIES = apps

DESCRIPTION = Unix system state reporter
define BLURB
endef

SF_PROJ = unixtop
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.unixtop.org/

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=72892
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

BUILD64 = 1

# No runtime linker path as we don't reference any libs from /opt/csw
RUNPATH_LINKER_FLAGS =

# autoconf tries to compile for the current kernel. Get rid of
# these extra flags as we set them ourselves with BUILD64 = 1
BUILD_OVERRIDE_DIRS = ARCHFLAG

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dualarch

# top doesn't have a testsuite
TEST_TARGET =

include gar/category.mk
