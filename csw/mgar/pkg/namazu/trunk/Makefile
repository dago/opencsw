GARNAME = namazu
GARVERSION = 2.0.14
CATEGORIES = utils

DESCRIPTION = full-text search engine
define BLURB
  Namazu is a full-text search engine intended for easy use. Not only does it
  work as a small or medium scale Web search engine, but also as a personal
  search system for email or other files.
endef

MASTER_SITES = http://www.namazu.org/stable/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWnamazu.gspec CSWnamazu.depend CSWnamazu.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS += $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
