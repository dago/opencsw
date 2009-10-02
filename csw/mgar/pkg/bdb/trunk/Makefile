GARNAME = db
GARVERSION = 4.7.25
CATEGORIES = lib

DESCRIPTION = Stub package as contents moved to CSWbdb47
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

PACKAGES = CSWbdb
CATALOGNAME = berkeleydb

REQUIRED_PKGS = CSWbdb47

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom

TEST_SCRIPTS =

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ln -s ../bdb47/lib/libdb-4.7.so $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	ln -s ../../bdb47/lib/$(ISA_DEFAULT64)/libdb-4.7.so $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	@$(MAKECOOKIE)
