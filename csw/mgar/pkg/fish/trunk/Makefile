# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fish
VERSION = 2.1.0
GARTYPE = v2

GARCOMPILER = GNU

DESCRIPTION = smart and user-friendly command line shell
define BLURB
 fish is a smart and user-friendly command line
 shell for OS X, Linux, and the rest of the family.
endef

MASTER_SITES = http://fishshell.com/files/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

ETCSHELLS = $(bindir)/fish

PATCHFILES += 0002-Patch-for-dirfd-on-Solaris-10.patch
PATCHFILES += 0003-LinuxSoft-patch-1.patch
PATCHFILES += 0004-LinuxSoft-patch-2.patch
PATCHFILES += 0005-Include-strings.h-to-make-bzero-available.patch
PATCHFILES += 0006-Include-strings.h-to-make-bzero-available-2.patch
PATCHFILES += 0007-Add-opt-csw-where-deemed-neccessary.patch

RUNTIME_DEP_PKGS_CSWfish += CSWlibintl8
RUNTIME_DEP_PKGS_CSWfish += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWfish += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWfish += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfish += CSWlibncurses5

# That's fine, directory list has been adjusted to include /opt/csw/share
CHECKPKG_OVERRIDES_CSWfish += file-with-bad-content|/usr/local|root/opt/csw/bin/mimedb
CHECKPKG_OVERRIDES_CSWfish += file-with-bad-content|/usr/share|root/opt/csw/bin/mimedb

EXTRA_CPPFLAGS = -I$(includedir)/ncurses
# Ain't pulled in automatically...
EXTRA_LINKER_FLAGS = -lintl -liconv

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

CONFIGURE_ARGS = $(DIRPATHS)

REINPLACE_MATCH = \#!/bin/sh
REINPLACE_WITH = \#!/bin/bash
REINPLACE_FILES = build_tools/git_version_gen.sh

TEST_SCRIPTS = custom

include gar/category.mk

PATH := $(prefix)/gnu:$(PATH)

pre-configure:
	cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)

test-custom:
	cd $(WORKSRC) && env $(BUILD_ENV) $(MAKE) test
	@$(MAKECOOKIE)
