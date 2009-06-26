GARNAME = db
GARVERSION = 4.3.29
CATEGORIES = lib

DESCRIPTION = BerkeleyDB 4.3 libraries and utilities
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

MASTER_SITES = http://downloads.sleepycat.com/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWbdb43,depend prototype)
DISTFILES += $(call admfiles,CSWbdb43-devel,depend prototype)
DISTFILES += $(call admfiles,CSWbdb43-doc,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/build_unix

CONFIGURE_SCRIPTS = dist

CONFIGURE_ARGS  = --prefix $(prefix)/bdb43
CONFIGURE_ARGS += --disable-cryptography
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java
CONFIGURE_ARGS += --enable-tcl
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --enable-o_direct

LIBTOOL_LADIR   = $(DESTDIR)$(prefix)/bdb43/lib
STRIP_DIRS     += $(DESTDIR)$(prefix)/bdb43/bin

# bdb tests are time consuming
TEST_SCRIPTS =

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/j2se/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

