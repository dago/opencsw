GARNAME = mrtg
GARVERSION = 2.16.2
CATEGORIES = utils

DESCRIPTION = Multi Router Traffic Grapher (network monitor)
define BLURB
	The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
	load on network-links. MRTG generates HTML pages containing PNG images which
	provide a LIVE visual representation of this traffic.
endef

MASTER_SITES = http://oss.oetiker.ch/mrtg/pub/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmrtg, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gd=/opt/csw
CONFIGURE_ARGS += --with-gd-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-gd-inc=/opt/csw/include

GARCOMPILER = SUN
TEST_TARGET =

include gar/category.mk
