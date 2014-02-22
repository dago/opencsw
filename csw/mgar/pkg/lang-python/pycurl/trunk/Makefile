# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pycurl
VERSION = 7.19.3.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = PycURL is a Python interface to libcurl
define BLURB
endef

MASTER_SITES = http://pycurl.sourceforge.net/download/
MASTER_SITES += http://src.opensolaris.org/source/raw/userland/src/components/python/pycurl/patches/
DISTFILES += $(DISTNAME).tar.gz

# Taken from http://src.opensolaris.org/source/xref/userland/src/components/python/pycurl/patches/pycurl-mondo.patch
#PATCHFILES += pycurl-mondo.patch
PATCHDIRLEVEL = 0

VENDOR_URL = http://pycurl.sourceforge.net/

PACKAGES += CSWpy-curl
SPKG_DESC_CSWpy-curl = PycURL is a Python interface to libcurl
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibidn11
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpy-curl += CSWlibgcc-s1

# These are essentially from libcurl4_feature and are not needed by default
CHECKPKG_OVERRIDES_CSWpy-curl += missing-dependency|CSWlibcares2
CHECKPKG_OVERRIDES_CSWpy-curl += missing-dependency|CSWliblber2-4-2
CHECKPKG_OVERRIDES_CSWpy-curl += missing-dependency|CSWlibrtmp0
CHECKPKG_OVERRIDES_CSWpy-curl += missing-dependency|CSWlibssh2-1
CHECKPKG_OVERRIDES_CSWpy-curl += missing-dependency|CSWlibldap2-4-2

# These are docs only
CHECKPKG_OVERRIDES_CSWpy-curl += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pycurl/INSTALL
CHECKPKG_OVERRIDES_CSWpy-curl += file-with-bad-content|/usr/share|root/opt/csw/share/doc/pycurl/ChangeLog

# Tests have problems ATM, disable while checkpkg is debugged
SKIPTEST ?= 1

TEST_SCRIPTS = $(WORKSRC)/Makefile
TEST_TARGET = test
TEST_ARGS += SHELL=/usr/bin/bash PYTHON=$(PYTHON_EXECUTABLE)


include gar/category.mk
