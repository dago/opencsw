# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = check
VERSION = 0.9.12
GARTYPE = v2

DESCRIPTION = A unit test framework for C

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# Needed for floor()
EXTRA_LINKER_FLAGS += -lm

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
# -pedantic is not rejected, but leads to _mcount not being defined, see for details
#   http://wiki.opencsw.org/porting-faq#toc8
CONFIGURE_ARGS += ax_cv_c_check_flag__pedantic=no

include gar/category.mk

