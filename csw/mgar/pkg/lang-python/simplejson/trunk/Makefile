# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = simplejson
VERSION = 2.2.1
CATEGORIES = python

DESCRIPTION = JSON encoder and decoder
define BLURB
endef

# Download from github does not really work as there are some suffixes at the end I cannot guess
MASTER_SITES = https://github.com/simplejson/simplejson/tarball/v2.2.1
DISTFILES = $(NAME)-$(VERSION).tar.gz
DISTNAME = simplejson-simplejson-52d0050

VENDOR_URL = http://simplejson.readthedocs.org/

LICENSE = LICENSE.txt

PACKAGES = CSWpy-simplejson
SPKG_DESC_CSWpy-simplejson = JSON encoder and decoder
# Is this really necessary? We are already depending on CSWpython as category == 'python'
RUNTIME_DEP_PKGS_CSWpy-simplejson += CSWlibpython2-6-1-0

include gar/category.mk
