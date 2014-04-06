# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = sbcl
VERSION = 1.0.23
# VERSION = 1.1.7
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = High performance Common Lisp compiler
define BLURB
	Steel Bank Common Lisp (SBCL) is a high performance Common Lisp compiler. It
	is open source / free software, with a permissive license. In addition to
	the compiler and runtime system for ANSI Common Lisp, it provides an
	interactive environment including a debugger, a statistical profiler, a code
	coverage tool, and many other extensions.
 http://www.sbcl.org/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparcON)-source.tar.bz2
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = sbcl
INSTALL_SCRIPTS = sbcl
TEST_SCRIPTS =
CONFIGURE_Ae/man/man1/sbcl.1
CHECKPKG_OVERRIDES_CSWsbcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/sbcl.1
CHECKPKG_OVERRIDES_CSWsbcl += file-with-bad-content|/usr/local|root
NOGITPATCH = 1

GARCOMPILER = GNU

include gar/category.mk

post-extract:
	gfind "$(WORKSRC)" -name '*.sh' -exec gsed -e 's+#!/bin/sh+#!/opt/csw/bin/bash+' -i {} \;
	@$(MAKECOOKIE)

build-sbcl:
	(cd $(WORKSRC) && env -i INSTALL_ROOT=$(DESTDIR)$(prefix) $(BUILD_ENV) /opt/csw/bin/bash make.sh)

install-sbcl:
	(cd $(WORKSRC) && env -i INSTALL_ROOT=$(DESTDIR)$(prefix) $(INSTALL_ENV) /opt/csw/bin/bash install.sh)
	@$(MAKECOOKIE)

PATH := /usr/xpg4/bin:$(PATH)
