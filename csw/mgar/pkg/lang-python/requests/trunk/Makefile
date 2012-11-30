# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = requests
VERSION = 426734d
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python HTTP library
define BLURB
  Long description
endef

MASTER_SITES = https://github.com/kennethreitz/requests/tarball/
# DISTFILES  = master
# DISTNAME = kennethreitz-requests-426734d

GIT_REPOS  = git://github.com/kennethreitz/requests.git
GIT_TREEISH_requests.git = $(VERSION)
NOGITPATCH = 1

VENDOR_URL = https://github.com/kennethreitz/requests

DEP_PKGS += CSWpy-chardet

PACKAGES = CSWpy-requests
ARCHALL_CSWpy-requests = 1

include gar/category.mk

