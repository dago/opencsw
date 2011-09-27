# $Id$
#
NAME = libmemcached
VERSION = 0.52
VENDOR_URL = http://libmemcached.org/
CATEGORIES = lib
DESCRIPTION = Library memcached interface
define BLURB
  memcached url
endef
SPKG_SOURCEURL = http://libmemcached.org/
MASTER_SITES = http://launchpad.net/libmemcached/1.0/$(VERSION)/+download/

PATCHFILES += 0001-Do-not-do-PANDORA_TEST_VC_DIR.patch
PATCHFILES += 0002-Use-opt-csw-bin-ggrep.patch

BUILD_DEP_PKGS += CSWlibevent-dev
RUNTIME_DEP_PKGS += CSWlibevent2-0-5

DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dtrace
CONFIGURE_ARGS += --disable-rpath

BUILD64 = 1
SKIPTEST = 1

OPT_FLAGS_SOS = -xO3
OPT_FLAGS_GCC = -O2 -pipe

GARCOMPILER = GCC4

include gar/category.mk

