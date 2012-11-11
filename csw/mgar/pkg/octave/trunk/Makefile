# TBD:
#  configure: error: You are required to have BLAS and LAPACK libraries

NAME = octave
VERSION = 3.6.2
GARTYPE = v2

DESCRIPTION = The GNU Octave language for numerical computations
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

