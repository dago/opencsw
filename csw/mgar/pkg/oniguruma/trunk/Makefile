NAME = oniguruma
VERSION = 5.9.2
CATEGORIES = lib

DESCRIPTION = A regular expression library
define BLURB
  Oniguruma is a regular expressions library.
  The characteristics of this library is that different character encoding 
  for every regular expression object can be specified. 
  (supported APIs: GNU regex, POSIX and Oniguruma native)
endef

MASTER_SITES = http://www.geocities.jp/kosako3/oniguruma/archive/
DISTNAME = onig-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.geocities.jp/kosako3/oniguruma/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
