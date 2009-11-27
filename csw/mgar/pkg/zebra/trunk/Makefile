GARNAME = zebra
GARVERSION = 0.95a
CATEGORIES = server

DESCRIPTION = Manages TCP/IP Based Routing Protocols
define BLURB
  GNU Zebra is free software that manages TCP/IP based routing protocols.
  It is released as part of the GNU Project, and it is distributed under the
  GNU General Public License. It supports BGP-4 protocol as described in RFC1771
  (A Border Gateway Protocol 4) as well as RIPv1, RIPv2 and OSPFv2. Unlike traditional,
  monolithic architectures and even the so-called "new modular architectures" that
  remove the burden of processing routing functions from the cpu and utilize special
  ASIC chips instead, Zebra software offers true modularity.
endef

MASTER_SITES = ftp://ftp.zebra.org/pub/zebra/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Fix-for-Sun-Studio.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_PAX_ARGS = -s ",\.conf.sample\(.*\),.conf\1.CSW,p"

SAMPLECONF = /etc/opt/csw/bgpd.conf
SAMPLECONF += /etc/opt/csw/bgpd.conf2
SAMPLECONF += /etc/opt/csw/ospfd.conf
SAMPLECONF += /etc/opt/csw/ripd.conf
SAMPLECONF += /etc/opt/csw/zebra.conf

MIGRATE_FILES = bgpd.conf ospfd.conf ripd.conf zebra.conf

include gar/category.mk
