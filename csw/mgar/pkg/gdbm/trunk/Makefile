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

# gdbm package has no test suite
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ROOT = $(DESTDIR)
export INSTALL_ROOT
EXTRA_COMMON_EXPORTS = INSTALL_ROOT

BUILD64 = 1

include gar/category.mk
