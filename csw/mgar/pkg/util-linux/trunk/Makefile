# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# 
# Programs to build from this source:
# - watch
# - column
NAME = util-linux
MINOR_VER = 2.24
PATCHLEVEL = .1
VERSION = $(MINOR_VER)$(PATCHLEVEL)
GARTYPE = v2RSION)$(PATCHLEVEL)

DESCRIPTION = A collection of basic utilities
define BLURB
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.
endef

s://www.kernel.org/pub/linux/utils/$(NAME)/v$(MINOR_VER)/
DISTFILES  = $(DISTNAME).tar.xz

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
