# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = yajl
VERSION = 2.1.0
GARTYPE = v2

DESCRIPTION = Yet Another JSON Library

MASTER_SITES = http://github.com/lloyd/yajl/tarball/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

DISTNAME = lloyd-yajl-66cb08c

GARCOMPILER = GNU

REINPLACEMENTS += bash
REINPLACE_MATCH_bash = /bin/sh
REINPLACE_WITH_bash = /bin/bash
REINPLACE_FILES_bash += test/parsing/run_tests.sh

PACKAGES += CSWlibyajl2
SPKG_DESC_CSWlibyajl2 = Yet Another JSON Library, libyajl.so.2
PKGFILES_CSWlibyajl2 += $(call pkgfiles_lib,libyajl.so.2)
RUNTIME_DEP_PKGS_CSWlibyajl2 += CSWlibgcc-s1

PACKAGES += CSWlibyajl-dev
SPKG_DESC_CSWlibyajl-dev = Development files for libyajl.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibyajl-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibyajl-dev += CSWlibyajl2

# CMake installs the 64 bit executables and libraries to /opt/csw/lib instead of /opt/csw/lib/64
# The next two lines take care that the files are taken from the correct directory.
bindir = $(bindir_install)
libdir = $(libdir_install)

BUILD64 = 1
ISAEXEC = 1
CONFIGURE_ARGS += -p $(prefix)

BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)

# This is already done during build
TEST_SCRIPTS =

include gar/category.mk

post-install-isa-sparcv8plus post-install-isa-pentium_pro:
	mv $(DESTDIR)$(sharedstatedir)/pkgconfig $(DESTDIR)$(libdir)
	rmdir $(DESTDIR)$(sharedstatedir)
	@$(MAKECOOKIE)

post-install-isa-sparcv9 post-install-isa-amd64:
	mv $(DESTDIR)$(sharedstatedir)/pkgconfig $(DESTDIR)$(libdir)
	rmdir $(DESTDIR)$(sharedstatedir)
	perl -i -npe 's!/lib!/lib/64!' $(DESTDIR)$(libdir)/pkgconfig/yajl.pc
	@$(MAKECOOKIE)

