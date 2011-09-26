# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! lmbench is supposed to be run from the extracted tarbarll, thus
#   no installation mechanism. See Debian for their packaging approach
#   http://patch-tracker.debian.org/patch/debianonly/view/lmbench/3.0-a9-1
#
NAME = lmbench
VERSION = 3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Utilities to benchmark UNIX systems
define BLURB
  Long description
endef

MASTER_SITES = http://www.bitmover.com/lmbench/
DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# lmbench doesn't use autoconf, but their own set of Makefiles and custom
# written platform detection scripts, cf. Makefile & src/Makefile
CONFIGURE_SCRIPTS =
# There's no test suite
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# Build relies on bk.ver which gets generated from bk VCS version information
# that we don't have. Skip it's generation in favor of pre-build-modulated.
# Beware: $(MAKEFLAGS) doesn't carry -o to make subinvocations, so we need to
# add -o to $(MAKE) instead of $(BUILD_ARGS).
BUILD_ARGS = build CC=$(CC) MAKE="$(MAKE) -o bk.ver"

include gar/category.mk

# relies on grep -r
PATH := /opt/csw/gnu:$(PATH)

pre-build-modulated:
	echo "v3 no-bk-rev-info" > $(WORKSRC)/src/bk.ver
	@$(MAKECOOKIE)

custom-install:
	$(error Easy tiger, there's work to be done first (custom-install))
