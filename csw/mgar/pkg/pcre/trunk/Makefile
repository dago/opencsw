NAME = pcre
VERSION = 8.21
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
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpcre += CSWlibz1
RUNTIME_DEP_PKGS_CSWpcre += CSWlibpcreposix0

PACKAGES += CSWlibpcre-dev
SPKG_DESC_CSWlibpcre-dev = Development files for libpcre.so.0, libpcrecpp.so.0 and libpcreposix.so.0
RUNTIME_DEP_PKGS_CSWlibpcre-dev += CSWlibpcre0
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

PACKAGES += CSWlibpcre0
CATALOGNAME_CSWlibpcre0 = libpcre0
SPKG_DESC_CSWlibpcre0 = Perl-compatible regular expression tools, libpcre.so.0
PKGFILES_CSWlibpcre0 = $(call pkgfiles_lib,libpcre.so.0)
OBSOLETED_BY_CSWlibpcre0 += CSWpcrert
CATALOGNAME_CSWpcrert = pcre_rt_stub

PACKAGES += CSWlibpcrecpp0
CATALOGNAME_CSWlibpcrecpp0 = libpcrecpp0
SPKG_DESC_CSWlibpcrecpp0 += Perl-compatible regular expression tools, libpcrecpp.so.0
PKGFILES_CSWlibpcrecpp0 += $(call pkgfiles_lib,libpcrecpp.so.0)
RUNTIME_DEP_PKGS_CSWlibpcrecpp0 += CSWlibpcre0
OBSOLETED_BY_CSWlibpcrecpp0 += CSWpcrert

PACKAGES += CSWlibpcreposix0
CATALOGNAME_CSWlibpcreposix0 = libpcreposix0
SPKG_DESC_CSWlibpcreposix0 += Perl-compatible regular expression tools, libpcreposix.so.0
PKGFILES_CSWlibpcreposix0 += $(call pkgfiles_lib,libpcreposix.so.0)
RUNTIME_DEP_PKGS_CSWlibpcreposix0 += CSWlibpcre0
OBSOLETED_BY_CSWlibpcreposix0 += CSWpcrert

REINPLACE_USRLOCAL += doc/pcre-config.1
REINPLACE_USRLOCAL += doc/pcresample.3

BUILD64_LIBS_ONLY = 1

EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-unicode-properties
CONFIGURE_ARGS += --enable-pcregrep-libz
CONFIGURE_ARGS += --enable-pcregrep-libbz2
CONFIGURE_ARGS += --enable-pcretest-libreadline

# No JIT for Sparc, may try for x86 at some later time
#CONFIGURE_ARGS += --enable-jit

include gar/category.mk

# The testcases need 'diff -u' which Solaris 8 diff does not have,
# but we need Solaris strip, otherwise pcregrep is broken and 200m in size...
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)
