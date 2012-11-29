# $Id$
NAME = erlang
VERSION = R15B02
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
DISTFILES  = $(DITBD:
# - Solaris 10 x86 needs a libdlpi.so symlink:
#     ln -s /lib/libdlpi.so.1 /lib/libdlpi.so$(DISTNAME).tar.gz

# We want DTrace
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = EPLICENCE

PACKAGES += CSWerlang
SPKG_DESC_CSWerlang = A functional programming language from Ericsson
RUNTIME_DEP_PKGS_CSWerlang += CSWemacscommon
RUNTIME_DEP_PKGS_CSWerlang += CSWlibncurses5

PACKAGES += CSWerlang-dev
SPKG_DESC_CSWerlang-dev = Ericson Erlang OTP library sources and headers
PKGFILES_CSWerlang-dev += $(PKGFILES_DEVEL)
OBSOLETED_BY_CSWerlang-dev = CSWerlangdevel
CATALOGNAME_CSWerlangdevel = erlang_devel_stub

PACKAGES += CSWerlang-doc
SPKG_DESC_CSWerlang-doc = Erlang manual and documentation
# This is empty right now, make sure docs are build later...
PKGFILES_CSWerlang-doc += $(docdir)/.*
OBSOLETED_BY_CSWerlang-doc = CSWerlangdoc
CATALOGNAME_CSWerlangdoc = erlang_doc_stub

G# $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))

BUILD64 = 1

# [8:23pm] aurora: LDFLAGS="-L/opt/csw/lib/64" CFLAGS="-I/opt/csw/include" CXXFLAGS="-I/opt/csw/include" AR=gar ./configure --with-ssl=/opt/csw --disable-dynamic-ssl-lib --enable-m64-build --with-odbc=/opt/csw --without-wxGARCOMPILER = GCC4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --w  CONFIGURE_ARGS += --disable-dynamic-ssl-lib
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

