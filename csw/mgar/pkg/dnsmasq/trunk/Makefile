NAME = dnsmasq
VERSION = 2.59
GARTYPE = v2
CATEGORIES = net

DESCRIPTION = Lightweight DNS forwarder and DHCP server
define BLURB
  Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server. It is designed to provide DNS and, optionally, DHCP, to a small network. It can serve the names of local machines which are not in the global DNS. The DHCP server integrates with the DNS server and allows machines with DHCP-allocated addresses to appear in the DNS with names configured either in each host or in a central configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP/TFTP/PXE for network booting of diskless machines.
endef

MASTER_SITES = http://www.thekelleys.org.uk/dnsmasq/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS =
GARCOMPILER = GNU
SKIPTEST = 1
INSTALL_ARGS = PREFIX=/opt/csw MAKE=gmake INSTALL=ginstall

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

post-install-modulated:

	perl -pi -e 's|/usr/local|/opt/csw|' \
		$(DESTDIR)/opt/csw/share/man/man8/dnsmasq.8
