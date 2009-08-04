GARNAME = patchutils
GARVERSION = 0.3.1
CATEGORIES = utils

DESCRIPTION = Tools for manipulating patch files
define BLURB
  Patchutils is a small collection of programs that operate on patch files.
endef

MASTER_SITES = http://cyberelk.net/tim/data/patchutils/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# gendiff is needed for the tests
DISTFILES += gendiff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWgnulinks CSWbash CSWdiffutils

SPKG_SOURCEURL = http://cyberelk.net/tim/software/patchutils/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# gendiff is still not found, but the results look otherwise pretty good.
# Ignore for now.
SKIPTEST ?= 1

include gar/category.mk

# WORKDIR is for gendiff, which is needed for tests but missing on Solaris
PATH := /opt/csw/gnu:$(WORKDIR):$(PATH)

# /bin/bash is too old
post-configure-modulated:
	find $(WORKSRC) -type f | grep -v '\.in$$' | grep /tests/ | \
		xargs perl -pi -e 's,#!/bin/bash,#!/opt/csw/bin/bash,'
	find $(WORKSRC) -type f | fgrep -v .in | fgrep tests | \
		xargs perl -pi -e 's,/bin/sh,/opt/csw/bin/bash,'
	@$(MAKECOOKIE)
