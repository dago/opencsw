# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = uniconvertor
VERSION = 1.1.5
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = UniConvertor is a universal vector graphics translator

MASTER_SITES = http://uniconvertor.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWuniconvertor
SPKG_DESC_CSWuniconvertor = UniConvertor is a universal vector graphics translator
RUNTIME_DEP_PKGS_CSWuniconvertor += CSWlibpython2-6-1-0

# This is intentional as it is a program, not a module
CHECKPKG_OVERRIDES_CSWuniconvertor += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWuniconvertor += catalogname-does-not-start-with-py_

# This is the default font location, I guess Solaris does not ship suitable fonts,
# leave for now until we have something better to depend on
CHECKPKG_OVERRIDES_CSWuniconvertor += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/uniconvertor/app/conf/configurator.py

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

