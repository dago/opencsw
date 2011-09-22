# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = sbcl
VERSION = 1.0.23
CATEGORIES = apps
DESCRIPTION = High performance Common Lisp compiler
define BLURB
	Steel Bank Common Lisp (SBCL) is a high performance Common Lisp compiler. It
	is open source / free software, with a permissive license. In addition to
	the compiler and runtime system for ANSI Common Lisp, it provides an
	interactive environment including a debugger, a statistical profiler, a code
	coverage tool, and many other extensions.
endef
VENDOR_URL =
MASTER_SITES = $(SF_MIRRORS)
CHECKPKG_OVERRIDES_CSWsbcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/sbcl.1
CHECKPKG_OVERRIDES_CSWsbcl += file-with-bad-content|/usr/local|root/opt/csw/bin/sbcl
DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = sbcl
INSTALL_SCRIPTS = sbcl
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk

build-sbcl:
	(cd $(WORKSRC) && INSTALL_ROOT=$(DESTDIR)$(prefix) /opt/csw/bin/bash make.sh)

install-sbcl:
	(cd $(WORKSRC) && INSTALL_ROOT=$(DESTDIR)$(prefix) /opt/csw/bin/bash install.sh)
	@$(MAKECOOKIE)
