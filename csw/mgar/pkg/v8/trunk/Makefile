# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = v8
GARVERSION = 2.5.1
# GARVERSION = bleeding_edge
CATEGORIES = lib
define BLURB
Google's open source JavaScript engine
endef
SPKG_SOURCEURL = http://code.google.com/p/$(GARNAME)/

MASTER_SITES = svn-http//$(GARNAME).googlecode.com/svn/branches/
DISTFILES  = bleeding_edge
NOCHECKSUM = bleeding_edge
DISTNAME = bleeding_edge
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWscons
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(GARNAME)
INSTALL_SCRIPTS = $(GARNAME)
TEST_SCRIPTS =
GARCOMPILER = GNU
SONAME_V = 2.5.1

PACKAGING_PLATFORMS = solaris10-i386

PACKAGES += CSWlib$(GARNAME)-2-5-1
PACKAGES += CSWlib$(GARNAME)-devel
CATALOGNAME_CSWlib$(GARNAME)-2-5-1 = lib$(GARNAME)_2_5_1
CATALOGNAME_CSWlib$(GARNAME)-devel = lib$(GARNAME)_devel

PKGFILES_CSWlib$(GARNAME)-devel += $(includedir).*
PKGFILES_CSWlib$(GARNAME)-devel += $(libdir)(/[^/]+)?/lib$(GARNAME)\.so

SPKG_DESC_CSWlib$(GARNAME)-2-5-1 = Google\'s open source JavaScript engine
SPKG_DESC_CSWlib$(GARNAME)-devel = Header files for V8

RUNTIME_DEP_PKGS_CSWlib$(GARNAME)-2-5-1 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlib$(GARNAME)-2-5-1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlib$(GARNAME)-devel += CSWlib$(GARNAME)-2-5-1
CHECKPKG_OVERRIDES_CSWlib$(GARNAME)-devel += surplus-dependency|CSWlib$(GARNAME)-2-5-1

# 64-bit support via a special scons option; passing CFLAGS and CXXFLAGS does
# not work here.
SCONS_ARCH_isa-amd64 = arch=x64
SCONS_ARCH += $(SCONS_ARCH_$(MODULATION))

LICENSE = LICENSE

BUILD64 = 1

include gar/category.mk

build-$(GARNAME):
	(cd $(WORKSRC); mkdir -p build-solaris; \
		 CC=/opt/csw/gcc4/bin/gcc \
		 CXX=/opt/csw/gcc4/bin/g++ \
		 RANLIB=/opt/csw/gcc4/bin/ranlib \
		 LD=/opt/csw/bin/gld \
		 AR=/opt/csw/bin/gar \
		 SHCXX=/opt/csw/gcc4/bin/g++ \
		 LINKFLAGS='-R/opt/csw/gcc4/lib' \
		 scons -Y .. \
		 $(SCONS_ARCH) \
		 visibility=default library=shared toolchain=gcc soname=on -j3)
	@$(MAKECOOKIE)

install-$(GARNAME):
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/lib$(GARNAME)-$(SONAME_V).so $(DESTDIR)$(libdir)
	ln -sf lib$(GARNAME)-$(SONAME_V).so $(DESTDIR)$(libdir)/lib$(GARNAME).so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in $(WORKSRC)/include/*.h; do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	tree $(DESTDIR)
	@$(MAKECOOKIE)
