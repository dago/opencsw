NAME = Net-SNMP
VERSION = v6.0.1
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DTOWN

DESCRIPTION = Object oriented interface to SNMP
define BLURB
  The Net::SNMP module abstracts the intricate details of the Simple Network
  Management Protocol by providing a high level programming interface to the
  protocol. Each Net::SNMP object provides a one-to-one mapping between a Perl
  object and a remote SNMP agent or manager. Once an object is created, it can
  be used to perform the basic protocol exchange actions defined by SNMP.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES = CSWpm-net-snmp
CATALOGNAME = pm_net_snmp
ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpm-net-snmp += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Net/SNMP.pm
CHECKPKG_OVERRIDES_CSWpm-net-snmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Net::SNMP.3perl

include gar/category.mk
