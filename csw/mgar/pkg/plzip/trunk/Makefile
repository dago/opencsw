GARNAME = plzip
GARVERSION = 0.1
CATEGORIES = utils

DESCRIPTION = plzip is a lossless data compressor based on the LZMA algorithm.
define BLURB
  Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
  integrity checking and a user interface similar to the one of gzip or bzip2. Lzip
  decompresses almost as fast as gzip and compresses better than bzip2, which makes
  it well suited for software distribution and data archiving. 
  Currently only compression is performed in parallel. Parallel decompression is
  planned to be implemented soon.
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
