# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Build in unknown state, work in progress, please take over & verify
# ! Include init script
# ! Include default configuration
# * Use the shipped Makefile optimization flags
#
NAME = haproxy
VERSION = 1.4.18
CATEGORIES = apps

DESCRIPTION = Reliable, high performance TCP/HTTP load balancer
define BLURB
  HAProxy is a free, very fast and reliable solution offering high
  availability, load balancing, and proxying for TCP and HTTP-based
  applications. It is particularly suited for web sites crawling under
  very high loads while needing persistence or Layer7 processing.
  Supporting tens of thousands of connections is clearly realistic with
  todays hardware. Its mode of operation makes its integration into
  existing architectures very easy and riskless, while still offering the
  possibility not to expose fragile web servers to the Net.
endef

MASTER_SITES = http://haproxy.1wt.eu/download/1.4/src/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://haproxy.1wt.eu/

LICENSE = LICENSE

# Heavily optimized, supported for gcc, didn't dare to touch
GARCOMPILER = GCC4

BUILD64 = 1
ISAEXEC = 1
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = \
	TARGET=solaris \
	CC=$(CC) \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)"

INSTALL_ARGS = \
	PREFIX=$(prefix) \
	SBINDIR=$(sbindir) \
	DOCDIR=$(docdir)/$(NAME)

# Don't care for now, investigate later!
CHECKPKG_OVERRIDES_CSWhaproxy += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/haproxy.1
CHECKPKG_OVERRIDES_CSWhaproxy += file-with-bad-content|/usr/share|root/opt/csw/share/doc/haproxy/haproxy.1
CHECKPKG_OVERRIDES_CSWhaproxy += file-with-bad-content|/usr/share|root/opt/csw/share/doc/haproxy/examples/build.cfg
CHECKPKG_OVERRIDES_CSWhaproxy += file-with-bad-content|/usr/share|root/opt/csw/share/doc/haproxy/examples/haproxy.cfg
CHECKPKG_OVERRIDES_CSWhaproxy += file-with-bad-content|/usr/share|root/opt/csw/share/doc/haproxy/examples/haproxy-1.1.21-flx.1.pkg

include gar/category.mk

# Makefile contains references to install
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	mkdir -p $(DOCDEST)
	cp -r $(WORKSRC)/examples $(DOCDEST)
	cp -r $(WORKSRC)/doc/* $(DOCDEST)
	@$(MAKECOOKIE)
