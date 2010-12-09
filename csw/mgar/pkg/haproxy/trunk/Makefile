# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Build in unknown state, work in progress, please take over & verify
# ! Include init script
# ! Include default configuration
# * Use the shipped Makefile optimization flags
#
GARNAME = haproxy
GARVERSION = 1.4.1
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

VENDOR_URL   = http://haproxy.1wt.eu/
MASTER_SITES = http://haproxy.1wt.eu/download/1.4/src/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = $(VENDOR_URL)

# Heavily optimized, supported for gcc, didn't dare to touch
GARCOMPILER = GCC4

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = \
	TARGET=solaris \
	CC=$(CC) \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)"

INSTALL_ARGS = \
	PREFIX=$(prefix) \
	DOCDIR=$(docdir)/$(GARNAME)

include gar/category.mk

# Makefile contains references to install
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	mkdir -p $(DOCDEST)
	cp -r $(WORKSRC)/examples $(DOCDEST)
	cp -r $(WORKSRC)/doc/* $(DOCDEST)
	@$(MAKECOOKIE)
