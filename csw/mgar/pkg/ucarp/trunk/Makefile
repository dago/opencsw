# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = ucarp
VERSION = 1.5.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = UCARP is a portable implementation of the CARP protocol. 
define BLURB
  UCARP allows a couple of hosts to share common virtual IP addresses in
  order to provide automatic failover. It is a portable userland
  implementation of the secure and patent-free Common Address Redundancy
  Protocol (CARP, OpenBSD's alternative to the patents-bloated VRRP).
endef

MASTER_SITES = http://download.pureftpd.org/pub/ucarp/
DISTFILES += $(DISTNAME).tar.bz2

PATCHFILES += 0001-Solaris-hacks.patch
PATCHFILES += 0002-Remove-double-invocation-of-SHELL.patch

VENDOR_URL = http://www.ucarp.org/project/ucarp

RUNTIME_DEP_PKGS_CSWucarp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWucarp += CSWlibpcap1

include gar/category.mk
