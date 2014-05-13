# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-make
VERSION = 2.6.6
GARTYPE = v2

DESCRIPTION = GNUstep-core make
define BLURB
  GNUstep-core make infrastructure and configuration files. Needed for all GNUstep setups.
endef

BUILD_DEP_PKGS = CSWgmake CSWgcc4objc

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

#we have no tests anyway
SKIPTEST = 1

prefix = $(BUILD_PREFIX)/GNUstep

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-layout=gnustep 
#CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"

include gar/category.mk

