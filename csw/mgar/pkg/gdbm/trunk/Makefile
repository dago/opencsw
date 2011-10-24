NAME = gdbm
VERSION = 1.9
CATEGORIES = lib

DESCRIPTION = GNU database library for C
define BLURB
  gdbm is a database indexing library replacement for the traditional
  'dbm' and 'ndbm' libraries. gdm is useful for those who need to write
  C applications and need access to a simple and efficient database.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWgdbm
CATALOGNAME_CSWgdbm = gdbm
SPKG_DESC_CSWgdbm = Legacy package as contents moved to CSWlibgdbm3
PKGFILES_CSWgdbm = NOFILES
ARCHALL_CSWgdbm = 1
# This is the legacy dependency for applications depending on CSWgdbm to require libgdbm.so.3
RUNTIME_DEP_PKGS_CSWgdbm = CSWlibgdbm3
CHECKPKG_OVERRIDES_CSWgdbm += surplus-dependency|CSWlibgdbm3

PACKAGES += CSWlibgdbm4
CATALOGNAME_CSWlibgdbm4 = libgdbm4
SPKG_DESC_CSWlibgdbm4 = GDBM share library, libgdbm.so.4
PKGFILES_CSWlibgdbm4 = $(call pkgfiles_lib,libgdbm.so.4)

PACKAGES += CSWlibgdbm-dev
CATALOGNAME_CSWlibgdbm-dev = libgdbm_dev
SPKG_DESC_CSWlibgdbm-dev = Development files for libgdbm.so.4
# This is catchall
RUNTIME_DEP_PKGS_CSWlibgdbm-dev = CSWlibgdbm4

BUILD64 = 1

# gdbm package has no test suite
TEST_SCRIPTS =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

include gar/category.mk

post-install-modulated:
	# These are only informational
	perl -pi -e 's,/usr/local,$(prefix),' $(DESTDIR)$(infodir)/gdbm.info
