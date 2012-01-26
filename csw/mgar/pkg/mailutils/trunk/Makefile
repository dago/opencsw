# $Id$
NAME = mailutils
VERSION = 2.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A collection of mail related utilities
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://savannah.gnu.org/projects/mailutils/

# This is needed for __FUNCTION__
EXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__

# This is to find the gnulib generated local lib/stdint.h
EXTRA_CPPFLAGS += -I../lib -I../../lib

CONFIGURE_ARGS = $(DIRPATHS)

# Make sure the gnulib is built first
BUILD_SCRIPTS  = $(WORKSRC)/lib/Makefile
BUILD_SCRIPTS += $(WORKSRC)/Makefile

include gar/category.mk
