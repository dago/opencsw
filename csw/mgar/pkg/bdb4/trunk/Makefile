GARNAME = db
GARVERSION = 4.2.52
CATEGORIES = lib

DESCRIPTION = Stub package as contents moved to CSWbdb42
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

PACKAGES = CSWbdb4
CATALOGNAME = berkeleydb4

ARCHALL = 1
REQUIRED_PKGS = CSWbdb42

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom

TEST_SCRIPTS =

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(prefix)
	ln -s bdb42 $(DESTDIR)$(prefix)/bdb4
	@$(MAKECOOKIE)
