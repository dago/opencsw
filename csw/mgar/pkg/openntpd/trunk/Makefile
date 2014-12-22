# Add user/group, see output below:
#chown: /home/bonivart/opencsw/openntpd/trunk/work/solaris10-i386/install-isa-pentium_pro/var/empty: Not owner
#chgrp: /home/bonivart/opencsw/openntpd/trunk/work/solaris10-i386/install-isa-pentium_pro/var/empty: Not owner
#Please create a dedicated group for ntpd.
#Please create a dedicated user for ntpd and ensure it can
#not be used to log in.  This is system-dependant, possibly:
## useradd -g _ntp -s /sbin/nologin -d /var/empty -c 'OpenNTP daemon' _ntp

NAME = openntpd
VERSION = 3.9p1
GARTYPE = v2

DESCRIPTION = OpenBSD Network Time Protocol
define BLURB
endef

MASTER_SITES = http://ftp.eu.openbsd.org/pub/OpenBSD/OpenNTPD/
DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWopenntpd += CSWlibssl1-0-0

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

# There are no tests
SKIPTEST = 1

# Fix before release, need to test software first to find proper config
CHECKPKG_OVERRIDES_CSWopenntpd += bad-location-of-file|file=/var/empty

include gar/category.mk

