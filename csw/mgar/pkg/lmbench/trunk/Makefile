# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! doesn't build yet gcc: error: language arch=v8 not recognized
# ! doesn't honor our build flags (e.g. gcc get's used despite CC)
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
BUILD_TARGET = build

include gar/category.mk

# relies on grep -r
PATH := /opt/csw/gnu:$(PATH)
