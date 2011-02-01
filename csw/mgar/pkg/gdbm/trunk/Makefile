NAME = gdbm
VERSION = 1.8.3
CATEGORIES = lib

DESCRIPTION = GNU database library for C
define BLURB
  gdbm is a database indexing library replacement for the traditional
  'dbm' and 'ndbm' libraries. gdm is useful for those who need to write
  C applications and need access to a simple and efficient database.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Makefile install permissions patch
PATCHFILES = perms.diff

PACKAGES = CSWgdbm
CATALOGNAME_CSWgdbm = gdbm
SPKG_DESC_CSWgdbm = Legacy package as contents moved to CSWlibgdbm3
PKGFILES_CSWgdbm = NOFILES
ARCHALL_CSWgdbm = 1
RUNTIME_DEP_PKGS_CSWgdbm = CSWlibgdbm3
CHECKPKG_OVERRIDES_CSWgdbm += surplus-dependency|CSWlibgdbm3

PACKAGES += CSWlibgdbm3
CATALOGNAME_CSWlibgdbm3 = libgdbm3
SPKG_DESC_CSWlibgdbm3 = GDBM share library, libgdbm.so.3
PKGFILES_CSWlibgdbm3 = $(call baseisadirs,$(libdir),libgdbm\.so\.3(\.\d+)*)

PACKAGES += CSWlibgdbm-dev
CATALOGNAME_CSWlibgdbm-dev = libgdbm_dev
SPKG_DESC_CSWlibgdbm-dev = Development Files for libgdbm
# This is catchall
RUNTIME_DEP_PKGS_CSWlibgdbm-dev = CSWlibgdbm3

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

# gdbm package has no test suite
TEST_SCRIPTS =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

include gar/category.mk

post-install-modulated:
	# These are only informational
	perl -pi -e 's,/usr/local,$(prefix),' $(DESTDIR)$(infodir)/gdbm.info
