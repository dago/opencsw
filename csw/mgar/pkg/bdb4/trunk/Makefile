GARNAME = db
GARVERSION = 4.1.25
CATEGORIES = lib

DESCRIPTION = Provides embedded database support for applications
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

MASTER_SITES = ftp://ftp.sleepycat.com/releases/

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = 

ARCHALL = 1
PACKAGES = CSWbdb4
SPKG_DESCRIPTION = Embedded database libraries and utilities
CATALOG_NAME = berkeleydb4 
REQUIRED_PKGS = CSWbdb

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/bdb4/lib/sparcv9
	ginstall -d $(DESTDIR)$(prefix)/bdb4/bin/sparcv9
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s . sparcv8
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s . 32
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s sparcv9 64
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/db.jar db.jar
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb-4.so libdb-4.2.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb-4.so libdb-4.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb.so libdb.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_cxx-4.so libdb_cxx-4.2.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_cxx-4.so libdb_cxx-4.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_cxx.so libdb_cxx.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_java-4.so libdb_java-4.2.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_java-4.so libdb_java-4.2_g.so
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_java-4.so libdb_java-4.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib && gln -s $(libdir)/libdb_java.so libdb_java.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/db.jar db.jar
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb-4.so libdb-4.2.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb-4.so libdb-4.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb.so libdb.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_cxx-4.so libdb_cxx-4.2.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_cxx-4.so libdb_cxx-4.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_cxx.so libdb_cxx.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_java-4.so libdb_java-4.2.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_java-4.so libdb_java-4.2_g.so
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_java-4.so libdb_java-4.so 
	cd $(DESTDIR)$(prefix)/bdb4/lib/sparcv9 && gln -s $(libdir)/sparcv9/libdb_java.so libdb_java.so
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_archive db_archive
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_checkpoint db_checkpoint
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_deadlock db_deadlock
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_dump db_dump
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_load db_load 
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_printlog db_printlog
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_recover db_recover 
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_stat db_stat
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_upgrade db_upgrade
	cd $(DESTDIR)$(prefix)/bdb4/bin && gln -s $(bindir)/db_verify db_verify 
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_archive db_archive
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_checkpoint db_checkpoint 
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_deadlock db_deadlock
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_dump db_dump 
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_load db_load
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_printlog db_printlog
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_recover db_recover
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_stat db_stat
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_upgrade db_upgrade
	cd $(DESTDIR)$(prefix)/bdb4/bin/sparcv9 && gln -s $(bindir)/sparcv9/db_verify db_verify
