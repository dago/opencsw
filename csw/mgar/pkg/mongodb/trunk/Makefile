# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mongodb
VERSION = 1.6.3

# http://fastdl.mongodb.org/src/mongodb-src-r1.6.3.tar.gz
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = A scalable, high-performance, open source, document-oriented database
define BLURB
endef
SPKG_SOURCEURL = http://www.mongodb.org/
MASTER_SITES = http://fastdl.mongodb.org/src/
DISTNAME = $(NAME)-src-r$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = mongo
INSTALL_SCRIPTS = mongo
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
# GARCOMPILER = GNU
PATCHFILES += 0001-Disabling-the-libstdc-check.patch
PATCHFILES += 0002-library-checking-by-locating-.so-files.patch

BUILD_DEP_PKGS = CSWboostdevel

# Depends on V8 which is available on Solaris 10 x86 only.
PACKAGING_PLATFORMS = solaris10-i386

include gar/category.mk

# scons libboost-dev libpcre++-dev xulrunner-1.9.1-dev

build-mongo:
	# (cd $(WORKSRC); $(BUILD_ENV) scons --extrapathdyn=/opt/csw,/opt/csw/gcc4 --cxx /opt/csw/gcc4/bin/g++ --usev8 all)
	(cd $(WORKSRC); $(BUILD_ENV) scons --libpath=/opt/csw/lib --extrapathdyn=/opt/csw,/opt/SUNWspro/bin --cxx /opt/SUNWspro/bin/CC --release all)
	@$(MAKECOOKIE)

install-mongo:
	(cd $(WORKSRC); $(INSTALL_ENV) scons -Q --prefix=$(DESTDIR)/opt/csw install)
	@$(MAKECOOKIE)
