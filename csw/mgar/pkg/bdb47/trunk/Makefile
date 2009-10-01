GARNAME = db
GARVERSION = 4.6.21
CATEGORIES = lib

DESCRIPTION = Berkeley DB 4.6
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

SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))

BUILD64 = 1
CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb46
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=$(libpath)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

# bdb tests are *very* time consuming
TEST_SCRIPTS =

NO_ISAEXEC = 1

PACKAGES = CSWbdb47 CSWbdb47devel CSWbdb47doc

CATALOGNAME_CSWbdb47      = berkeleydb47
CATALOGNAME_CSWbdb47devel = berkeleydb47_devel
CATALOGNAME_CSWbdb47doc   = berkeleydb47_doc

# Remove the license from share/doc/berkeleydb/license/.*
# because GAR expects license to be a file instead of a directory
EXTRA_MERGE_EXCLUDE_FILES = .*/license.*

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb47),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.*
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.*

ARCHALL_CSWbdb47doc = 1

SPKG_DESC_CSWbdb47      = BerkeleyDB 4.7 embedded database libraries and utilities
SPKG_DESC_CSWbdb47devel = BerkeleyDB 4.7 development support
SPKG_DESC_CSWbdb47doc   = BerkeleyDB 4.7 documentation

REQUIRED_PKGS_CSWbdb47devel = CSWbdb47

LICENSE = LICENSE

PKGFILES_CSWbdb47doc = /opt/csw/share/doc/.*

PKGFILES_CSWbdb47devel = $(PKGFILES_DEVEL)

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/jdk1.6.0_07/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
