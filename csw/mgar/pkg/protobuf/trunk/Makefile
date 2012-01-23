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
DESCRIPTION = Google Protocol buffers
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
BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
PYCOMPILE = 1

PACKAGES  = CSWprotobuf
SPKG_DESC_CSWprotobuf = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWprotobuf += CSWstlport
RUNTIME_DEP_PKGS_CSWprotobuf += CSWzlib
RUNTIME_DEP_PKGS_CSWprotobuf += CSWlibprotoc6
RUNTIME_DEP_PKGS_CSWprotobuf += CSWlibprotobuf6

# Libraries
PACKAGES += CSWlibprotobuf-lite6
CATALOGNAME_CSWlibprotobuf-lite6 = libprotobuf_lite6
SPKG_DESC_CSWlibprotobuf-lite6 = $(DESCRIPTION), libprotobuf-lite.so.6
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite6 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibprotobuf-lite6 += CSWstlport
PKGFILES_CSWlibprotobuf-lite6  = .*libprotobuf-lite\.so\..*
CHECKPKG_OVERRIDES_CSWlibprotobuf-lite6 += bad-rpath-entry

PACKAGES += CSWlibprotobuf6
CATALOGNAME_CSWlibprotobuf6 = libprotobuf6
SPKG_DESC_CSWlibprotobuf6 = $(DESCRIPTION), libprotobuf.so.6
RUNTIME_DEP_PKGS_CSWlibprotobuf6 += CSWstlport
RUNTIME_DEP_PKGS_CSWlibprotobuf6 += CSWzlib
PKGFILES_CSWlibprotobuf6  = .*libprotobuf\.so\..*
CHECKPKG_OVERRIDES_CSWlibprotobuf6 += bad-rpath-entry

PACKAGES += CSWlibprotoc6
CATALOGNAME_CSWlibprotoc6 = libprotoc6
SPKG_DESC_CSWlibprotoc6 = $(DESCRIPTION), libprotoc.so.6
RUNTIME_DEP_PKGS_CSWlibprotoc6 += CSWstlport
RUNTIME_DEP_PKGS_CSWlibprotoc6 += CSWzlib
PKGFILES_CSWlibprotoc6  = .*libprotoc\.so\..*
RUNTIME_DEP_PKGS_CSWlibprotoc6 += CSWlibprotobuf6
CHECKPKG_OVERRIDES_CSWlibprotoc6 += bad-rpath-entry

# Devel package
PACKAGES                           += CSWprotobuf-devel
CATALOGNAME_CSWprotobuf-devel       = protobuf_devel
SPKG_DESC_CSWprotobuf-devel         = $(DESCRIPTION), header files
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWprotobuf
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWpy-protobuf
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWlibprotobuf-lite6
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWlibprotobuf6
RUNTIME_DEP_PKGS_CSWprotobuf-devel += CSWlibprotoc6
PKGFILES_CSWprotobuf-devel          = $(PKGFILES_DEVEL)

# Python support
PACKAGES += CSWpy-protobuf
CATALOGNAME_CSWpy-protobuf = py_protobuf
SPKG_DESC_CSWpy-protobuf= $(DESCRIPTION), Python support
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWprotobuf
RUNTIME_DEP_PKGS_CSWpy-protobuf += CSWpython
PKGFILES_CSWpy-protobuf = $(libdir)/python.*
ARCHALL_CSWpy-protobuf = 1
CHECKPKG_OVERRIDES_CSWpy-protobuf += surplus-dependency|CSWprotobuf

# Empty transitional package
PACKAGES += CSWprotobuf-rt
CATALOGNAME_CSWprotobuf-rt = protobuf_rt
SPKG_DESC_CSWprotobuf-rt = An empty transitional package
PKGFILES_CSWprotobuf-rt = an-empty-package
ARCHALL_CSWprotobuf-rt = 1

include gar/category.mk

post-build-modulated:
	(cd $(WORKSRC)/python; python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python; python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	@$(MAKECOOKIE)
