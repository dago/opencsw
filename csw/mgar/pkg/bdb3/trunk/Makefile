NAME = db
VERSION = 3.3.11
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
DISTFILES = $(NAME)-$(VERSION).tar.gz 

PATCHDIR = $(WORKDIR)/$(DISTNAME)
WORKSRC = $(PATCHDIR)/build_unix

PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(VERSION).%,$(PATCHFILES)))

BUILD64 = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb33
docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=$(libpath)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

FIXCONFIG_DIRS  = $(DESTDIR)$(prefix)/bdb33/lib

# There are no test scripts for bdb 3.3
TEST_SCRIPTS =

LICENSE = LICENSE
VENDOR_URL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

PACKAGES += CSWbdb3
CATALOGNAME_CSWbdb3 = berkeleydb3
SPKG_DESC_CSWbdb3 = BerkeleyDB 3.3 embedded database libraries and utilities
RUNTIME_DEP_PKGS_CSWbdb3 += CSWtcl
CHECKPKG_OVERRIDES_CSWbdb3 += catalogname-does-not-match-pkgname|pkgname=CSWbdb3|catalogname=berkeleydb3|expected-catalogname=bdb3

PACKAGES += CSWbdb3-dev
CATALOGNAME_CSWbdb3-dev = berkeleydb3_dev
SPKG_DESC_CSWbdb3-dev = BerkeleyDB 3.3 development support
# Keep these in the main package
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWbdb3-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWbdb3-dev = CSWbdb3
CHECKPKG_OVERRIDES_CSWbdb3-dev += surplus-dependency|CSWbdb3
CHECKPKG_OVERRIDES_CSWbdb3-dev += catalogname-does-not-match-pkgname|pkgname=CSWbdb3-dev|catalogname=berkeleydb3_dev|expected-catalogname=bdb3_dev
OBSOLETED_BY_CSWbdb3-dev = CSWbdb3devel
CATALOGNAME_CSWbdb3devel = berkeleydb3_devel_stub

PACKAGES += CSWbdb3-doc
CATALOGNAME_CSWbdb3-doc = berkeleydb3_doc
SPKG_DESC_CSWbdb3-doc = BerkeleyDB 3.3 documentation
PKGFILES_CSWbdb3-doc = $(PKGFILES_DOC)
ARCHALL_CSWbdb3-doc = 1
CHECKPKG_OVERRIDES_CSWbdb3-doc += catalogname-does-not-match-pkgname|pkgname=CSWbdb3-doc|catalogname=berkeleydb3_doc|expected-catalogname=bdb3_doc
OBSOLETED_BY_CSWbdb3-doc = CSWbdb3doc
CATALOGNAME_CSWbdb3doc = berkeleydb3_doc_stub

# These are all pure examples
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/build_unix/flags.html
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/build_unix/install.html
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/build_unix/conf.html
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/build_unix/notes.html
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/sendmail/intro.html
CHECKPKG_OVERRIDES_CSWbdb3-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/berkeleydb3/ref/tcl/intro.html

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir includedir libdir

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_CSWbdb3),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.*
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.*

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
	ginstall -d $(PKGROOT)$(libpath)
	gln -s ../bdb33/lib/libdb-3.3.so $(PKGROOT)$(libpath)
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

