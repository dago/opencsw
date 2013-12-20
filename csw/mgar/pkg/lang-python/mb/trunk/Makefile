# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mirrorbrain
VERSION = 2.17.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = http://mirrorbrain.org/files/releases/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-New-locations-for-GeoIP-databases.patch

WORKSRC = $(WORKDIR)/$(DISTNAME)/mb

LICENSE = COPYING

PACKAGES += CSWpy-mb
SPKG_DESC_CSWpy-mb = Python module used by the MirrorBrain commandline tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-mb += CSWpy-cmdln
RUNTIME_DEP_PKGS_CSWpy-mb += CSWgeolitedb
# checkpkg cannot detect these deps
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWpy-cmdln
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWgeolitedb

# There is no testsuite
SKIPTEST ?= 1

include gar/category.mk


