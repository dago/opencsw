# $Id$
#
NAME = subvertpy
VERSION = 0.9.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Alternative python bindings for subversion

MASTER_SITES = http://samba.org/~jelmer/subvertpy/
DISTFILES  = $(DISTNAME).tar.gz
UPSTREAM_MASTER_SITES = http://pypi.python.org/pypi/subvertpy
LICENSE = COPYING

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-subvertpy += CSWsvn
CHECKPKG_OVERRIDES_CSWpy-subvertpy += missing-dependency|CSWlibuuid1


SVN_LIBRARY_PATH = $(libdir)/svn
SVN_HEADER_PATH = $(includedir)/subversion-1
EXTRA_COMMON_EXPORTS = SVN_LIBRARY_PATH SVN_HEADER_PATH

CONFIGURE_ARGS = $(DIRPATHS)
SVN_PREFIX = /opt/csw
EXTRA_LIB = /opt/csw/lib/svn
TEST_SCRIPTS = 

include gar/category.mk

