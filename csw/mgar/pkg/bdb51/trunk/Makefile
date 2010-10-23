GARNAME = db
GARVERSION = 5.0.26
CATEGORIES = lib

DESCRIPTION = Berkeley DB 5.0
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

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(GARVERSION).%,$(PATCHFILES)))

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb50
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

PACKAGES = CSWbdb50 CSWbdb50devel CSWbdb50doc

CATALOGNAME_CSWbdb50      = berkeleydb50
CATALOGNAME_CSWbdb50devel = berkeleydb50_devel
CATALOGNAME_CSWbdb50doc   = berkeleydb50_doc

ARCHALL_CSWbdb50doc = 1

SPKG_DESC_CSWbdb50      = BerkeleyDB 5.0 embedded database libraries and utilities
SPKG_DESC_CSWbdb50devel = BerkeleyDB 5.0 development support
SPKG_DESC_CSWbdb50doc   = BerkeleyDB 5.0 documentation

SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

LICENSE = LICENSE

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb50),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.* $(libdir)/db.jar
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.* $(libdir)/db.jar

# Remove the license from share/doc/berkeleydb/license/.*
# because GAR expects license to be a file instead of a directory
EXTRA_MERGE_EXCLUDE_FILES = .*/license.*

PKGFILES_CSWbdb50doc = $(PKGFILES_DOC)
PKGFILES_CSWbdb50devel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/lib|opt/csw/bdb50/lib/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/bdb50/lib/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/opt/studio/SOS12/SUNWspro/lib|opt/csw/bdb50/lib/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/opt/studio/SOS12/SUNWspro/lib/rw7|opt/csw/bdb50/lib/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/lib/64|opt/csw/bdb50/lib/amd64/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/opt/studio/SOS12/SUNWspro/lib/amd64|opt/csw/bdb50/lib/amd64/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/opt/studio/SOS12/SUNWspro/lib/rw7/amd64|opt/csw/bdb50/lib/amd64/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/usr/ccs/lib/amd64|opt/csw/bdb50/lib/amd64/libdb_cxx-5.0.so
CHECKPKG_OVERRIDES_CSWbdb50 += bad-rpath-entry|/usr/lib/64|opt/csw/bdb50/lib/amd64/libdb_cxx-5.0.so


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

