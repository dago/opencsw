# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = manifold
VERSION = 0.2.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = An SMF service manifest creation tool
define BLURB
endef

MASTER_SITES = http://pypi.python.org/packages/source/M/Manifold/
DISTNAME = Manifold-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://code.google.com/p/manifold/

PACKAGES += CSWmanifold
SPKG_DESC_CSWmanifold = An SMF service manifest creation tool
ARCHALL_CSWpy-manifold = 1

# That is the URL of the DTD to check against
CHECKPKG_OVERRIDES_CSWpy-manifold += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/manifold/manifold.py

include gar/category.mk

