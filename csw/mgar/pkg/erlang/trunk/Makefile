# $Id$
NAME = erlang
VERSION = R14B03
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
DISTFILES  = $(DISTNAME).tar.gz

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

GARCOMPILER = GCC4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-smp-support
CONFIGURE_ARGS += --enable-kernel-poll
CONFIGURE_ARGS += --enable-hipe
#  CONFIGURE_ARGS += --without-odbc

# There doesn't seem to be a testsuite
TEST_SCRIPTS =

#post-configure-modulated:
#	@echo " ==> disabling WxWidgets"
#	@touch $(WORKDIR)/otp_src_$(VERSION)/lib/wx/SKIP
#	@$(MAKECOOKIE)

include gar/category.mk
