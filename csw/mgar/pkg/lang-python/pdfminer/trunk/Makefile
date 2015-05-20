# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pdfminer
# VERSION = 
GIT_VERSION = HEAD
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES =
GIT_REPOS = http://github.com/euske/$(NAME).git
GIT_TREEISH_pdfminer.git = $(GIT_VERSION)

LICENSE = README.md

# MASTER_SITES = https://pypi.python.org/packages/source/p/$(NAME)/

PACKAGES = CSWpy-pdfminer
ARCHALL_CSWpy-pdfminer = 1
CHECKPKG_OVERRIDES_CSWpy-pdfminer += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/pdfminer/cmapdb.py
CHECKPKG_OVERRIDES_CSWpy-pdfminer += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/pdfminer/cmapdb.py


SKIPTEST = 1

include gar/category.mk

