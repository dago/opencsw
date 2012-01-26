# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pycurl
VERSION = 7.19.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = PycURL is a Python interface to libcurl
define BLURB
endef

MASTER_SITES = http://pycurl.sourceforge.net/download/
MASTER_SITES += http://src.opensolaris.org/source/raw/userland/src/components/python/pycurl/patches/
DISTFILES += $(DISTNAME).tar.gz

# Taken from http://src.opensolaris.org/source/xref/userland/src/components/python/pycurl/patches/pycurl-mondo.patch
PATCHFILES += pycurl-mondo.patch
PATCHDIRLEVEL = 0

VENDOR_URL = http://pycurl.sourceforge.net/

PACKAGES += CSWpy-curl
SPKG_DESC_CSWpy-curl = PycURL is a Python interface to libcurl
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibidn11
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-curl += CSWosslrt

# These are docs only
CHECKPKG_OVERRIDES_CSWpy-curl += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pycurl/INSTALL
CHECKPKG_OVERRIDES_CSWpy-curl += file-with-bad-content|/usr/share|root/opt/csw/share/doc/pycurl/ChangeLog

TEST_SCRIPTS = $(WORKSRC)/Makefile
TEST_TARGET = test

include gar/category.mk
