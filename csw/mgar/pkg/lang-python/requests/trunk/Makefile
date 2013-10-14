# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = requests
VERSION = 2.0.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python HTTP for Humans

DISTFILES  = $(NAME)-$(VERSION).tar.gz

REINPLACE_USRLOCAL = requests/utils.py

VENDOR_URL = https://pypi.python.org/pypi/requests

RUNTIME_DEP_PKGS += CSWpy-chardet
CHECKPKG_OVERRIDES_CSWpy-requests += surplus-dependency|CSWpy-chardet

PACKAGES = CSWpy-requests
ARCHALL_CSWpy-requests = 1

SKIPTEST = 1

include gar/category.mk

