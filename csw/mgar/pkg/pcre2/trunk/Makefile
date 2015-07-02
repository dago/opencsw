NAME = pcre2
VERSION = 10.20
GARTYPE = v2

DESCRIPTION = Perl-compatible regular expression toolsession API.
endef

MASTER_SITES = ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
DISTFILES  = $(D#ISTNAME).tar.bz2
PATCHFILES = 0001-Allow-norunpath-for-libtool.patch

VENDOR_URL = http://www.pcre.org

P2
SPKG_DESC_CSWpcre2 = Perl-compatible regular expression tools v2
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibpcre2-8-0
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibpcre2-16-0
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibpcre2-32-0
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWpcre2 += CSWlibpcre2posix0

PACKAGES += CSWlibpcre2-dev
SPKG_DESC_CSWlibpcre2G_DESC_CSWlibpcre-dev = Development files for libpcre.so.1, libpcre16.so.0, libpcrecpp.so.0 and libpcreposix.so.0
RUNTIME_DE2-dev += CSWlibpcre2-8-0
RUNTIME_DEP_PKGS_CSWlibpcre2-dev += CSWlibpcre2-16-0
RUNTIME_DEP_PKGS_CSWlibpcre2-dev += CSWlibpcre2-32-0
RUNTIME_DEP_PKGS_CSWlibpcre2-dev += CSWlibpcre2posix0
PKGFILES_CSWlibpcre2-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpcre2-dev += $(docdir)/.*

# We don't want to depend on pcre2
CHECKPKG_OVERRIDES_CSWlibpcre2-dev += missing-dependency|CSWpcre2

PACKAGES += CSWlibpcre2-8-0
SPKG_DESC_CSWlibpcre2-8-0 = Perl-compatible regular expression tools, libpcre2-8.so.0
PKGFILES_CSWlibpcre2-8-0 = $(call pkgfiles_lib,libpcre2-8.so.0)

PACKAGES += CSWlibpcre2-16-0
SPKG_DESC_CSWlibpcre2-16-0 = Perl-compatible regular expression tools, libpcre2-16.so.0
PKGFILES_CSWlibpcre2-16-0 = $(call pkgfiles_lib,libpcre2-16.so.0)

PACKAGES += CSWlibpcre2-32-0
SPKG_DESC_CSWlibpcre2-32-0 = Perl-compatible regular expression tools, libpcre2-32.so.0
PKGFILES_CSWlibpcre2-32-0 = $(call pkgfiles_lib,libpcre2-32.so.0)

PACKAGES += CSWlibpcre2posix0
SPKG_DESC_CSWlibpcre2posix0 += Perl-compatible regular expression tools, libpcre2-posix.so.0
PKGFILES_CSWlibpcre2posix0 += $(call pkgfiles_lib,libpcre2-posix.so.0)
RUNTIME_DEP_PKGS_CSWlibpcre2posix0 += CSWlibpcre2-8-0 d# Older compiler like Sun Studio 12 behave differently on -Wl,-i... and -Qoption ld -i...
# This leads to configure detecting something works which later on does not work.
# Newer compilers behave consistently.
# See also http://bugs.exim.org/show_bug.cgi?id=1278
GARCOMPILER = SOS12U= doc/pcresample.3

BUILD64_LIBS_ONLY = 1

EXTRA_LINKER_FLAGS = -norunpath+= $(DIRPATHS)
CONFIGURE_ARGS += --enable-pcre2grep-libz
CONFIGURE_ARGS += --enable-pcre2grep-libbz2

# Prefer libreadline over libedit
CONFIGURE_ARGS += --enable-pcre2test-libreadline

CONFIGURE_ARGS += --enable-pcre2-8
CONFIGURE_ARGS += --enable-pcre2-16
CONFIGURE_ARGS += --enable-pcre2-32

# The stack on Solaris is rather limited, disable stack allocation
CONFIGURE_ARGS += --disable-stack-for-recursion

# No JIT for Sparc 64 bit
JIT-i386-32 = --enable-jit
JIT-i386-64 = --enable-jit
JIT-sparc-32 = --enable-jit
JIT-sparc-64 =
CONFIGURE_ARGS += $(JIT-$(GARCH)-$(MEMORYMODEL))

include gar/category.mk
