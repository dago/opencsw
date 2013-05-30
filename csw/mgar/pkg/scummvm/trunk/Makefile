NAME    = scummvm
VERSION = 1.6.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Virtual machine for several classic graphical point-and-click adventure games
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

RUNTIME_DEP_PKGS_CSWscummvm += CSWlibz1
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibogg0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibflac8
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWscummvm += RUNTIME_DEP_PKGS_CSWscummvm += CSWlibfluidsynth1
RUNTIME_DEP_PKGS_CSWscummvm += CSWmesa
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibmad0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibfaad2
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibtheoradec1

BUILD64 = 1
ISAEXEC = 1

BUILD_DEP_PKGS_CSWscummvm += CSWlibsdl-dev
BUILD_DEP_PKGS_CSWscummvm += CSWfluidsynth-dev
BUILD_DEP_PKGS_CSWscummvm += CSWlibmad-dev
BUILD_DEP_PKGS_CSWscummvm += CSWlibfaad-dev
BUILD_DEP_PKGS_CSWscummvm += CSWlibtheora-dev

PATCHFILES += 0001-redefining-FILE.patch
PATCHFILES += 0002-configure-really-is-a-bash-script.patchCan/man6/scummvm.6

GARCOMPILER = GCC4

# Custom configure
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGrootURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURErelease
CONFIGURE_ARGS += --enable-plugins
CONFIGURE_ARGS += --default-dynamic
CONFIGURE_ARGS += --enable-updat--eCONFIGURE_ARGS += --disable-nasmenable-all-engines

TEST_TARGET = test

# Testsuite relies on Python which throws lots of errors, disable for now
SKIPTEST ?= 1

include gar/category.mk

# For "install" with GNU syntax
PATH := /op