NAME = mrtg
VERSION = 2.17.4
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Multi Router Traffic Grapher (network monitor)
define BLURB
	The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
	load on network-links. MRTG generates HTML pages containing PNG images which
	provide a LIVE visual representation of this traffic.
endef

DISTFILES    = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://oss.oetiker.ch/mrtg/
MASTER_SITES = http://oss.oetiker.ch/mrtg/pub/

PACKAGES = CSWmrtg
CATALOGNAME = mrtg

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGING_PLATFORMS =  solaris9- solaris10-sparc solaris10ris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gd=/opt/csw
CONFIGURE_ARGS += --with-gd-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-gd-inc=/opt/csw/include

RUNTIME_DEP_PKGS_CSWmrtg += CSWperl
RUNTIME_DEP_PKGS_3CSWmrtg += CSWlibz1

# Reviewed checkpkg overrides
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/lib/mrtg
TEST_TARGET =

include gar/category.mk
