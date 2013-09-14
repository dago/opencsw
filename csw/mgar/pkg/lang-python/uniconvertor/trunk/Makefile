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

REINPLACEMENTS += pyimport
REINPLACE_MATCH_pyimport = imaging.Image, imaging.ImageChops
REINPLACE_WITH_pyimport = imaging
REINPLACE_FILES_pyimport += src/app/scripts/export_raster.py

PACKAGES += CSWuniconvertor
SPKG_DESC_CSWuniconvertor = UniConvertor is a universal vector graphics translator
RUNTIME_DEP_PKGS_CSWuniconvertor += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWuniconvertor += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWuniconvertor += CSWlibpython2-7-1-0

# Can't track this with checkpkg
RUNTIME_DEP_PKGS_CSWuniconvertor += CSWpy-sk1libs
CHECKPKG_OVERRIDES_CSWuniconvertor += surplus-dependency|CSWpy-sk1libs

# Again /usr/share/fonts/ ...
CHECKPKG_OVERRIDES_CSWuniconvertor += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/uniconvertor/app/conf/configurator.py
CHECKPKG_OVERRIDES_CSWuniconvertor += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/uniconvertor/app/conf/configurator.py

# This is intentional as it is a program, not a module
CHECKPKG_OVERRIDES_CSWuniconvertor += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWuniconvertor += catalogname-does-not-start-with-py_

# This is the default font location, I guess Solaris does not ship suitable fonts,
# leave for now until we have something better to depend on
CHECKPKG_OVERRIDES_CSWuniconvertor += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/uniconvertor/app/conf/configurator.py

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

