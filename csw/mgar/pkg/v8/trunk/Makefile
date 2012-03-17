# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = v8
VERSION = 0.2012.03
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
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(NAME)
INSTALL_SCRIPTS = $(NAME)
TEST_SCRIPTS =
GARCOMPILER = GNU
SONAME_V = $(VERSION)

NOGITPATCH = 1

PACKAGING_PLATFORMS = solaris10-i386

LICENSE = LICENSE

# The V8 build system thinks we are on a 32-bit host and disallows a 64-bit
# build.
# BUILD64 = 1

PATCHFILES += 0001-Link-with-librt-on-Solaris-by-default.patch
PATCHFILES += 0002-Comment-out-unused-variables.patch
PATCHFILES += 0003-Cast-to-wint_t-which-is-what-lc-expects.patch

SCONS_ENV += CC=/opt/csw/bin/gcc
SCONS_ENV += CXX=/opt/csw/bin/g++
SCONS_ENV += RANLIB=/opt/csw/bin/ranlib
SCONS_ENV += LD=/opt/csw/bin/gld
SCONS_ENV += AR=/opt/csw/bin/gar
SCONS_ENV += SHCXX=/opt/csw/bin/g++
SCONS_ENV += LINKFLAGS=-R/opt/csw/lib

LINK = $(CXX)
LD_ALTEXEC = /opt/csw/bin/gld
EXTRA_BUILD_EXPORTS = LINK LD_ALTEXEC

BUILD_OPTS += visibility=default
BUILD_OPTS += library=shared
BUILD_OPTS += toolchain=gcc
BUILD_OPTS += soname=on
BUILD_OPTS += soname_version=$(VERSION)

GYPFLAGS = -D OS=solaris

OBJDIR = $(abspath $(WORKDIR)/objdir)

# 64-bit support via a special option; passing CFLAGS and CXXFLAGS does
# not work here.
# It would be better to use MEMORY_MODEL or something similar from GAR.
V8_TARGET_isa-pentium_pro = ia32
V8_TARGET_isa-amd64 = x64
V8_TARGET = $(V8_TARGET_$(MODULATION))

PACKAGES += CSWlibv8-dev
SPKG_DESC_CSWlibv8-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibv8-dev += CSWlibv8-0-2012-03

PACKAGES += CSWlibv8-0-2012-03
PKGFILES_CSWlibv8-0-2012-03 += $(call baseisadirs,$(libdir),libv8\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibv8-0-2012-03 += $(DESCRIPTION), the shared library
RUNTIME_DEP_PKGS_CSWlibv8-0-2012-03 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibv8-0-2012-03 += CSWlibstdc++6

include gar/category.mk

post-extract-modulated:
	(cd $(WORKSRC); \
	  gmake dependencies; \
	  cd build/gyp; \
	  svn update; \
	)
	@$(MAKECOOKIE)

build-$(NAME):
	(cd $(WORKSRC); \
	  $(BUILD_ENV) \
	  gmake \
	  $(PARALLELMFLAGS) \
	  $(BUILD_OPTS) \
	  $(V8_TARGET).release; \
	)
	@$(MAKECOOKIE)

install-$(NAME):
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	# ginstall -m 755 $(WORKSRC)/build-solaris/lib$(NAME)-$(SONAME_V).so $(DESTDIR)$(libdir)
	ginstall -m 755 \
	  $(WORKSRC)/out/$(V8_TARGET).release/obj.target/tools/gyp/lib$(NAME).so.$(SONAME_V) \
	  $(DESTDIR)$(libdir)
	ln -sf lib$(NAME).so.$(SONAME_V) $(DESTDIR)$(libdir)/lib$(NAME).so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in $(WORKSRC)/include/*.h; do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	tree $(DESTDIR)
	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:$(PATH)
