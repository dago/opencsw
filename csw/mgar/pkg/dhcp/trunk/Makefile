# split into devel package
# use cswclassutils for conf files and smf support (add init file)
# create doc dir with license

GARNAME = dhcp
GARVERSION = 4.1.0
CATEGORIES = net

DESCRIPTION = ISC DHCP reference implementation
define BLURB
  ISC DHCP is open-source software that implements the Dynamic Host
  Configuration Protocols for connection to a local network. It is a reference
  implementation of those protocols, but it is also production-grade software,
  suitable for use in high-volume and high-reliability applications. 
endef

MASTER_SITES = http://ftp.isc.org/isc/dhcp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdhcp,)

GARCOMPILER = GNU
TEST_TARGET = check

CONFIGURE_ARGS = $(DIRPATHS)

SPKG_SOURCEURL = https://www.isc.org/software/dhcp

include gar/category.mk

