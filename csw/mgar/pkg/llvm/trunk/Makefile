# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = llvm
VERSION = 3.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Collection of modular and reusable compiler and toolchain technologies
define BLURB
  Long description
endef

MASTER_SITES = http://llvm.org/releases/$(VERS = llvm-$(VERSION).tar.gz
DISTFILES  += clang-$(VERSION).tar.gz

DISTNAME = llvm-$(VERSION).src

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

NOGITPATCH = 1M_MASTER_SITES = 

GARCOMPILER = GNU

libdir = $(prefix)/lib/llvm

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-optimized
# ocaml causes a compilation failure
# http://lists.cs.uiuc.edu/pipermail/llvmbugs/2010-December/015967.html
# http://lists.cs.uiuc.edu/pipermail/llvmbugs/2010-December/015968.html
CONFIGURE_ARGS += --enable-bindings=none
# CONFIGURE_ARGS +=CONFIGURE_ARGS += --enable-shared
# CONFIGURE_ARGS += --with-llvmgcc
# CONFIGURE_ARGS += --with-llvmgxx
# CONFIGURE_ARGS += --with-clang= --enable-libffi

PATCHFILES += 0001-limits.h-used-for-MAX_PATH.patch
PATCHFILES += 0002-OpenCSW-bash-for-tests.patch
PATCHFILES += 0003-OpenCSW-bash-with-the-Python-test-runner.patch
PATCHFILES += 0004-test-runner-adaptation-to-Solaris.patch

RUNTIME_DEP_PKGS_CSWllvm += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWllvm += CSWgcc4corert

ENABLE_OPTIMIZED = 1
OPTIMopt/csw/bin/bash
CONFIG_SHELL = /opt/csw/bin/bash
EXTRA_CONFIGURE_EXPORTS  = ENABLE_OPTIMIZED
EXTRA_CONFIGURE_EXPORTS += OPTIMIZE_OPTION
EXTRA_CONFIGURE_EXPORTS += CONFIG_SHELL
EXTRA_BUILD_EXPORTS  = ENABLE_OPTIMIZED
EXTRA_BUILD_EXPORTS +=# SHELL = /opt/csw/bin/bash
#  OPTIMIZE_OPTION
EXTRA_TEST_EXPORTS = SHELL

NM = /opt/csw/bin/gnm
EXTRA_CONFIGURE_EXPORTS += NM
EXTRA_BUILD_EXPORTS += NM

VERBOSE = 1
EXTRA_CONFIGURE_EXPORTS  = VERBOSE
EXTRA_BUILD_EXPORTS  = VERBOSE

include gar/category.mk

# To help the configure script find /opt/csw/gnu/nm
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

# ARCHFLAGS_GCC4_sparcv8 = -m32

# Undefined symbol __sync_fetch_and_add_4
# http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
# http://opencsw.wikidot.com/porting-faq#toc6
# ifeq # ($(ISA),sparcv8)
OPT_FLAGS_GCC = -O0
# endif
# ifeq ($(ISA),i386)
# OPT_FLAG# pre-configure-modulated:
# 	(cd $(WORKSRC)/tools && gln -s -v ../../clang-$(VERSION) clang)
# 	@$(MAKECOOKIE)

pre-configure-modulated:
	(cd $(WORKSRC)/tools; gln -v -s ../../clang-$(VERSION).src clang)
	# $(FILEDIR)/gar_helper.sh $@ "$(WORKSRC)"
	@$(MAKECOOKIE)
