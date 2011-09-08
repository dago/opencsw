# $Id$
# 
# ! The library builds, but there are two failing tests.
# - http://www.cs.unipr.it/pipermail/ppl-devel/2011-August/017604.html
#
# The problem could be GCC Bug 40024 which seems to be affecting our released
# version of the compiler.
# 
# http://lists.opencsw.org/pipermail/users/2011-May/008908.html
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=40024
#
# One way to fix this, would be to build a newer version of the 4.3 line, e.g.
# 4.3.6 and see what happens.

NAME = ppl
VERSION = 0.11.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Parma Polyhedra Library
define BLURB
endef

# The tests are mostly passing on sparc, but the compilation of tests fails on
# amd64 with a cryptic error message.
# http://www.cs.unipr.it/pipermail/ppl-devel/2011-August/017618.html
SKIPTEST ?= 1

BUILD_DEP_PKGS = CSWlibgmp-dev
BUILD_DEP_PKGS += CSWlibmpfr-dev
BUILD_DEP_PKGS += CSWlibmpc-dev
BUILD_DEP_PKGS += CSWgm4

MASTER_SITES = http://www.cs.unipr.it/ppl/Download/ftp/releases/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-R1-is-defined-in-usr-include-ia32-sys-reg.h-disturbi.patch
PATCHFILES += 0002-Make-call-to-version-explicit-to-avoid-clash-with-ma.patch
PATCHFILES += 0003-Remove-a-const-arg-declaration.patch

VENDOR_URL = http://www.cs.unipr.it/ppl/

# C++ bindings require the consistency between GMP, PPL and GCC.
GARCOMPILER = GNU

BUILD64 = 1

# Undefined symbol __sync_fetch_and_add_4
# http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
# http://opencsw.wikidot.com/porting-faq#toc6
ifeq ($(ISA),sparcv8)
OPT_FLAGS_GCC = -O0
endif
ifeq ($(ISA),i386)
OPT_FLAGS_GCC = -O0
endif

# http://wiki.opencsw.org/porting-faq#toc13
RUNTIME_DEP_PKGS = $(RUNTIME_DEP_PKGS_$(GAROSREL))
RUNTIME_DEP_PKGS_5.9 = CSWlibgnugetopt
EXTRA_LDFLAGS = $(EXTRA_LDFLAGS_$(GAROSREL))
EXTRA_LDFLAGS_5.9 = -lgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibppl-dev
SPKG_DESC_CSWlibppl-dev = $(DESCRIPTION), development files
# catch-all package
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibgmpxx4
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibppl-c4
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibppl9
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibpwl5
RUNTIME_DEP_PKGS_CSWlibppl-dev += CSWlibstdc++6
CHECKPKG_OVERRIDES_CSWlibppl-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/ppl/README.doc
CHECKPKG_OVERRIDES_CSWlibppl-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/pwl/README.doc

PACKAGES += CSWlibppl9
CATALOGNAME_CSWlibppl9 = libppl9
PKGFILES_CSWlibppl9 += $(call baseisadirs,$(libdir),libppl\.so\.9\.0\.0)
PKGFILES_CSWlibppl9 += $(call baseisadirs,$(libdir),libppl\.so\.9(\.\d+)*)
SPKG_DESC_CSWlibppl9 += $(DESCRIPTION), libppl.so.9
RUNTIME_DEP_PKGS_CSWlibppl9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibppl9 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibppl9 += CSWlibgmpxx4
RUNTIME_DEP_PKGS_CSWlibppl9 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibppl9 += CSWlibstdc++6


PACKAGES += CSWlibppl-c4
CATALOGNAME_CSWlibppl-c4 = libppl_c4
PKGFILES_CSWlibppl-c4 += $(call baseisadirs,$(libdir),libppl_c\.so\.4\.0\.0)
PKGFILES_CSWlibppl-c4 += $(call baseisadirs,$(libdir),libppl_c\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibppl-c4 += $(DESCRIPTION), libppl_c.so.4
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibgmpxx4
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibppl9
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibpwl5
RUNTIME_DEP_PKGS_CSWlibppl-c4 += CSWlibstdc++6

PACKAGES += CSWlibpwl5
CATALOGNAME_CSWlibpwl5 = libpwl5
PKGFILES_CSWlibpwl5 += $(call baseisadirs,$(libdir),libpwl\.so\.5\.0\.0)
PKGFILES_CSWlibpwl5 += $(call baseisadirs,$(libdir),libpwl\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibpwl5 += $(DESCRIPTION), libpwl.so.5
RUNTIME_DEP_PKGS_CSWlibpwl5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpwl5 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibpwl5 += CSWlibstdc++6

include gar/category.mk

# To help the configure script find GNU M4
PATH := /opt/csw/gnu:$(PATH)
