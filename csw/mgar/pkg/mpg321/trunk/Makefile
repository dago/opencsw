# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mpg321
VERSION = 0.2.11
DISTFILE_SUFFIX = -2
CATEGORIES = apps

DESCRIPTION = A Free, fast fixed-point math replacement for mpg123
SPKG_SOURCEURL = http://mpg321.sourceforge.net/
define BLURB
endef
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)$(DISTFILE_SUFFIX).tar.gz
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibao
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibmad
RUNTIME_DEP_PKGS_CSWmpg321 += CSWzlib
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS_CSWmpg321)
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
# A fix for an inline function and 'symbol not found'.
EXTRA_CFLAGS = -features=no%extinl

ALTERNATIVES = mpg321

ALTERNATIVE_mpg321 = $(bindir)/mpg123 mpg123 $(bindir)/mpg321 50

include gar/category.mk

post-merge:
	rm $(PKGROOT)$(bindir)/mpg123
	@$(MAKECOOKIE)
