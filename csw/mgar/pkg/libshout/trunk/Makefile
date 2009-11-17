GARNAME = libshout
GARVERSION = 2.2.2
CATEGORIES = lib

DESCRIPTION = Icecast library
define BLURB
endef

MASTER_SITES = http://downloads.us.xiph.org/releases/libshout/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWlibogg CSWtheora CSWvorbis
PRERQUISITE_PKGS = $(REQUIRED_PKGS)

#         GAR default: -xO3 -xarch=v8 -I/opt/csw/include
# Configure hardwired: -xO4 -fast -w -fsimple -native -xcg92

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_ARGS = CFLAGS="-xO4 -fast -w -fsimple -native -xcg92 $(filter -xarch=% -I%,$(CFLAGS))"

TEST_TARGET = check

include gar/category.mk
