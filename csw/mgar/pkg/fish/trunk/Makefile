# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fish
VERSION = 2.1.0
GARTYPE = v2

GARCOMPILER = GNU

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://fishshell.com/files/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0002-Patch-for-dirfd-on-Solaris-10.patch
PATCHFILES += 0003-LinuxSoft-patch-1.patch
PATCHFILES += 0004-LinuxSoft-patch-2.patch
PATCHFILES += 0005-Include-strings.h-to-make-bzero-available.patch
PATCHFILES += 0006-Include-strings.h-to-make-bzero-available-2.patch

EXTRA_CPPFLAGS = -I$(includedir)/ncurses

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

CONFIGURE_ARGS = $(DIRPATHS)

REINPLACE_MATCH = \#!/bin/sh
REINPLACE_WITH = \#!/bin/bash
REINPLACE_FILES = build_tools/git_version_gen.sh

include gar/category.mk

PATH := $(prefix)/gnu:$(PATH)

pre-configure:
	cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)
