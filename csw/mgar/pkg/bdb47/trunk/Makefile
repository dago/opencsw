GARNAME = db
GARVERSION = 4.7.25
CATEGORIES = lib

DESCRIPTION = Berkeley DB 4.7
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

# No patches for the 4.7 series... yet.
#PATCHDIR = $(WORKSRC)/..
#PATCHDIRLEVEL = 0
#PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*.diff))

BUILD64 = 1
CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb47
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
ifeq ($(MEMORYMODEL),32)
CONFIGURE_ARGS += --enable-tcl
CONFIGURE_ARGS += --with-tcl=$(libdir)
endif

FIXCONFIG_DIRS  = $(DESTDIR)$(prefix)/bdb47/lib

# bdb tests are *very* time consuming
TEST_SCRIPTS =

NO_ISAEXEC = 1

PACKAGES = CSWbdb47 CSWbdb47-devel CSWbdb47-doc

CATALOGNAME_CSWbdb47       = berkeleydb47
CATALOGNAME_CSWbdb47-devel = berkeleydb47_devel
CATALOGNAME_CSWbdb47-doc   = berkeleydb47_doc

ARCHALL_CSWbdb47-doc = 1

SPKG_DESC_CSWbdb47       = BerkeleyDB 4.7 embedded database libraries and utilities
SPKG_DESC_CSWbdb47-devel = BerkeleyDB 4.7 development support
SPKG_DESC_CSWbdb47-doc   = BerkeleyDB 4.7 documentation

REQUIRED_PKGS_CSWbdb47-devel = CSWbdb47

LICENSE = LICENSE

PKGFILES_CSWbdb47-doc = $(prefix)/docs/.*

PKGFILES_CSWbdb47-devel = $(PKGFILES_DEVEL)

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/jdk1.6.0_07/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)

