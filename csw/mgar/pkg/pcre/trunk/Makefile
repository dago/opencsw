NAME = pcre
VERSION = 8.11
CATEGORIES = lib

DESCRIPTION = Perl-compatible regular expression tools
define BLURB
  The PCRE library is a set of functions that implement regular
  expression pattern matching using the same syntax and semantics
  as Perl 5. PCRE has its own native API, as well as a set of
  wrapper functions that correspond to the POSIX regular expression API.
endef

MASTER_SITES = ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES = 0001-Allow-norunpath-for-libtool.patch

# pcregrep testsuite crashes as reported here:
#   http://bugs.exim.org/show_bug.cgi?id=1054
# Use fix for 64 bit PPC which solves the problem as reported in this bug report:
#   http://bugs.exim.org/show_bug.cgi?id=1048
PATCHFILES += bug-attachment-433.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.pcre.org

BUILD_DEP_PKGS = CSWgnulinks

PACKAGES = CSWpcre
CATALOGNAME_CSWpcre = pcre
SPKG_DESC_CSWpcre = Perl-compatible regular expression tools
RUNTIME_DEP_PKGS_CSWpcre += CSWreadline
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWpcre += CSWbzip2
RUNTIME_DEP_PKGS_CSWpcre += CSWzlib
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcreposix0

PACKAGES += CSWpcrert
CATALOGNAME_CSWpcrert = pcre_rt
SPKG_DESC_CSWpcrert = Legacy stub as contents was moved to libpcre0, libpcrecpp0 and libpcreposix0
PKGFILES_CSWpcrert = NOFILES
RUNTIME_DEP_PKGS_CSWpcrert = CSWlibpcre0 CSWlibpcrecpp0 CSWlibpcreposix0
# This is a legacy lib, force dependencies to new libraries
CHECKPKG_OVERRIDES_CSWpcrert += surplus-dependency|CSWlibpcrecpp0
CHECKPKG_OVERRIDES_CSWpcrert += surplus-dependency|CSWlibpcreposix0
CHECKPKG_OVERRIDES_CSWpcrert += surplus-dependency|CSWlibpcre0
ARCHALL_CSWpcrert = 1

PACKAGES += CSWpcre-devel
CATALOGNAME_CSWpcre-devel = pcre_devel
SPKG_DESC_CSWpcre-devel = Development files for PCRE
RUNTIME_DEP_PKGS_CSWpcre-devel += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWpcre-devel += CSWlibpcreposix0
RUNTIME_DEP_PKGS_CSWpcre-devel += CSWlibpcrecpp0
PKGFILES_CSWpcre-devel = $(PKGFILES_DEVEL)

PACKAGES += CSWlibpcre0
CATALOGNAME_CSWlibpcre0 = libpcre0
SPKG_DESC_CSWlibpcre0 = Perl-compatible regular expression tools, libpcre.so.0
PKGFILES_CSWlibpcre0 = $(call baseisadirs,$(libdir),libpcre\.so\.0(\.\d+)*)

PACKAGES += CSWlibpcrecpp0
CATALOGNAME_CSWlibpcrecpp0 = libpcrecpp0
SPKG_DESC_CSWlibpcrecpp0 += Perl-compatible regular expression tools, libpcrecpp.so.0
PKGFILES_CSWlibpcrecpp0 += $(call baseisadirs,$(libdir),libpcrecpp\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibpcrecpp0 += CSWlibpcre0

PACKAGES += CSWlibpcreposix0
CATALOGNAME_CSWlibpcreposix0 = libpcreposix0
SPKG_DESC_CSWlibpcreposix0 += Perl-compatible regular expression tools, libpcreposix.so.0
PKGFILES_CSWlibpcreposix0 += $(call baseisadirs,$(libdir),libpcreposix\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibpcreposix0 += CSWlibpcre0

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-unicode-properties
CONFIGURE_ARGS += --enable-pcregrep-libz
CONFIGURE_ARGS += --enable-pcregrep-libbz2
CONFIGURE_ARGS += --enable-pcretest-libreadline

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)
