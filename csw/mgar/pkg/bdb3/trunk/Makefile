GARNAME = db
GARVERSION = 3.3.11
CATEGORIES = lib

DESCRIPTION = Stub package as contents moved to CSWbdb33
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

PACKAGES = CSWbdb3
CATALOGNAME = berkeleydb3

REQUIRED_PKGS = CSWbdb33

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom

TEST_SCRIPTS =

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ln -s ../bdb33/lib/libdb-3.3.so $(DESTDIR)$(libdir)
	@$(MAKECOOKIE)
