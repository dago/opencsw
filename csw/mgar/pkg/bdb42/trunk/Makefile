GARNAME = db
GARVERSION = 4.2.52
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

PACKAGES = CSWbdb42 CSWbdb42-devel CSWbdb42-doc

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*.diff))

BUILD64 = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb42
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

FIXCONFIG_DIRS  = $(DESTDIR)$(prefix)/bdb42/lib

# bdb tests are *very* time consuming
TEST_SCRIPTS =

NO_ISAEXEC = 1

PACKAGES = CSWbdb42 CSWbdb42-devel CSWbdb42-doc

CATALOGNAME_CSWbdb42       = berkeleydb42
CATALOGNAME_CSWbdb42-devel = berkeleydb42_devel
CATALOGNAME_CSWbdb42-doc   = berkeleydb42_doc

ARCHALL_CSWbdb42-doc = 1

SPKG_DESC_CSWbdb42       = BerkeleyDB 4.2 embedded database libraries and utilities
SPKG_DESC_CSWbdb42-devel = BerkeleyDB 4.2 development support
SPKG_DESC_CSWbdb42-doc   = BerkeleyDB 4.2 documentation

REQUIRED_PKGS_CSWbdb42-devel = CSWbdb42
INCOMPATIBLE_PKGS_CSWbdb42-doc = CSWbdb42doc

LICENSE = LICENSE

# Leave the docs where they are for now
#EXTRA_PAX_ARGS_isa-sparcv8 = -s ",^\.$(prefix)/docs/,$(docdir)/bdb42/,p"
#EXTRA_PAX_ARGS_isa-i386    = -s ",^\.$(prefix)/docs/,$(docdir)/bdb42/,p"

#PKGFILES_CSWbdb42-doc = $(PKGFILES_DOC)
PKGFILES_CSWbdb42-doc = $(prefix)/docs/.*

PKGFILES_CSWbdb42-devel = $(PKGFILES_DEVEL)

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
