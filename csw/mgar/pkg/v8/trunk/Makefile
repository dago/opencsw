# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = v8
GARVERSION = bleeding_edge
CATEGORIES = lib
DESCRIPTION = Google\'s open source JavaScript engine
define BLURB
endef
SPKG_SOURCEURL = http://code.google.com/p/v8/

MASTER_SITES = svn-http://v8.googlecode.com/svn/branches/
# svn checkout http://v8.googlecode.com/svn/branches/bleeding_edge/ v8
PATCHFILES += 0001-uninitialized-member-v8-internal-Sampler-synchronous.patch
DISTFILES  = $(GARVERSION)
NOCHECKSUM = $(GARVERSION)
# $(GARNAME)-$(GARVERSION).tar.gz
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWscons
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = v8
INSTALL_SCRIPTS = v8
TEST_SCRIPTS =
GARCOMPILER = GNU

include gar/category.mk

build-v8:
	(cd $(WORKSRC); mkdir -p build-solaris; \
		 CC=/opt/csw/gcc4/bin/gcc \
		 CXX=/opt/csw/gcc4/bin/g++ \
		 RANLIB=/opt/csw/gcc4/bin/ranlib \
		 LD=/opt/csw/bin/gld \
		 AR=/opt/csw/bin/gar \
		 SHCXX=/opt/csw/gcc4/bin/g++ \
		 LINKFLAGS='-R/opt/csw/gcc4/lib' \
		 scons -Y .. \
		 visibility=default library=shared toolchain=gcc soname=on -j3)
	@$(MAKECOOKIE)

install-v8:
	false
