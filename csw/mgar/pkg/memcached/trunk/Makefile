# $Id$

NAME = memcached
VERSION = 1.4.15
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Distributed memory object caching system
define BLURB
  memcached is a high-performance, distributed memory object caching system,
  generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load.
endef

MASTER_SITES = http://memcached.googlecode.com/files/
DISTFILES = $(NAME)-$(VERSION).tar.gz

## Use patches until this is applied:
##   https://github.com/memcached/memcached/pull/3
#PATCHFILES += 0001-Fix-alignment-check-as-84148994-0x05040302.patch
#PATCHFILES += 0002-Take-endianness-into-account-on-alignment-check.patch
#
## The addition of more status field made the data arrive in multiple packets
## leading to broken tests when it is not waited for more packages.
# PATCHFILES += 0003-Make-sure-to-wait-for-data.patch
#
## Looks like the data structure is not clean on sparcv9 (only!)
#PATCHFILES += 0004-Make-sure-to-clean-ai_flags-in-testsuite-or-test-fai.patch

#PATCHFILES += 0001-Fix-memcached_dtrace.d-and-add-touch-command.patch

# If we enable GIT patching this makes a .git repo in $WORKSRC.
# Unfortunatly this triggers maintainer mode for t/whitespace.t which
# then fails because the developer GIT repo contains more things than the
# distributed release tarball.
NOGITPATCH = 1

VENDOR_URL = http://memcached.org/

BUILD_DEP_PKGS = CSWlibevent-dev
RUNTIME_DEP_PKGS = CSWlibevent2-0-5

# Solaris 9 does not have atomic_inc_ushort_nv
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --enable-sasl
#CONFIGURE_ARGS += --enable-sasl-pwdb

CONFIGURE_ARGS-sol5.10 += --enable-dtrace
CONFIGURE_ARGS += $(CONFIGURE_ARGS-sol$(GAROSREL))

TEST_TARGET = test

include gar/category.mk

