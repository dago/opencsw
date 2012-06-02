# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = util-linux
VERSION = 2.21
PATCHLEVEL = .2
GARTYPE = v2
CATEGORIES = utils
DISTNAME = $(NAME)-$(VERSION)$(PATCHLEVEL)

DESCRIPTION = A collection of basic utilities
define BLURB
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.
endef

MASTER_SITES = http://www.kernel.org/pub/linux/utils/$(NAME)/v$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

