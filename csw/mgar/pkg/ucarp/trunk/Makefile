# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = ucarp
VERSION = 1.5.2
CATEGORIES = apps

DESCRIPTION = UCARP is a portable implementation of the CARP protocol. 
define BLURB
  UCARP allows a couple of hosts to share common virtual IP addresses in
  order to provide automatic failover. It is a portable userland
  implementation of the secure and patent-free Common Address Redundancy
  Protocol (CARP, OpenBSD's alternative to the patents-bloated VRRP).
endef

VENDOR_URL   = http://www.ucarp.org/project/ucarp
MASTER_SITES = http://download.pureftpd.org/pub/ucarp/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
