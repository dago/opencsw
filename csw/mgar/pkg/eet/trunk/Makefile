NAME = eet
VERSION = 1.2.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Write an arbitary set of chunks of data to a file and optionally compress each chunk
define BLURB
  Eet is a tiny library designed to write an arbitary set of chunks of data to a
  file and optionally compress each chunk (very much like a zip file) and allow fast
  random-access reading of the file later on. It does not do zip as zip itself has more
  complexity than we need, and it was much simpler to implement this once here.
endef

MASTER_SITES = http://download.enlightenment.org/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_CPPFLAGS = -D__FUNCTION__=

CPPFLAGS = abc

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
