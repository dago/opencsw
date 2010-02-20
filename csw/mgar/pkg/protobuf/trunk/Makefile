# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = protobuf
GARVERSION = 2.3.0
CATEGORIES = lib
DESCRIPTION = encoding structured data in an efficient yet extensible format
define BLURB
	Protocol Buffers are a way of encoding structured data in an efficient yet
	extensible format. Google uses Protocol Buffers for almost all of its
	internal RPC protocols and file formats.
endef
PACKAGING_PLATFORMS ?= solaris9-sparc solaris9-i386
SPKG_SOURCEURL = http://code.google.com/p/protobuf/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PATCHFILES  = stdint-and-ddi.patch
PATCHFILES += std-map-in-google-protobuf-extension_set.cc.patch
PATCHFILES += stdint-gcc.patch
PATCHFILES += std-map-2.patch
LICENSE = COPYING.txt
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = SOS12
# GARCOMPILER = GNU
include gar/category.mk
