# $Id$
NAME = WebTest
VERSION = 2.0.9
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Helper to test WSGI applications

DISTFILES  = $(DISTNAME).zip
VENDOR_URL = https://pypi.python.org/pypi/WebTest
PACKAGES += CSWpy-webtest

BUILD_DEP_PKGS += CSWpy-coverage
BUILD_DEP_PKGS += CSWpy-cssselect
BUILD_DEP_PKGS += CSWpy-lxml
BUILD_DEP_PKGS += CSWpy-mock
BUILD_DEP_PKGS += CSWpy-nose
BUILD_DEP_PKGS += CSWpy-pyquery
BUILD_DEP_PKGS += CSWpy-unittest2
DEP_PKGS += CSWpy-beautifulsoup4
DEP_PKGS += CSWpy-ordereddict
DEP_PKGS += CSWpy-six
DEP_PKGS += CSWpy-waitress
DEP_PKGS += CSWpy-webob

ARCHALL = 1

TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWpy-webtest += surplus-dependency|CSWpy-beautifulsoup4
CHECKPKG_OVERRIDES_CSWpy-webtest += surplus-dependency|CSWpy-webob
CHECKPKG_OVERRIDES_CSWpy-webtest += surplus-dependency|CSWpy-waitress
CHECKPKG_OVERRIDES_CSWpy-webtest += surplus-dependency|CSWpy-six
CHECKPKG_OVERRIDES_CSWpy-webtest += surplus-dependency|CSWpy-ordereddict

include gar/category.mk
