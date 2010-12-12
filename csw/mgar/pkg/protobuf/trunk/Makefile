# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# http://code.google.com/p/protobuf/issues/detail?id=166
#
# About using stlport4
# http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html

NAME = protobuf
VERSION = 2.3.0
CATEGORIES = lib
define BLURB
	Protocol Buffers are a way of encoding structured data in an efficient yet
	extensible format. Google uses Protocol Buffers for almost all of its
	internal RPC protocols and file formats.
endef
SPKG_SOURCEURL = http://code.google.com/p/protobuf/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PATCHFILES += 0001-Patches-from-GAR.patch
PATCHFILES += 0002-std-map-in-two-more-files.patch
PATCHFILES += OutputDirectoryIsFileError-unittest.patch
PATCHFILES += trailing-slash-test-fails-on-solaris-8-x86.patch
LICENSE = COPYING.txt
EXTRA_CFLAGS = 
EXTRA_CXXFLAGS = -library=stlport4 -library=no%Cstd
EXTRA_LDFLAGS = -lCrun -lm
BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
TEST_TARGET = check
PYCOMPILE = 1

PACKAGES  = CSWprotobuf
PACKAGES += CSWprotobuf-rt
PACKAGES += CSWprotobuf-devel
PACKAGES += CSWpy-protobuf
SPKG_DESC_CSWprotobuf = Google Protocol buffers
SPKG_DESC_CSWprotobuf-rt = $(SPKG_DESC_CSWprotobuf), shared libraries
SPKG_DESC_CSWprotobuf-devel = $(SPKG_DESC_CSWprotobuf), header files
SPKG_DESC_CSWpy-protobuf= $(SPKG_DESC_CSWprotobuf), Python support
CATALOGNAME_CSWprotobuf-rt = protobuf_rt
CATALOGNAME_CSWprotobuf-devel = protobuf_devel
CATALOGNAME_CSWpy-protobuf = py_protobuf
PKGFILES_CSWprotobuf += $(bindir).*protoc.*
PKGFILES_CSWprotobuf += $(libdir).*protoc.*
PKGFILES_CSWprotobuf-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWprotobuf-rt = $(libdir).*libprotobuf.*
PKGFILES_CSWpy-protobuf = $(libdir)/python.*

ARCHALL_CSWpy-protobuf = 1
RUNTIME_DEP_PKGS_CSWprotobuf += CSWprotobuf-rt
RUNTIME_DEP_PKGS_CSWprotobuf += CSWstlport
RUNTIME_DEP_PKGS_CSWprotobuf += CSWzlib
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWprotobuf
RUNTIME_DEP_PKGS_CSWprotobuf-rt += CSWstlport
RUNTIME_DEP_PKGS_CSWprotobuf-rt += CSWzlib
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWprotobuf

include gar/category.mk

post-build-modulated:
	(cd $(WORKSRC)/python; python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python; python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	@$(MAKECOOKIE)
