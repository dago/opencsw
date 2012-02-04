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

VENDOR_URL = http://www.pcre.org

PACKAGES = CSWpcre
CATALOGNAME_CSWpcre = pcre
SPKG_DESC_CSWpcre = Perl-compatible regular expression tools
RUNTIME_DEP_PKGS_CSWpcre += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre16-0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibz1
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcreposix0

PACKAGES += CSWlibpcre-dev
SPKG_DESC_CSWlibpcre-dev = Development files for libpcre.so.1, libpcre16.so.0, libpcrecpp.so.0 and libpcreposix.so.0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcre16-0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcreposix0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcrecpp0
PKGFILES_CSWlibpcre-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpcre-dev += $(docdir)/.*
OBSOLETED_BY_CSWlibpcre-dev += CSWpcre-devel
# Leave these in the docs for now
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/pcre-config.txt
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/pcre.txt
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/README
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/html/pcre-config.html
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/html/pcresample.html
CHECKPKG_OVERRIDES_CSWlibpcre-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pcre/html/pcredemo.html

PACKAGES += CSWlibpcre1
SPKG_DESC_CSWlibpcre1 = Perl-compatible regular expression tools, libpcre.so.1
PKGFILES_CSWlibpcre1 = $(call pkgfiles_lib,libpcre.so.1)

PACKAGES += CSWlibpcre16-0
SPKG_DESC_CSWlibpcre16-0 = Perl-compatible regular expression tools, libpcre16.so.0
PKGFILES_CSWlibpcre16-0 = $(call pkgfiles_lib,libpcre16.so.0)

PACKAGES += CSWlibpcrecpp0
SPKG_DESC_CSWlibpcrecpp0 += Perl-compatible regular expression tools, libpcrecpp.so.0
PKGFILES_CSWlibpcrecpp0 += $(call pkgfiles_lib,libpcrecpp.so.0)
RUNTIME_DEP_PKGS_CSWlibpcrecpp0 += CSWlibpcre0

PACKAGES += CSWlibpcreposix0
SPKG_DESC_CSWlibpcreposix0 += Perl-compatible regular expression tools, libpcreposix.so.0
PKGFILES_CSWlibpcreposix0 += $(call pkgfiles_lib,libpcreposix.so.0)
RUNTIME_DEP_PKGS_CSWlibpcreposix0 += CSWlibpcre0

REINPLACE_USRLOCAL += doc/pcre-config.1
REINPLACE_USRLOCAL += doc/pcresample.3

BUILD64_LIBS_ONLY = 1

EXTRA_LINKER_FLAGS = -norunpath

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

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)

test-custom:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	cd $(WORKSRC) && /usr/bin/ulimit -s 16384 && /usr/bin/env -i $(TEST_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

