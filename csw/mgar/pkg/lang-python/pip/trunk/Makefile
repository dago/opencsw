# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pip
VERSION = 1.2.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = A Python easy_install replacement

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# These are hardcodes for Mac OS X
CHECKPKG_OVERRIDES_CSWpy-pip += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/pip/locations.py
CHECKPKG_OVERRIDES_CSWpy-pip += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/pip/commands/install.py
CHECKPKG_OVERRIDES_CSWpy-pip += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/pip/util.py

# Testsuite seeems to be broken
TEST_SCRIPTS ?=

include gar/category.mk

