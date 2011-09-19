# $Id$
NAME = erlang
VERSION = R14B03
CATEGORIES = lang

DESCRIPTION = A functional programming language from Ericsson
define BLURB
  Erlang is a small concurrent functional programming language
  developed by Ericsson. It is being used by Ericsson as a systems
  programming language for large concurrent distributed systems.
endef

VENDOR_URL = http://www.erlang.org/
MASTER_SITES = http://www.erlang.org/download/
DISTFILES  = otp_src_$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

WORKSRC = $(WORKDIR)/otp_src_$(VERSION)

GARCOMPILER = GCC3

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-smp-support
CONFIGURE_ARGS += --enable-kernel-poll
CONFIGURE_ARGS += --enable-hipe
CONFIGURE_ARGS += --without-odbc

SKIPTEST = 1

RUNTIME_DEP_PKGS_CSWerlang += CSWemacscommon
RUNTIME_DEP_PKGS_CSWerlang += CSWlibncurses5

post-configure-modulated:
	@echo " ==> disabling WxWidgets"
	@touch $(WORKDIR)/otp_src_$(VERSION)/lib/wx/SKIP
	@$(MAKECOOKIE)

include gar/category.mk
