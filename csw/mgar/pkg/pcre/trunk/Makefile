NAME = pcre
VERSION = 8.36
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Perl-compatible regular expression tools
define BLURB
  The PCRE library is a set of functions that implement regular
  expression pattern matching using the same syntax and semantics
  as Perl 5. PCRE has its own native API, as well as a set of
  wrapper functions that correspond to the POSIX regular expression API.
endef

MASTER_SITES = ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
DISTFILES  = $(DISTNAME).tar.bz2
PATCHFILES = 0001-Allow-norunpath-for-libtool.patch

VENDOR_URL = http://www.pcre.org

PACKAGES = CSWpcre
CATALOGNAME_CSWpcre = pcre
SPKG_DESC_CSWpcre = Perl-compatible regular expression tools
RUNTIME_DEP_PKGS_CSWpcre += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre16-0
RUNTIME_DEP_PKGS_pcre32e += CSWlibpcre16-0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibz1
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcreposix0

PACKAGES += CSWlibpcre-dev
SPKG_DESC_CSWlibpcre-dev = Development files for libpcre.so.1, libpcre16.so.0, libpcrecpp.so.0 and libpcreposix.so.0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcre16-0
RUNTIME_DEP_PKGS_CSWlibpcre-32v += CSWlibpcre16-0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcreposix0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcrecpp0
PKGFILES_CSWlibpcre-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpcre-dev += $(docdir)/.*
OBSOLETED_BY_CSWlibpcre-dev m# We don't want to depend on pcre
CHECKPKG_OVERRIDES_CSWlibpcre-dev += missing-dependency|CSWpcretml/pcredemo.html

PACKAGES += CSWlibpcre1
SPKG_DESC_CSWlibpcre1 = Perl-compatible regular expression tools, libpcre.so.1
PKGFILES_CSWlibpcre1 = $(call pkgfiles_lib,libpcre.so.1)

PACKAGES += CSWlibpcre16-0
SPKG_DESC_CSWlibpcre16-0 = Perl-compatible regular expression tools, libpcre16.so.0
PKGFILES_CSWlibpcre16-0 = $(call pkgfiles_lib,libpcre16.so.0)

PACKA32-0
SPKG_DESC_CSWlibpcre32-0 = Perl-compatible regular expression tools, libpcre32.so.0
PKGFILES_CSWlibpcre32-0 = $(call pkgfiles_lib,libpcre32les_lib,libpcre16.so.0)

PACKAGES += CSWlibpcrecpp0
SPKG_DESC_CSWlibpcrecpp0 += Perl-compatible regular expression tools, libpcrecpp.so.0
PKGFILES_CSWlibpcrecpp0 += $(call pkgfiles_lib,libpcrecpp.so.0)
RUNTIME_DEP_PKGS_CSWlibpcrecpp0 += CSWlibpcre1

PACKAGES += CSWlibpcreposix0
SPKG_DESC_CSWlibpcreposix0 += Perl-compatible regular expression tools, libpcreposix.so.0
PKGFILES_CSWlibpcreposix0 += $(call pkgfiles_lib,libpcreposix.so.0)
RUNTIME_DEP_PKGS_CSWlibpcreposix0 += CSWlibpcre1

REINPLACE_USRLOCAL += doc/pcre-config.1
REINPLACE_USRLOCAL += d# Older compiler like Sun Studio 12 behave differently on -Wl,-i... and -Qoption ld -i...
# This leads to configure detecting something works which later on does not work.
# Newer compilers behave consistently.
# See also http://bugs.exim.org/show_bug.cgi?id=1278
GARCOMPILER = SOS12U= doc/pcresample.3

BUILD64_LIBS_ONLY = 1

EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-unicode-properties
CONFIGURE_ARGS += --enable-pcregrep-libz
CONFIGURE_ARGS += --enable-pcregrep-libbz2
CONFIGURE_ARGS += --enable-pcretest-libreadline
CONFIGURE_ARGS +=CONFIGURE_ARGS += --enable-pcre32

# The stack on Solaris is rather limited, disable stack allocation
CONFIGURE_ARGS += --disable-stack-for-recursion

# No JIT for Sparc, may try for x86 at some later time
#CONFIGURE_ARGS += --enable-jit

# This includes some alias things that don't work with the Sun linker
BUILD_OVERRIDE_VARS += EXTRA_LIBPCRECPP_LDFLAGS

# We need more than the default 8 MB of stack space
# B of stack space
TEST_SCRIPTS = custom

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)

test-custom:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	cd $(WORKSRC) && /usr/bin/ulimit -s 32768 && /usr/bin/env -i $(TEST_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(TEST_ARGS) $(TEST_TARGET)
