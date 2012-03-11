# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mongodb
VERSION = 2.0.3

CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = A scalable, high-performance, open source, document-oriented database
define BLURB
endef
SPKG_SOURCEURL = http://www.mongodb.org/
MASTER_SITES = http://fastdl.mongodb.org/src/
DISTNAME = $(NAME)-src-r$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = mongo
INSTALL_SCRIPTS = mongo
TEST_SCRIPTS =

GARCOMPILER = GNU

# PATCHFILES += 0001-Disabling-the-libstdc-check.patch
PATCHFILES += 0002-library-checking-by-locating-.so-files.patch

# Depends on V8 which is available on Solaris 10 x86 only.
# Can only run on little-endian machines.
PACKAGING_PLATFORMS = solaris10-i386

# scons libboost-dev libpcre++-dev xulrunner-1.9.1-dev

BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWgcc4g++
# BUILD_DEP_PKGS += CSWlibmozjs185-gxx-dev
BUILD_DEP_PKGS += CSWlibjs-gxx-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibpcre-gxx-dev
BUILD_DEP_PKGS += CSWscons
BUILD_DEP_PKGS += CSWsnappy-gxx-dev

SCONS_FLAGS += --libpath=$(libdir)
SCONS_FLAGS += --extrapath=$(BUILD_PREFIX),$(prefix)
SCONS_FLAGS += --cxx=$(BUILD_PREFIX)/bin/g++
SCONS_FLAGS += --use-system-all
SCONS_FLAGS += --extralib=rt,pcre
SCONS_FLAGS += --release all

SCONS_ENV = LIBPATH=$(libdir)

include gar/category.mk

build-mongo:
	(cd $(WORKSRC); \
		$(SCONS_ENV) \
		scons \
		$(SCONS_FLAGS))
	@$(MAKECOOKIE)

install-mongo:
	(cd $(WORKSRC); \
		$(SCONS_ENV) \
		scons  \
		$(SCONS_FLAGS) \
		-Q --prefix=$(DESTDIR)$(BUILD_PREFIX) \
		install)
	@$(MAKECOOKIE)
