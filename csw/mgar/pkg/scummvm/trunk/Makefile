NAME = scummvm
VERSION = 1.4.0
CATEGORIES = apps

DESCRIPTION = Virtual machine for several classic graphical point-and-click adventure games
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

RUNTIME_DEP_PKGS_CSWscummvm += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibz1
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibogg0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibflac8
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibmad0
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWscummvm += CSWlibvorbisfile3

# Don't know about these, investigate later
CHECKPKG_OVERRIDES_CSWscummvm += file-with-bad-content|/usr/local|root/opt/csw/bin/scummvm
CHECKPKG_OVERRIDES_CSWscummvm += file-with-bad-content|/usr/local|root/opt/csw/share/man/man6/scummvm.6

GARCOMPILER = GCC4

# Custom configure
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --enable-all-engines

TEST_TARGET = test

# Testsuite relies on Python which throws lots of errors, disable for now
SKIPTEST ?= 1

include gar/category.mk

# For "install" with GNU syntax
PATH := /opt/csw/gnu:$(PATH)
