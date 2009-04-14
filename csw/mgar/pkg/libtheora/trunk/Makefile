GARNAME = libtheora
GARVERSION = 1.0
CATEGORIES = lib

DESCRIPTION = Theora video codec support library
define BLURB
  Theora is a free and open video compression format from the Xiph.org Foundation.
  Like all our multimedia technology it can be used to distribute film and video
  online and on disc without the licensing and royalty fees or vendor lock-in
  associated with other formats. 
endef

MASTER_SITES = http://downloads.xiph.org/releases/theora/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://www.theora.org

PREREQUISITE_PKGS = CSWtransfig
REQUIRED_PKGS = CSWlibogg

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-examples
CONFIGURE_ARGS += --disable-asm

TEST_TARGET = check

include gar/category.mk
