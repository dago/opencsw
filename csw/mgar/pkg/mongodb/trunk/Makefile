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

LICENSE = APACHE-2.0.txt

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = mongo
INSTALL_SCRIPTS = mongo
TEST_SCRIPTS =

GARCOMPILER = GNU

PATCHFILES += 0002-library-checking-by-locating-.so-files.patch
PATCHFILES += 0003-Hardcode-OpenCSW-specifics-in-the-Solaris-section.patch
PATCHFILES += 0004-Try-Boost-libs-without-the-mt-suffix-first.patch

# Depends on V8 which is available on Solaris 10 x86 only.
# Can only run on little-endian machines.
PACKAGING_PLATFORMS = solaris10-i386

EXTRA_RUNPATH_DIRS = $(prefix)/gxx/lib

BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWgcc4g++
BUILD_DEP_PKGS += CSWlibjs-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibpcre-gxx-dev
BUILD_DEP_PKGS += CSWscons
BUILD_DEP_PKGS += CSWsnappy-gxx-dev

SCONS_FLAGS += --libpath=$(prefix)/gxx/lib
SCONS_FLAGS += --extrapath=$(prefix)/gxx,$(prefix)
SCONS_FLAGS += --cxx=$(CXX)
SCONS_FLAGS += --use-system-all
SCONS_FLAGS += --extralib=rt,pcre
SCONS_FLAGS += --release all

SCONS_ENV = LIBPATH=$(prefix)/gxx/lib

RUNTIME_DEP_PKGS_CSWmongodb += CSWlibboost-filesystem1-49-0-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibboost-thread1-49-0-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibjs1-7-0
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibpcre1-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibpcrecpp0-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibsnappy1-gxx
RUNTIME_DEP_PKGS_CSWmongodb += CSWlibstdc++6

PRESERVECONF = $(sysconfdir)/mongodb.conf

PROTOTYPE_MODIFIERS = datadir
PROTOTYPE_FILES_datadir = $(localstatedir)/mongodb
PROTOTYPE_PERMS_datadir = 0700
PROTOTYPE_USER_datadir = mongo
PROTOTYPE_CLASS_datadir = ugfiles

USERGROUP = $(sysconfdir)/pkg/CSW$(NAME)/cswusergroup

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
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)
	ginstall -m 644 $(FILEDIR)/mongodb.conf $(DESTDIR)$(sysconfdir)/mongodb.conf
	ginstall -m 700 -d $(DESTDIR)$(localstatedir)/mongodb
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(DESTDIR)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/mongodb.xml \
		        $(DESTDIR)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 644 $(FILEDIR)/mongodb-smf-cas-trigger \
		$(DESTDIR)$(sysconfdir)/init.d/mongodb
	@$(MAKECOOKIE)
