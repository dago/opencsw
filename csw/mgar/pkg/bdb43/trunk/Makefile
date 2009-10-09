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

MASTER_SITES = http://download.oracle.com/berkeley-db/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(GARVERSION).%,$(PATCHFILES)))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/build_unix

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb43
docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java
CONFIGURE_ARGS += --enable-o_direct

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=$(libpath)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

FIXCONFIG_DIRS  = $(DESTDIR)$(prefix)/bdb43/lib

# bdb tests are time consuming
TEST_SCRIPTS =

PACKAGES = CSWbdb43 CSWbdb43devel CSWbdb43doc

CATALOGNAME_CSWbdb43      = berkeleydb43
CATALOGNAME_CSWbdb43devel = berkeleydb43_devel
CATALOGNAME_CSWbdb43doc   = berkeleydb43_doc

ARCHALL_CSWbdb43doc = 1

SPKG_DESC_CSWbdb43      = BerkeleyDB 4.3
SPKG_DESC_CSWbdb43devel = BerkeleyDB 4.3 development support
SPKG_DESC_CSWbdb43doc   = BerkeleyDB 4.3 documentation

SPKG_SOURCEURL = http://www.oracle.com/technology/products/berkeley-db/index.html

REQUIRED_PKGS_CSWbdb43devel = CSWbdb43

LICENSE = LICENSE

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb43),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.* $(libdir)/db.jar
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.* $(libdir)/db.jar

PKGFILES_CSWbdb43doc = $(PKGFILES_DOC)
PKGFILES_CSWbdb43devel = $(PKGFILES_DEVEL)

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/j2se/bin:$(PATH)
export PATH

configure-dist:
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

