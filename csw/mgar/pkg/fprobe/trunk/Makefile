GARNAME = fprobe
GARVERSION = 1.1
CATEGORIES = net

DESCRIPTION = Tool that collect network traffic data
define BLURB
  fprobe - libpcap-based tool that collect network traffic data 
  and emit it as NetFlow flows towards the specified collector.
endef

MASTER_SITES = http://downloads.sourceforge.net/project/fprobe/fprobe/1.1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# we require
REQUIRED_PKGS = CSWlibpcap

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# no build tests
SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pcap=$(includedir)
CONFIGURE_ARGS += --with-libpcap=$(libdir)

include gar/category.mk

pre-configure-modulated:
	@gsed -i'' 's,CFLAGS="$$CFLAGS -DWALL -W -Wall",,' $(WORKSRC)/configure
