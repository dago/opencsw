# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME       = putty
VERSION    = 0.61
GARTYPE    = v2
CATEGORIES = utils

DESCRIPTION = Free implementation of Telnet and SSH
define BLURB
  Free implementation of Telnet and SSH for Windows and Unix platforms, along with an xterm terminal emulator
endef

MASTER_SITES = http://the.earth.li/~sgtatham/putty/latest/

DISTFILES = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

include gar/category.mk
