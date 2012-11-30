# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = requests
# VERSION = 426734d
VERSION = 0.14.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python HTTP library
define BLURB
  Long description
endef

# MASTER_SITES = https://github.com/kennethreitz/requests/tarball/
MASTER_SITES = http://pypi.python.org/packages/source/r/requests/
DISTFILES  = $(NAME)-$(VERSION).tar.gz


# GIT_REPOS  = http://github.com/kennethreitz/requests.git
# GIT_TREEISH_requests.git = $(VERSION)
NOGITPATCH = 1

REINPLACE_USRLOCAL = requests/utils.py

VENDOR_URL = https://github.com/kennethreitz/requests

RUNTIME_DEP_PKGS += CSWpy-chardet
CHECKPKG_OVERRIDES_CSWpy-requests += surplus-dependency|CSWpy-chardet

PACKAGES = CSWpy-requests
ARCHALL_CSWpy-requests = 1

SKIPTEST = 1

include gar/category.mk

