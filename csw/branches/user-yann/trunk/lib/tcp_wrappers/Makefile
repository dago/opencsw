GARNAME = tcp_wrappers
GARVERSION = 7.6
CATEGORIES = lib

SPKG_PKGNAME = CSWtcpwrap
SPKG_BITNAME = tcpwrappers

DESCRIPTION = Socket Wrappers
define BLURB
  Socket Wrappers is an improved version of tcp_wrappers by Wietse Venema.
endef

MASTER_SITES = http://www.web-insights.net/$(GARNAME)/
DISTNAME = $(GARNAME)_$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz
WORKSRC = $(WORKDIR)/$(DISTNAME)

#BUILD_ARGS  = REAL_DAEMON_DIR=/foo/bar
BUILD_ARGS += STYLE=-DPROCESS_OPTIONS

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# No test suite
ENABLE_TEST = 0

include ../category.mk

build-custom:
	@$(MAKE) -C $(WORKSRC) $(BUILD_ARGS) sunos5

BINFILES = $(addprefix $(WORKSRC)/,safe_finger tcpd tcpdchk tcpdmatch try-from)
INCFILES = $(addprefix $(WORKSRC)/,tcpd.h)
LIBFILES = $(addprefix $(WORKSRC)/,libwrap.a)

install-custom:
	@echo " => Installing $(GARNAME)"
	@install -v -m 555 $(BINFILES) $(DESTDIR)$(bindir)
	@install -v -m 444 $(INCFILES) $(DESTDIR)$(includedir)
	@install -v -m 444 $(LIBFILES) $(DESTDIR)$(libdir)
	
