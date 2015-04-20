# $Id$

NAME = memcached
VERSION = 1.4.23
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Distributed memory object caching system
define BLURB
  memcached is a high-performance, distributed memory object caching system,
  generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load.
end+= http://www.memcached.org/files/
DISTFILES += $(NAME)-$(VERSION).tar.gz
DISTFILES += mman.ouch-command.patch

# If we enable GIT patching this makes a .git repo in $WORKSRC.
# Unfortunatly this triggers maintainer mode for t/whitespace.t which
# then fails because the developer GIT repo contains more things than the
# distributed release tarball.
NOGITPATCH = 1

VENDOR_URL = http://memcached.org/

BUILD_DEP_PKGS = CSWlibevent-dev
RUNTIME_DEP_PKGS = CSW64 bit is broken on Solaris, disable until this is fixed:
#   https://code.google.com/p/memcached/issues/detail?id=404
# BUILD64 = 1
# ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE += --enable-dtrace

TEST_TARGET = test

include gar/category.mk
