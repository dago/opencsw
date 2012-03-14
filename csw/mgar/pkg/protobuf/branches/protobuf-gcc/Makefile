# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# http://code.google.com/p/protobuf/issues/detail?id=166

NAME = protobuf
VERSION = 2.4.1
CATEGORIES = lib
GARTYPE = v2
define BLURB
	Protocol Buffers are a way of encoding structured data in an efficient yet
	extensible format. Google uses Protocol Buffers for almost all of its
	internal RPC protocols and file formats.
endef
SPKG_SOURCEURL = http://code.google.com/p/protobuf/
DESCRIPTION = Google Protocol buffers
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = COPYING.txt
BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
PYCOMPILE = 1

EXTRA_MERGE_EXCLUDE_FILES = .*.pyc

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GNU
prefix = $(BUILD_PREFIX)/gxx

PACKAGES += CSWlibprotobuf-lite7-gxx
PKGFILES_CSWlibprotobuf-lite7-gxx += $(call baseisadirs,$(libdir),libprotobuf-lite\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibprotobuf-lite7-gxx += $(DESCRIPTION), libprotobuf-lite.so.7
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite7-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite7-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite7-gxx += CSWlibz1

PACKAGES += CSWlibprotoc7-gxx
PKGFILES_CSWlibprotoc7-gxx += $(call baseisadirs,$(libdir),libprotoc\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibprotoc7-gxx += $(DESCRIPTION), libprotoc.so.7
RUNTIME_DEP_PKGS_CSWlibprotoc7-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotoc7-gxx += CSWlibprotobuf7-gxx
RUNTIME_DEP_PKGS_CSWlibprotoc7-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibprotoc7-gxx += CSWlibz1

PACKAGES += CSWlibprotobuf7-gxx
PKGFILES_CSWlibprotobuf7-gxx += $(call baseisadirs,$(libdir),libprotobuf\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibprotobuf7-gxx += $(DESCRIPTION), libprotobuf.so.7
RUNTIME_DEP_PKGS_CSWlibprotobuf7-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf7-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibprotobuf7-gxx += CSWlibz1

# Devel package
PACKAGES                           += CSWprotobuf-gxx-dev
SPKG_DESC_CSWprotobuf-gxx-dev         = $(DESCRIPTION), header files
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWpy-protobuf
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibz1
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotobuf7-gxx
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotobuf-lite7-gxx
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotoc7-gxx
# Catch-all package

# Python support
PACKAGES += CSWpy-protobuf
SPKG_DESC_CSWpy-protobuf = $(DESCRIPTION), Python support
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWpython
PKGFILES_CSWpy-protobuf = $(libdir)/python.*
ARCHALL_CSWpy-protobuf = 1

include gar/category.mk

post-build-modulated:
	(cd $(WORKSRC)/python; python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python; python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	@$(MAKECOOKIE)
