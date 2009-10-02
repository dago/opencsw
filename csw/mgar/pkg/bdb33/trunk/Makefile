GARNAME = db
GARVERSION = 3.3.11
CATEGORIES = lib

DESCRIPTION = embedded database libraries and utilities
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

#BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb33
docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-cryptography
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

FIXCONFIG_DIRS  = $(DESTDIR)$(prefix)/bdb33/lib

# bdb tests are *very* time consuming
TEST_SCRIPTS =

PACKAGES = CSWbdb33 CSWbdb33devel CSWbdb33doc

CATALOGNAME_CSWbdb33      = berkeleydb33
CATALOGNAME_CSWbdb33devel = berkeleydb33_devel
CATALOGNAME_CSWbdb33doc   = berkeleydb33_doc

ARCHALL_CSWbdb33doc = 1

SPKG_DESC_CSWbdb33      = BerkeleyDB 3.3 embedded database libraries and utilities
SPKG_DESC_CSWbdb33devel = BerkeleyDB 3.3 development support
SPKG_DESC_CSWbdb33doc   = BerkeleyDB 3.3 documentation

SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

REQUIRED_PKGS_CSWbdb33devel = CSWbdb33
INCOMPATIBLE_PKGS_CSWbdb33doc = CSWbdb33doc

LICENSE = LICENSE

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir includedir libdir

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb33),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.*
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.*

PKGFILES_CSWbdb33doc = $(PKGFILES_DOC)
PKGFILES_CSWbdb33devel = $(PKGFILES_DEVEL)

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

