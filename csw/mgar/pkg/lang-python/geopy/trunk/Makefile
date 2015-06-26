# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = geopy
VERSION = 1.10.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Client for several popular geocoding web services.
define BLURB
endef

# git@github.com:geopy/geopy.git
# GIT_REPOS = http://github.com/$(NAME)/$(NAME).git
GIT_REPOS = git://github.com/$(NAME)/$(NAME).git
# proxy: only for URI git, need socat
# GIT_USE_PROXY = 1
GIT_TREEISH_geopy.git = $(VERSION)

LICENSE = LICENSE

# does not work on Python 2.6
MODULATIONS_PYTHON_VERSION = 2_7
CHECKPKG_OVERRIDES_CSWpy-geopy += python-package-missing-py26-files

ARCHALL = 1

include gar/category.mk

