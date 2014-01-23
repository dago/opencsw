# TODO (release-critical prefixed with !, non release-critical with *)
# most stuff from here: https://github.com/joyent/pkgsrc/blob/trunk/lang/clang/Makefile
#
NAME = llvm
VERSION = 3.4
GARTYPE = v2

DESCRIPTION = Clangis a compiler front end for the C, C++, Objective-C and Objective-C++ programming languages
define BLURB
  Clang is a compiler front end for the C, C++, Objective-C and Objective-C++ programming languages.It uses LLVM as its back end.
endef

MASTER_SITES = http://llvm.org/releases/$(VERSION)/
DISTFILES  = llvm-$(VERSION).src.tar.gz
DISTFILES  += clang-$(VERSION).src.tar.gz
PATCHFILES += 0001-use_a_tail_that_works.patch
PATCHFILES += 0002-fix-endiness.patch
PATCHFILES += 0003-fix_Solaris_opencsw_gcc.patch

PACKAGES = CSWclang
CATALOGNAME_CSWclang = clang
SPKG_DESC_CSWclang += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWclang += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWclang += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWclang += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWclang += CSWlibz1
# Kind of bad but it needs crtbegin.o and crtend.o which are in /opt/csw/lib/gcc/*/4.x.x/ with new gcc clang needs to be rebuild because of this.
RUNTIME_DEP_PKGS_CSWclang += CSWgcc4core
CHECKPKG_OVERRIDES_CSWclang += surplus-dependency|CSWgcc4core

CHECKPKG_OVERRIDES_CSWclang += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWclang += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWclang += file-with-bad-content
CHECKPKG_OVERRIDES_CSWclang += no-direct-binding
CHECKPKG_OVERRIDES_CSWclang += soname-equals-filename|file=/opt/csw/lib/BugpointPasses.so
CHECKPKG_OVERRIDES_CSWclang += soname-equals-filename|file=/opt/csw/lib/LLVMHello.so
CHECKPKG_OVERRIDES_CSWclang += soname-equals-filename|file=/opt/csw/lib/libLTO.so
CHECKPKG_OVERRIDES_CSWclang += soname-equals-filename|file=/opt/csw/lib/libclang.so


NOGITPATCH = 1

GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assertions
CONFIGURE_ARGS += --disable-bindings # disable OCaml
CONFIGURE_ARGS += --disable-timestamps
CONFIGURE_ARGS += --enable-optimized
CONFIGURE_ARGS += --with-extra-ld-options="-mimpure-text -lrt"
CONFIGURE_ARGS += --with-gcc-toolchain="/opt/csw/gcc4/bin"
CONFIGURE_ARGS += --with-c-include-dirs="/usr/include:/opt/csw/include"

# Solaris 10 needs a special map file since we need newer libc 
# This sets the minumum Solaris 10 Version to Update 9
#This is do to use of futimens the check is here: http://llvm.org/viewvc/llvm-project?view=revision&revision=185601 the check is there but it checks in the headers but default map file prevents use of it. Needs fix not sure what to set where so it's update 9 for now
        LINKER_MAPS ?= -M "$(abspath $(WORKDIR)/map.clang)"
DISTFILES += map.clang

EXTRA_CFLAGS += -mimpure-text

SKIPTEST = 1
#TEST_TARGET = unittests

include gar/category.mk

post-extract:
	mv $(WORKDIR)/clang-$(VERSION) $(WORKDIR)/llvm-$(VERSION)/tools/clang
	echo "int sun_ld_needs_a_symbol=0;" >> $(WORKSRC)/lib/Target/NVPTX/InstPrinter/NVPTXInstPrinter.cpp
	@$(MAKECOOKIE)
