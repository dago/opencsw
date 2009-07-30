GARNAME = patchutils
GARVERSION = 0.3.1
CATEGORIES = utils

DESCRIPTION = Tools for manipulating patch files
define BLURB
  Patchutils is a small collection of programs that operate on patch files.
endef

MASTER_SITES = http://cyberelk.net/tim/data/patchutils/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWgnulinks CSWbash

SPKG_SOURCEURL = http://cyberelk.net/tim/software/patchutils/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# /bin/bash is too old
post-configure-modulated:
	find . -type f | fgrep -v fgrep -v .in | \
		xargs perl -pi -e 's,#!/bin/bash,#!/opt/csw/bin/bash,'
	@$(MAKECOOKIE)
