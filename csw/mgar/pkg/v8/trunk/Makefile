# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = v8
VERSION = 3.6.0
DASH_VERSION = 3-6-0
UNDER_VERSION = 3_6_0
# VERSION = bleeding_edge
DESCRIPTION = Open source JavaScript engine from Google
CATEGORIES = lib
GARTYPE = v2
define BLURB
Google's open source JavaScript engine
endef
VENDOR_URL = http://code.google.com/p/$(NAME)/

MASTER_SITES = svn-http//$(NAME).googlecode.com/svn/branches/
DISTFILES  = bleeding_edge
NOCHECKSUM = bleeding_edge
DISTNAME = bleeding_edge
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWscons
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(NAME)
INSTALL_SCRIPTS = $(NAME)
TEST_SCRIPTS = $(NAME)
GARCOMPILER = GNU
SONAME_V = $(VERSION)

PACKAGING_PLATFORMS = solaris10-i386

PACKAGES += CSWlibv8-3-6-0
CATALOGNAME_CSWlibv8-3-6-0 = libv8_3_6_0
PKGFILES_CSWlibv8-3-6-0 += $(call baseisadirs,$(libdir),libv8-3\.6\.0\.so)
PKGFILES_CSWlibv8-3-6-0 += $(call baseisadirs,$(libdir),libv8-3\.6\.0\.so(\.\d+)*)
SPKG_DESC_CSWlibv8-3-6-0 += $(DESCRIPTION), libv8-3.6.0.so

PACKAGES += CSWlibv8-dev
SPKG_DESC_CSWlibv8-dev += $(DESCRIPTION), development files

# 64-bit support via a special scons option; passing CFLAGS and CXXFLAGS does
# not work here.
SCONS_ARCH_isa-amd64 = arch=x64
SCONS_ARCH += $(SCONS_ARCH_$(MODULATION))

LICENSE = LICENSE

BUILD64 = 1

SCONS_ENV += CC=/opt/csw/gcc4/bin/gcc
SCONS_ENV += CXX=/opt/csw/gcc4/bin/g++
SCONS_ENV += RANLIB=/opt/csw/gcc4/bin/ranlib
SCONS_ENV += LD=/opt/csw/bin/gld
SCONS_ENV += AR=/opt/csw/bin/gar
SCONS_ENV += SHCXX=/opt/csw/gcc4/bin/g++
SCONS_ENV += LINKFLAGS=-R/opt/csw/gcc4/lib

SCONS_OPTS = visibility=default library=shared toolchain=gcc soname=on

include gar/category.mk

build-$(NAME):
	(cd $(WORKSRC); mkdir -p build-solaris; \
		cd build-solaris; \
		$(SCONS_ENV) \
		\
		scons \
		-Y .. \
		$(SCONS_ARCH) \
		$(SCONS_OPTS) \
		-j3 \
		)
	@$(MAKECOOKIE)

install-$(NAME):
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/build-solaris/lib$(NAME)-$(SONAME_V).so $(DESTDIR)$(libdir)
	ln -sf lib$(NAME)-$(SONAME_V).so $(DESTDIR)$(libdir)/lib$(NAME).so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in $(WORKSRC)/include/*.h; do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	tree $(DESTDIR)
	@$(MAKECOOKIE)

test-$(NAME):
	(cd $(WORKSRC)/build-solaris; \
		$(SCONS_ENV) scons -Y .. $(SCONS_OPTS) d8)
	(cd $(WORKSRC)/build-solaris; \
		$(SCONS_ENV) \
		../tools/test.py \
		--shell=d8 \
		-S toolchain=gcc \
		-S library=shared \
		-S soname=on \
		-S visibility=default \
		)
