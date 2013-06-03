NAME = gdbm
VERSION = 1.9
GARTYPE = bts lib
GARTYPE = v2

DESCRIPTION = GNU database library for C
define BLURB
  gdbm is a database indexing library replacement for the traditional
  'dbm' and 'ndbm' libraries. gdm is useful for those who need to write
  C applications and need access to a simple and efficient database.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

FONIMOSSlibgdbm3
OBSOLETED_BY_NIMOSSlibgdbm3 += NIMOSSgdbm

PACKAGES += NIMOSSlibgdbm4
CATALOGNAME_NIMOSSlibgdbm4 = libgdbm4
SPKG_DESC_NIMOSSlibgdbm4 = GDBM share library, libgdbm.so.4
PKGFILES_NIMOSSlibgdbm4 = $(call pkgfiles_lib,libgdbm.so.4)

PACKAGES += NIMOSSlibgdbm-dev
CATALOGNAME_NIMOSSlibgdbm-dev = libgdbm_dev
SPKG_DESC_NIMOSSdev
SPKG_DESC_CSWlibgdbm-dev = Development files for libgdbm.so.4
# This is catchall
NIMOSSlibgdbm-dev = NIMOSSlibgdbm-dev = CSWlibgdbm4

BUILD64_LIBS_ONLY = 1

# gdbm package has no test suite
TEST_SCRIPTS =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

include gar/category.mk

post-install-modulated:
	# These are only informational
	perl -pi -e 's,/usr/local,$(prefix),' $(DESTDIR)$(in