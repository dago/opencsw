NAME = db
VERSION = 4.8.30
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Berkeley DB 4.8
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

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(VERSION).%,$(PATCHFILES)))

BUILD64 = 1

CONFIGURE_SCRIPTS = dist

# prefix = $(BUILD_PREFIX)/bdb48
prefix = $(BUILD_PREFIX)/stlport4
EXTRA_CXXFLAGS += -library=stlport4

docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
# No longer there in 4.8
#CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
# CONFIGURE_ARGS += --enable-stl
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=$(libpath)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

# bdb tests are *very* time consuming
TEST_SCRIPTS =

VENDOR_URL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

LICENSE = LICENSE

PACKAGES += CSWlibdb-cxx4-8-stlport
SPKG_DESC_CSWlibdb-cxx4-8-stlport = BerkeleyDB 4.8 bindings for C++ with STLPort
PKGFILES_CSWlibdb-cxx4-8-stlport += $(call baseisadirs,$(libdir),libdb_cxx(-\d+(\.\d+)*)?\.so)
# Change later on to new stlport package CSWlibstlport1-stlport
RUNTIME_DEP_PKGS_CSWlibdb-cxx4-8-stlport += CSWstlport

# Compiler run pathes, skip for now
CHECKPKG_OVERRIDES_CSWlibdb-cxx4-8-stlport += bad-rpath-entry

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/jdk1.6.0_20/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

