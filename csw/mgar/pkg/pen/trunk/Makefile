GARNAME = pen
GARVERSION = 0.18.0
CATEGORIES = utils

DESCRIPTION = Simple load balancer
define BLURB
  This is pen, a load balancer for "simple" tcp based protocols such as http 
  or smtp. It allows several servers to appear as one to the outside and 
  automatically detects servers that are down and distributes clients among 
  the available servers. This gives high availability and scalable performance. 
endef

MASTER_SITES = ftp://siag.nu/pub/pen/
MASTER_SITES += http://siag.nu/pub/pen/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software 
# release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --with-docdir=$(docdir)/$(GARNAME)

# no tests, well...
TEST_SCRIPTS =

include gar/category.mk
