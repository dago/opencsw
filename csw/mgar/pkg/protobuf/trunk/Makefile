# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# http://code.google.com/p/protobuf/issues/detail?id=166
#
# About using stlport4
# http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html

NAME = protobuf
VERSION = 2.6.1
CATEGORIES = lib
GARTYPE = v2
define BLURB
	Protocol Buffers are a way of encoding structured data in an efficient yet
	extensible format. Google uses Protocol Buffers for almost all of its
	internal RPC protocols and filDESCRIPTION = Google Protocol buffers
MASTER_SITES = https://github.com/google/protobuf/releases/download/v$(VERSION)/
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = https://github.com/google/protobuf/
LICENSE = LICENSE

GARCOMPILER = GNU
BUILD64 = 1
CONFIGURE_ARGS += $(DIRPATHS)

PYCOMPILE = 1

PACKAGES += CSWlibprotobuf-lite9
SPKG_DESC_CSWlibprotobuf-lite9 = $(DESCRIPTION), libprotobuf-lite.so.9
PKGFILES_CSWlibprotobuf-lite9 += $(call pkgfiles_lib,libprotobuf-lite.so.9)
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite9 += CSWlibstdc++6

PACKAGES += CSWlibprotobuf9
SPKG_DESC_CSWlibprotobuf9 = $(DESCRIPTION), libprotobuf.so.9
PKGFILES_CSWlibprotobuf9 += $(call pkgfiles_lib,libprotobuf.so.9)
RUNTIME_DEP_PKGS_CSWlibprotobuf9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf9 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibprotobuf9 += CSWlibz1

PACKAGES += CSWlibprotoc9
SPKG_DESC_CSWlibprotoc9 = $(DESCRIPTION), libprotoc.so.9
PKGFILES_CSWlibprotoc9 += $(call pkgfiles_lib,libprotoc.so.9)
RUNTIME_DEP_PKGS_CSWlibprotoc9 += CSWlibprotobuf9
RUNTIME_DEP_PKGS_CSWlibprotoc9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotoc9 += CSWlibstdc++6

PACKAGES += CSWprotobuf-dev
SPKG_DESC_CSWprotobuf-dev = $(DESCRIPTION), header files
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWpy-protobuf
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWlibprotobuf-lite9
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWlibprotobuf9
RUNTIME_DEP_PKGS_CSWprotobuf-dev += CSWlibprotoc9

# Python support
PACKAGES += CSWpy-protobuf
SPKG_DESC_CSWpy-protobuf= $(DESCRIPTION), Python supportuf += CSWprotobuf
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWpython
PKGFILE+= $(libdir)/python.*
ARCHALL_CSWpy-protobuf = 1
CHECKPKG_OVERRIDES_CSWpy-protobuf += surplus-dependency|CSWprotobuf

# This is intended, no more Python 2.6
CHECKPKG_OVERRIDES_CSWpy-protobuf += python-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-protobuf += surplus-dependency|CSWpython

include gar/category.mk

post-build:
	(cd $(WORKSRC)/python; python setup.py build)
	@$(MAKECOOKIE)

post-installinstall-modulated:
	(cd $(WORKSRC)/python; python setup.py install --root=$(DESTDIR) --prefix=$(prefix))