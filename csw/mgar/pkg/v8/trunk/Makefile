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
# PATCHFILES += 0001-uninitialized-member-v8-internal-Sampler-synchronous.patch
DISTFILES  = $(GARVERSION)
NOCHECKSUM = $(GARVERSION)
DISTNAME = $(GARVERSION)
# $(GARNAME)-$(GARVERSION).tar.gz
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWscons
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = v8
INSTALL_SCRIPTS = v8
TEST_SCRIPTS =
GARCOMPILER = GNU
SONAME_V = 2.5.1

PACKAGING_PLATFORMS = solaris10-i386

PACKAGES += CSWlibv8-2-5-1
PACKAGES += CSWlibv8-devel
CATALOGNAME_CSWlibv8-2-5-1 = libv8_2_5_1
CATALOGNAME_CSWlibv8-devel = libv8_devel

PKGFILES_CSWlibv8-devel = $(includedir).*
PKGFILES_CSWlibv8-devel = $(libdir)/libv8\.so

SPKG_DESC_CSWlibv8-2-5-1 = Google\'s open source JavaScript engine
SPKG_DESC_CSWlibv8-devel = Header files for V8

RUNTIME_DEP_PKGS_CSWlibv8-2-5-1 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibv8-2-5-1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibv8-devel += CSWlibv8-2-5-1
CHECKPKG_OVERRIDES_CSWlibv8-devel += surplus-dependency|CSWlibv8-2-5-1

LICENSE = LICENSE

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
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/libv8-$(SONAME_V).so $(DESTDIR)$(libdir)
	ln -sf libv8-$(SONAME_V).so $(DESTDIR)$(libdir)/libv8.so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in $(WORKSRC)/include/*.h; do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	tree $(DESTDIR)
	@$(MAKECOOKIE)
