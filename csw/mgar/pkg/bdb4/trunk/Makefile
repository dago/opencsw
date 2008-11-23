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
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWbdb4.gspec

# See http://www.sleepycat.com/update/4.1.25/patch.4.1.25.html
PATCHFILES += 4.1.25.1.diff 4.1.25.2.diff
PATCHDIRLEVEL = 0

DEPENDS += lang/tcl

CONFIGURE_SCRIPTS = $(WORKSRC)/dist/configure
BUILD_SCRIPTS = $(WORKSRC)/dist/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/dist/Makefile
TEST_SCRIPTS = $(WORKSRC)/dist/Makefile

NODIRPATHS = --prefix
CONFIGURE_ARGS  = --prefix $(prefix)/bdb4 $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java
CONFIGURE_ARGS += --enable-tcl
CONFIGURE_ARGS += --with-tcl=$(libdir)

include gar/category.mk
