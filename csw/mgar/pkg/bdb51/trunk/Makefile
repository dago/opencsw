NAME = db
VERSION = 5.1.29
CATEGORIES = lib

DESCRIPTION = Berkeley DB 5.1
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
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(VERSION).%,$(PATCHFILES)))

BUILD64 = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb51
docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
# No longer there in 4.8
#CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=$(libpath)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

# bdb tests are *very* time consuming
TEST_SCRIPTS =

PACKAGES = CSWbdb51 CSWbdb51devel CSWbdb51doc

CATALOGNAME_CSWbdb51      = berkeleydb51
SPKG_DESC_CSWbdb51        = BerkeleyDB 5.1 embedded database libraries and utilities
RUNTIME_DEP_PKGS_CSWbdb51 += CSWbdb51devel

CATALOGNAME_CSWbdb51devel = berkeleydb51_devel
SPKG_DESC_CSWbdb51devel   = BerkeleyDB 5.1 development support
PKGFILES_CSWbdb51devel    = $(PKGFILES_DEVEL)

CATALOGNAME_CSWbdb51doc   = berkeleydb51_doc
SPKG_DESC_CSWbdb51doc     = BerkeleyDB 5.1 documentation
PKGFILES_CSWbdb51doc      = $(PKGFILES_DOC)

ARCHALL_CSWbdb51doc = 1


SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

LICENSE = LICENSE

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb51),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.* $(libdir)/db.jar
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.* $(libdir)/db.jar

# Remove the license from share/doc/berkeleydb/license/.*
# because GAR expects license to be a file instead of a directory
EXTRA_MERGE_EXCLUDE_FILES = .*/license.*


include gar/category.mk

LIBS += -lnsl
export LIBS

JAVA_HOME := /usr/jdk1.6.0_20
export JAVA_HOME
PATH := $(JAVA_HOME)/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

