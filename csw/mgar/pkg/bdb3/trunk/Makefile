GARNAME = db
GARVERSION = 3.3.11
CATEGORIES = lib

DESCRIPTION = BerkeleyDB 3
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

MASTER_SITES = http://download.oracle.com/berkeley-db/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# See http://www.sleepycat.com/update/4.1.25/patch.4.1.25.html
PATCHFILES = patch.$(GARVERSION).1 patch.$(GARVERSION).2
PATCHDIRLEVEL = 0

LICENSE = LICENSE

PACKAGES = CSWbdb3
CATALOGNAME = berkeleydb3

CONFIGURE_SCRIPTS = $(WORKSRC)/dist/configure
BUILD_SCRIPTS = $(WORKSRC)/dist/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/dist/Makefile

TEST_SCRIPTS =

#NODIRPATHS = --prefix
CONFIGURE_ARGS  = --prefix $(prefix) $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java
CONFIGURE_ARGS += --enable-tcl
CONFIGURE_ARGS += --with-tcl=$(libdir)

include gar/category.mk
