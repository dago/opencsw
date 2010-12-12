# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = v8
VERSION = 2.5.1
# VERSION = bleeding_edge
CATEGORIES = lib
define BLURB
Google's open source JavaScript engine
endef
SPKG_SOURCEURL = http://code.google.com/p/$(NAME)/

MASTER_SITES = svn-http//$(NAME).googlecode.com/svn/branches/
DISTFILES  = bleeding_edge
NOCHECKSUM = bleeding_edge
DISTNAME = bleeding_edge
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWscons
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(NAME)
INSTALL_SCRIPTS = $(NAME)
TEST_SCRIPTS =
GARCOMPILER = GNU
SONAME_V = 2.5.1

PACKAGING_PLATFORMS = solaris10-i386

PACKAGES += CSWlib$(NAME)-2-5-1
PACKAGES += CSWlib$(NAME)-devel
CATALOGNAME_CSWlib$(NAME)-2-5-1 = lib$(NAME)_2_5_1
CATALOGNAME_CSWlib$(NAME)-devel = lib$(NAME)_devel

PKGFILES_CSWlib$(NAME)-devel += $(includedir).*
PKGFILES_CSWlib$(NAME)-devel += $(libdir)(/[^/]+)?/lib$(NAME)\.so

SPKG_DESC_CSWlib$(NAME)-2-5-1 = Google\'s open source JavaScript engine
SPKG_DESC_CSWlib$(NAME)-devel = Header files for V8

RUNTIME_DEP_PKGS_CSWlib$(NAME)-2-5-1 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlib$(NAME)-2-5-1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlib$(NAME)-devel += CSWlib$(NAME)-2-5-1
CHECKPKG_OVERRIDES_CSWlib$(NAME)-devel += surplus-dependency|CSWlib$(NAME)-2-5-1

# 64-bit support via a special scons option; passing CFLAGS and CXXFLAGS does
# not work here.
SCONS_ARCH_isa-amd64 = arch=x64
SCONS_ARCH += $(SCONS_ARCH_$(MODULATION))

LICENSE = LICENSE

BUILD64 = 1

include gar/category.mk

build-$(NAME):
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

install-$(NAME):
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/lib$(NAME)-$(SONAME_V).so $(DESTDIR)$(libdir)
	ln -sf lib$(NAME)-$(SONAME_V).so $(DESTDIR)$(libdir)/lib$(NAME).so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in $(WORKSRC)/include/*.h; do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	tree $(DESTDIR)
	@$(MAKECOOKIE)
