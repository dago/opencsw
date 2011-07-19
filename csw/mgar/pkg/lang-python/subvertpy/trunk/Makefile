# $Id$
#
NAME = subvertpy
VERSION = 0.8.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Alternative python bindings for subversion

MASTER_SITES = http://launchpad.net/subvertpy/trunk/$(VERSION)/+download/
DISTFILES  = $(DISTNAME).tar.gz
UPSTREAM_MASTER_SITES = http://launchpad.net/subvertpy/trunk
LICENSE = COPYING

RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWapr
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWsvn

CONFIGURE_ARGS = $(DIRPATHS)
SVN_PREFIX = /opt/csw
EXTRA_LIB = /opt/csw/lib/svn
TEST_SCRIPTS = 

include gar/category.mk

