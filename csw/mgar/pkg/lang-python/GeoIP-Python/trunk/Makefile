# $Id$

NAME = GeoIP-Python
VERSION = 1.2.7
CATEGORIES = python
GARTYPE = v2

MASTER_SITES = http://www.maxmind.com/download/geoip/api/python/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.maxmind.com/app/python

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWgeoip-dev

PACKAGES = CSWpy-geoip
SPKG_DESC_CSWpy-geoip = Python GeoIP bindings
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibpython2-6-1-0
CHECKPKG_OVERRIDES_CSWpy-geoip += surplus-dependency|CSWpython

# The testsuite is complicated to run, skip for now
TEST_SCRIPTS =

STRIP_DIRS += $(DESTDIR)$(libdir)/python/site-packages

include gar/category.mk
