GARNAME = libdatrie
GARVERSION = 0.2.2
CATEGORIES = lib

DESCRIPTION = Double array tree library
define BLURB
endef

MASTER_SITES = ftp://linux.thai.net/pub/ThaiLinux/software/libthai/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://linux.thai.net/~thep/datrie/datrie.html

REQUIRED_PKGS = CSWiconv

EXTRA_LINKER_FLAGS = -liconv
BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
