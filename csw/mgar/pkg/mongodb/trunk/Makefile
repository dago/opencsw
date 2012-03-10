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
CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER = GNU

# PATCHFILES += 0001-Disabling-the-libstdc-check.patch
PATCHFILES += 0002-library-checking-by-locating-.so-files.patch

# Depends on V8 which is available on Solaris 10 x86 only.
# Can only run on little-endian machines.
PACKAGING_PLATFORMS = solaris10-i386

# scons libboost-dev libpcre++-dev xulrunner-1.9.1-dev

BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWgcc4g++
BUILD_DEP_PKGS += CSWlibmozjs185-gxx-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWscons

include gar/category.mk

build-mongo:
	(cd $(WORKSRC); LIBPATH=/opt/csw/gxx/lib \
		scons \
		--extrapath=/opt/csw,/opt/csw/gxx \
		--cxx=/opt/csw/bin/g++ \
		--release all)
	@$(MAKECOOKIE)

install-mongo:
	(cd $(WORKSRC); $(INSTALL_ENV) scons -Q --prefix=$(DESTDIR)/opt/csw install)
	@$(MAKECOOKIE)
