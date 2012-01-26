NAME = patchutils
VERSION = 0.3.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Tools for manipulating patch files
define BLURB
  Patchutils is a small collection of programs that operate on patch files.
endef

MASTER_SITES = http://cyberelk.net/tim/data/patchutils/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# gendiff is needed for the tests
DISTFILES += gendiff

PATCHFILES = patch-use-csw-bash.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS = CSWgnulinks CSWbash CSWdiffutils

RUNTIME_DEP_PKGS = CSWbash CSWperl

SPKG_SOURCEURL = http://cyberelk.net/tim/software/patchutils/

CONFIGURE_ARGS = $(DIRPATHS)

# gendiff is still not found, but the results look otherwise pretty good.
# Ignore for now.
SKIPTEST ?= 1

include gar/category.mk

# WORKDIR is for gendiff, which is needed for tests but missing on Solaris
PATH := /opt/csw/gnu:$(WORKDIR):$(PATH)

# /bin/bash is too old
post-configure-modulated:
	find $(WORKSRC) -type f | grep -v '\.in$$' | grep /tests/ | \
		xargs perl -pi.orig -e 's,/bin/sh,/opt/csw/bin/bash,'
	@$(MAKECOOKIE)
