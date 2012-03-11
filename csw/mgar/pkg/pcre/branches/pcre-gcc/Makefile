NAME = pcre
VERSION = 8.30
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

# Use patch until this is fixed:
#   http://bugs.exim.org/show_bug.cgi?id=1206
PATCHFILES += 0002-Remove-bashism.patch

ISA_DEFAULT_i386-5.9 = pentium_pro

VENDOR_URL = http://www.pcre.org

prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

PACKAGES = CSWpcre-gxx
SPKG_DESC_CSWpcre-gxx = Perl-compatible regular expression tools
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibpcre1-gxx
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibpcre16-0-gxx
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibz1
RUNTIME_DEP_PKGS_CSWpcre-gxx += CSWlibpcreposix0-gxx

PACKAGES += CSWlibpcre-gxx-dev
SPKG_DESC_CSWlibpcre-gxx-dev = Development files for libpcre.so.1, libpcre16.so.0, libpcrecpp.so.0 and libpcreposix.so.0
RUNTIME_DEP_PKGS_CSWlibpcre-gxx-dev += CSWlibpcre1-gxx
RUNTIME_DEP_PKGS_CSWlibpcre-gxx-dev += CSWlibpcre16-0-gxx
RUNTIME_DEP_PKGS_CSWlibpcre-gxx-dev += CSWlibpcreposix0-gxx
RUNTIME_DEP_PKGS_CSWlibpcre-gxx-dev += CSWlibpcrecpp0-gxx
PKGFILES_CSWlibpcre-gxx-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpcre-gxx-dev += $(docdir)/.*
# Leave these in the docs for now
CHECKPKG_OVERRIDES_CSWlibpcre-gxx-dev += file-with-bad-content

PACKAGES += CSWlibpcre1-gxx
SPKG_DESC_CSWlibpcre1-gxx = Perl-compatible regular expression tools, libpcre.so.1
PKGFILES_CSWlibpcre1-gxx = $(call pkgfiles_lib,libpcre.so.1)
RUNTIME_DEP_PKGS_CSWlibpcre1-gxx += CSWlibgcc-s1

PACKAGES += CSWlibpcre16-0-gxx
SPKG_DESC_CSWlibpcre16-0-gxx = Perl-compatible regular expression tools, libpcre16.so.0
PKGFILES_CSWlibpcre16-0-gxx = $(call pkgfiles_lib,libpcre16.so.0)
RUNTIME_DEP_PKGS_CSWlibpcre16-0-gxx += CSWlibgcc-s1

PACKAGES += CSWlibpcrecpp0-gxx
SPKG_DESC_CSWlibpcrecpp0-gxx += Perl-compatible regular expression tools, libpcrecpp.so.0
PKGFILES_CSWlibpcrecpp0-gxx += $(call pkgfiles_lib,libpcrecpp.so.0)
RUNTIME_DEP_PKGS_CSWlibpcrecpp0-gxx += CSWlibpcre1-gxx
RUNTIME_DEP_PKGS_CSWlibpcrecpp0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpcrecpp0-gxx += CSWlibstdc++6

PACKAGES += CSWlibpcreposix0-gxx
SPKG_DESC_CSWlibpcreposix0-gxx += Perl-compatible regular expression tools, libpcreposix.so.0
PKGFILES_CSWlibpcreposix0-gxx += $(call pkgfiles_lib,libpcreposix.so.0)
RUNTIME_DEP_PKGS_CSWlibpcreposix0-gxx += CSWlibpcre1-gxx
RUNTIME_DEP_PKGS_CSWlibpcreposix0-gxx += CSWlibgcc-s1

REINPLACE_USRLOCAL += doc/pcre-config.1
REINPLACE_USRLOCAL += doc/pcresample.3

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-unicode-properties
CONFIGURE_ARGS += --enable-pcregrep-libz
CONFIGURE_ARGS += --enable-pcregrep-libbz2
CONFIGURE_ARGS += --enable-pcretest-libreadline
CONFIGURE_ARGS += --enable-pcre16

# No JIT for Sparc, may try for x86 at some later time
#CONFIGURE_ARGS += --enable-jit

# We need more than the default 8 MB of stack space
TEST_SCRIPTS = custom

LD_OPTIONS =

# These checks fail on Solaris 9, because there is no libgcc_s.so.1 installed
# on Solaris 9. However, the library does exist on Solaris 10, where these
# libraries would be run. Checkpkg currently doesn't handle this special case,
# so overrides are used.
CHECKPKG_OVERRIDES_CSWlibpcrecpp0-gxx += soname-not-found|libstdc++.so.6|is|needed|by|opt/csw/gxx/lib/amd64/libpcrecpp.so.0.0.0
CHECKPKG_OVERRIDES_CSWlibpcrecpp0-gxx += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/gxx/lib/amd64/libpcrecpp.so.0.0.0
CHECKPKG_OVERRIDES_CSWlibpcre1-gxx += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/gxx/lib/amd64/libpcre.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibpcreposix0-gxx += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/gxx/lib/amd64/libpcreposix.so.0.0.0
CHECKPKG_OVERRIDES_CSWlibpcre16-0-gxx += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/gxx/lib/amd64/libpcre16.so.0.0.0

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)

test-custom:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	cd $(WORKSRC) && /usr/bin/ulimit -s 16384 && /usr/bin/env -i $(TEST_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

