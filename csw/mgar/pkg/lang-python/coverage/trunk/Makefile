# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = coverage
VERSION = 3.7
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Code coverage measurement for Python

DISTFILES = $(DISTNAME).tar.gz
VENDOR_URL = https://pypi.python.org/pypi/coverage

RUNTIME_DEP_PKGS_CSWpy-coverage += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-coverage += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-coverage += CSWlibpython2-7-1-0

CHECKPKG_OVERRIDES_CSWpy-coverage += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/coverage/html.py
CHECKPKG_OVERRIDES_CSWpy-coverage += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/coverage/html.py

include gar/category.mk
