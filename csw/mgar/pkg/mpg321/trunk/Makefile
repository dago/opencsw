# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mpg321
VERSION = 0.2.13_2
CATEGORIES = apps

DESCRIPTION = A Free, fast fixed-point math replacement for mpg123

define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)-$(subst _,-,$(VERSION))
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://mpg321.sourceforge.net/

RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibao4
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibmad0
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWmpg321 += CSWzlib
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibgnugetopt

BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibmad-dev
BUILD_DEP_PKGS += CSWlibid3tag
BUILD_DEP_PKGS += CSWzlib
BUILD_DEP_PKGS += CSWlibgnugetopt

# We don't have round on Solaris 9
EXTRA_CPPFLAGS = -Dround=floor

EXTRA_LINKER_FLAGS += -lrt
EXTRA_LINKER_FLAGS += -lgnugetopt

ALTERNATIVES = mpg321
ALTERNATIVE_mpg321 = $(bindir)/mpg123 mpg123 $(bindir)/mpg321 50

# Checkpkg can't check this
CHECKPKG_OVERRIDES_CSWmpg321 += surplus-dependency|CSWalternatives

# Location explicitly stated for Debian
CHECKPKG_OVERRIDES_CSWmpg321 += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/mpg321.1

include gar/category.mk

post-merge:
	rm $(PKGROOT)$(bindir)/mpg123
	@$(MAKECOOKIE)
