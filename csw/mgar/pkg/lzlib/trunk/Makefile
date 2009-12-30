GARNAME = lzlib
GARVERSION = 0.8-rc1
CATEGORIES = lib

DESCRIPTION = lzlib is a lossless data compression library based on the LZMA algorithm.
define BLURB
  The lzlib compression library provides in-memory LZMA compression and
  decompression functions, including integrity checking of the uncompressed
  data. The compressed data format used by the library is the lzip format. 
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/lzip/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER    = GNU
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
