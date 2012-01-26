NAME = fortune4all
VERSION = 1023
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = 
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = Fortune4All-src-$(VERSION).zip
#DISTFILES += fortune.zip
DISTFILES += fortune_big.zip
#DISTFILES += greek-fortunes.zip

PATCHFILES = 0001-Fix-for-Sun-CC.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = license

DISTNAME = Fortune

CONFIGURE_SCRIPTS = 

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)"

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk


