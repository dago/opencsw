# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = webalizer
VERSION = 2.23
SUBREV = 05
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = A flexible web server log file analysis program
define BLURB
endef

MASTER_SITES = ftp://ftp.mrunix.net/pub/webalizer/
DISTNAME = $(NAME)-$(VERSION)-$(SUBREV)
DISTFILES += $(DISTNAME)-src.tgz

PATCHFILES += 0001-Force-void-context.patch

# Having u_int64_t defined during autoconf-time disturbs detection of BerkeleyDB db.h
# so we disable the test below and re-add the definition manually in webalizer.h
PATCHFILES += 0002-Re-add-definition-on-u_int64_t.patch

VENDOR_URL = http://www.webalizer.org

BUILD_DEP_PKGS += CSWlibgd-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWgeoip-dev

PACKAGES += CSWwebalizer
SPKG_DESC_CSWwebalizer = A flexible web server log file analysis program
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibgd2
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibz1
RUNTIME_DEP_PKGS_CSWwebalizer += CSWbdb48
RUNTIME_DEP_PKGS_CSWwebalizer += CSWgeoip
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibbz2-1-0

# Fix config file later
CHECKPKG_OVERRIDES_CSWwebalizer += file-with-bad-content|/usr/share|root/etc/opt/csw/webalizer.conf.CSW

EXTRA_INC = $(prefix)/bdb48/include
EXTRA_LIB = $(prefix)/bdb48/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dns
CONFIGURE_ARGS += --enable-bz2
CONFIGURE_ARGS += --enable-geoip
#CONFIGURE_ARGS += --with-geoip=DIR        Alternate location for libGeoIP header files
#CONFIGURE_ARGS += --with-geoiplib=DIR     Alternate location for geoip library
CONFIGURE_ARGS += --with-geodb=$(sharedstatedir)/GeoDB

# This is also defined in db.h from BerkeleyDB and causes trouble when being defined twice (see patch above)
CONFIGURE_ARGS += ac_cv_type_u_int64_t=yes

# There is no testsuite
TEST_SCRIPTS =

MIGRATE_FILES += webalizer.conf
PRESERVECONF += $(sysconfdir)/webalizer.conf

EXTRA_PAX_ARGS += -s ',/webalizer\.conf\.sample$$,/webalizer.conf.CSW,'

include gar/category.mk

