# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# This recipe does not build, because the code is in C++, and Python's setup
# script insists on calling the 'cc' binary instead of 'CC'. I don't know how
# to change it.
#
# upstream bug: http://bugs.python.org/issue1250

NAME = matplotlib
VERSION = 1.1.0
CATEGORIES = python
DESCRIPTION = A pure python plotting library
define BLURB
endef
SPKG_SOURCEURL = http://matplotlib.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE.txt
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
