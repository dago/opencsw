# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pip
VERSION = 1.4.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = A Python easy_install replacement

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

REINPLACE_USRLOCAL += pip/cmdoptions.py
REINPLACE_USRLOCAL += pip/locations.py

ARCHALL_CSWpy-pip = 1

# These are hardcodes for Mac OS X
CHECKPKG_OVERRIDES_CSWpy-pip += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/pip/util.py
CHECKPKG_OVERRIDES_CSWpy-pip += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/pip/util.py

# Testsuite seeems to be broken
TEST_SCRIPTS ?=

include gar/category.mk

