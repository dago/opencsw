# $Id$
NAME = erlang
VERSION = R16B
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = A functional programming language from Ericsson
define BLURB
  Erlang is a small concurrent functional programming language
  developed by Ericsson. It is being used by Ericsson as a systems
  programming language for large concurrent distributed systems.
endef

VENDOR_URL = http://www.erlang.org/
MASTER_SITES = http://www.erlang.org/download/
DISTNAME = otp_src_$(VERSION)
DISTFILES  = $(PATCHFILES += 0001-Fix-main-signature.patch

PATCHFILES += 0001-Do-not-use-ssl-standard-locations.patch

# TBD:
# - Solaris 10 x86 needs a libdlpi.so symlink:
#     ln -s /lib/libdlpi.so.1 /lib/libdlpi.so
# Solaris patches needed 145923-03 (sparc) or 145924-03 (i386)$(DISTNAME).tar.gz

# We want DTrace
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = EPLICENCE

PACKAGES += CSWerlang
SPKG_DESC_CSWerlang = A functional programming language from Ericsson
RUNTIME_DEP_PKGlibncurses5
RUNTIME_DEP_PKGS_CSWerlang += CSWlibssl1-0-0 +# These are just examples
CHECKPKG_OVERRIDES_CSWerlang += file-with-bad-content

# This is just for the emacs style
CHECKPKG_OVERRIDES_CSWerlang += missing-dependency|CSWemacs-common
 # Don't care for now
CHECKPKG_OVERRIDES_CSWerlang += no-direct-binding|/opt/csw/lib/amd64/erlang/lib/runtime_tools-1.8.10/priv/lib/trace_ip_drv.so|is|not|directly|bound|to|soname|libdlpi.so.1
CHECKPKG_OVERRIDES_CSWerlang += no-direct-binding|/opt/csw/lib/amd64/erlang/lib/runtime_tools-1.8.10/priv/lib/trace_ip_drv.so|is|not|directly|bound|to|soname|libsendfile.so.1 += CSWlibncurses5

PACKAGES += CSWerlang-dev
SPKG_DESC_CSWerlang-dev = Ericson Erlang OTP library sources and headers
PKGFILES.*/src/.*
PKGFILES_CSWerlang-dev += .*/include/.*
PKGFILES_CSWerlang-dev += $(mandir)/man3erl/.*
OBSOLETED_BY_CSWerlang-dev = CSWerlangdevel
CATALOGNAME_CSWerlangdevel = erlang_devel_stub

CHECKPKG_OVERRIDES_CSWerlang-dev += file-with-bad-content erlang_devel_stub

PACKAGES += CSWerlang-doc
SPKG_DESC_CSWerlang-doc = Erlang manual and documentation
# This is empty right now, make sure docs are build later...
PKGFILES.*/doc/.*
PKGFILES_CSWerlang-doc += .*/infooc += $(docdir)/.*
OBSOLETED_BY_CSWerlang-doc = CSWerlangdoc
CATALOGNAME_CSWerlangdoc = erlang_doc_stub

G# $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))

BUILD64 = 1
ISAEXEC = 1

# [8:23pm] aurora: LDFLAGS="-L/opt/csw/lib/64" CFLAGS="-I/opt/csw/include" CXXFLAGS="-I/opt/csw/include" AR=gar ./configure --with-ssl=/opt/csw --disable-dynamic-ssl-lib --enable-m64-build --with-odbc=/opt/csw --without-wxGARCOMPILER = GCC4

CONFIGURE_AR
CONFIGURE_ARGS += --with-ssl=$(prefix)
#CONFIGURE_ARGS += --disable-dynamic-ssl-lib

CONFIGURE_ARGS += --without-wx
#CONFIGURE_ARGS += --enable-threads
#CONFIGURE_ARGS += --enable-smp-support
#CONFIGURE_ARGS += --enable-kernel-poll
##CONFIGURE_ARGS += --enable-hipe
#CONFIGURE_ARGS += --disable-hipe
#CONFIGURE_ARGS += --with-dynamic-trace=dtrace
##  CONFIGURE_ARGS += --without-odbc

CONFIGURE_ARGS-32 += --enable-m32-build
CONFIGURE_ARGS-64 += --enable-m64-build
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# We need to override this or we pollute RUNPATH with lots of invalid dirs like /usr/local etc.
CONFIGURE_ARGS += std_ssl_locations=

EXTRA_CONFIGURE_ENV += AR=$(bindir)/gar

# On Solaris 10 i386 enabling hipe leads to 
#   Undefined                       first referenced
#    symbol                             in file
#   hipe_emulate_fpe                    obj/i386-pc-solaris2.10/opt/smp/hipe_x86_bifs.o
CONFIGURE_ARGS += --disable-hipe += --without-odbc

# There doesn't seem to be a testsuite
TEST_SCRIPTS =

#post-configure-modulated:
#	@echo " ==> disabling WxWidgets"
#	@touch $(WORKDIR)/otp_src_$(VERSION)/lib/wx/SKIP
#	@$(MAKECOOKIE)

includ
# The -m32 -march=pentium_pro disturbs ld which just takes -32
ARCHFLAGS_GCC4_pentium_pro :=
ARCHFLAGS_GCC4_amd64 :=

