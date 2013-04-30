# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# http://code.google.com/p/protobuf/issues/detail?id=166

NAME = protobuf
VERSION = 2.5.0
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

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

EXTRA_LINKER_FLAGS = -lrt

GARCOMPILER = GNU
prefix = $(BUILD_PREFIX)/gxx

PACKAGES += CSWlibprotobuf-lite8-gxx
PKGFILES_CSWlibprotobuf-lite8-gxx += $(call baseisadirs,$(libdir),libprotobuf-lite\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibprotobuf-lite8-gxx += $(DESCRIPTION), libprotobuf-lite.so.8
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite8-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite8-gxx += CSWlibstdc++6

PACKAGES += CSWlibprotoc8-gxx
PKGFILES_CSWlibprotoc8-gxx += $(call baseisadirs,$(libdir),libprotoc\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibprotoc8-gxx += $(DESCRIPTION), libprotoc.so.8
RUNTIME_DEP_PKGS_CSWlibprotoc8-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotoc8-gxx += CSWlibprotobuf8-gxx
RUNTIME_DEP_PKGS_CSWlibprotoc8-gxx += CSWlibstdc++6

PACKAGES += CSWlibprotobuf8-gxx
PKGFILES_CSWlibprotobuf8-gxx += $(call baseisadirs,$(libdir),libprotobuf\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibprotobuf8-gxx += $(DESCRIPTION), libprotobuf.so.8
RUNTIME_DEP_PKGS_CSWlibprotobuf8-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibprotobuf8-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibprotobuf8-gxx += CSWlibz1

# Devel package
PACKAGES                           += CSWprotobuf-gxx-dev
SPKG_DESC_CSWprotobuf-gxx-dev         = $(DESCRIPTION), header files
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWpy-protobuf
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibz1
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotobuf8-gxx
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotobuf-lite8-gxx
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWprotobuf-gxx-dev += CSWlibprotoc8-gxx
# Catch-all package

# Python support
PACKAGES += CSWpy-protobuf
SPKG_DESC_CSWpy-protobuf = $(DESCRIPTION), Python support
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWpython
PKGFILES_CSWpy-protobuf = $(libdir)/python.*
ARCHALL_CSWpy-protobuf = 1

# The 64-bit binaries check misfires because libdir=/opt/csw/gxx/lib but the
# check looks into /opt/csw/lib.
CHECKPKG_OVERRIDES_CSWlibprotobuf8-gxx += 64bits-binaries-missing
CHECKPKG_OVERRIDES_CSWlibprotobuf-lite8-gxx += 64bits-binaries-missing
CHECKPKG_OVERRIDES_CSWlibprotoc8-gxx += 64bits-binaries-missing

include gar/category.mk

post-build-modulated:
	(cd $(WORKSRC)/python; python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python; python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	@$(MAKECOOKIE)
