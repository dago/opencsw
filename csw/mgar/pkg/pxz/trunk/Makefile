NAME = pxz
VERSION = 4.999.9beta.20091201git
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = pxz is a lossless data compressor based on the LZMA algorithm.
define BLURB
  Parallel XZ is a compression utility that takes advantage of running LZMA compression
  of different parts of an input file on multiple cores and processors simultaneously.
  Its primary goal is to utilize all resources to speed up compression time with minimal
  possible influence on compression ratio. 
endef

MASTER_SITES = http://jnovy.fedorapeople.org/pxz/
DISTFILES  = $(NAME)-$(VERSION).tar.xz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
