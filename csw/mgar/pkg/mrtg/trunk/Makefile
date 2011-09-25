NAME = mrtg
VERSION = 2.17.2
CATEGORIES = utils

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

PACKAGING_PLATFORMS =  solaris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gd=/opt/csw
CONFIGURE_ARGS += --with-gd-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-gd-inc=/opt/csw/include

RUNTIME_DEP_PKGS_CSWmrtg += CSWperl
RUNTIME_DEP_PKGS_CSWmrtg += CSWlibgd2
RUNTIME_DEP_PKGS_CSWmrtg += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWmrtg += CSWlibz1

# Reviewed checkpkg overrides
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/lib/mrtg2/Net_SNMP_util.pm
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/mrtg-rrd.1
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/mrtg-unix-guide.1
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/mrtg-reference.1
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-rrd.txt
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/CHANGES
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-unix-guide.txt
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-reference.txt
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-rrd.pod
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-reference.pod
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mrtg2/mrtg-unix-guide.pod
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/mrtg-squid.1
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/share|root/opt/csw/share/doc/mrtg2/mrtg-squid.pod
CHECKPKG_OVERRIDES_CSWmrtg += file-with-bad-content|/usr/share|root/opt/csw/share/doc/mrtg2/mrtg-squid.txt

TEST_TARGET =

include gar/category.mk
