GARNAME = pcre
GARVERSION = 8.10
CATEGORIES = lib

DESCRIPTION = Perl-compatible regular expression tools
define BLURB
  The PCRE library is a set of functions that implement regular
  expression pattern matching using the same syntax and semantics
  as Perl 5. PCRE has its own native API, as well as a set of
  wrapper functions that correspond to the POSIX regular expression API.
endef

MASTER_SITES = ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-Allow-norunpath-for-libtool.patch

SPKG_SOURCEURL = http://www.pcre.org

BUILD_DEP_PKGS = CSWgnulinks
RUNTIME_DEP_PKGS_CSWpcrert = CSWncurses
RUNTIME_DEP_PKGS_CSWpcre = CSWpcrert CSWzlib CSWbzip2 CSWreadline $(RUNTIME_DEP_PKGS_CSWpcrert)

PACKAGES = CSWpcre CSWpcrert
CATALOGNAME_CSWpcrert = pcre_rt
LICENSE = LICENCE

SPKG_DESC_CSWpcrert = Perl-compatible regular expression runtime libraries
SPKG_DESC_CSWpcre = Perl-compatible regular expression tools

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-unicode-properties
CONFIGURE_ARGS += --enable-pcregrep-libz
CONFIGURE_ARGS += --enable-pcregrep-libbz2
CONFIGURE_ARGS += --enable-pcretest-libreadline

EXTRA_LINKER_FLAGS = -lncurses

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWpcrert = $(PKGFILES_RT)

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)
