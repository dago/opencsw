GARNAME = memcached
GARVERSION = 1.4.3
CATEGORIES = net

DESCRIPTION = Distributed memory object caching system
define BLURB
  memcached is a high-performance, distributed memory object caching system,
  generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load.
endef

MASTER_SITES = http://memcached.googlecode.com/files/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.danga.com/memcached/

PREREQUISITE_PKGS = CSWlibevent-devel
REQUIRED_PKGS = CSWlibevent

# Solaris 8 Sparc does work, but Solaris 8 x86 has many failed tests due to
# errors in Solaris 8 itself. For consistency we build from Solaris 9 on for
# both ISAs.
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

