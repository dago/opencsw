GARNAME = gdbm
GARVERSION = 1.8.3
CATEGORIES = lib

DESCRIPTION = GNU database library for C
define BLURB
  gdbm is a database indexing library replacement for the traditional
  'dbm' and 'ndbm' libraries. gdm is useful for those who need to write
  C applications and need access to a simple and efficient database.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgdbm,)

# Makefile install permissions patch
PATCHFILES = perms.diff

# gdbm package has no test suite
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ROOT = $(DESTDIR)
export INSTALL_ROOT

include gar/category.mk
