# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Build in unknown state, work in progress, please take over & verify
# ! Include init script
# ! Include default configuration
# * Use the shipped Makefile optimization flags
# * For some obscure reason this link is missing on unstable10x:
#     lrwxrwxrwx   1 root     root          13 Dec 28 23:53 /usr/lib/64/libcrypt.so -> libcrypt_d.so
#   I added this link manually for now, investigate later!
#
NAME = haproxy
VERSION = 1.4.26
CATEGORIES = apps
GARTYPE = v2

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

VEwww.haproxy.org

LICENSE = LICENSE

# Heavily optimized, supported for gcc, didn't dare to touch
GARCOMPILER = GCC4

BUILD64 = 1
ISAEXEC = 1

# There is no configure script, configuration is passed directly to the Makefile
CONFIGURE_SCRIPTS =

# There is no testsuiteONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = \
	TARGET=solaris \
	CC=$(CC) \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)"

INSTALL_ARGS = \
	PREFIX=$(prefix) \
	SBINDIR=$(sbindir) \
	DOCDIR=$# We need GNU install as 'install'
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk

post-install: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-install-modulated:
	mkdir -p $(DOCDEST)
	cp -r $(WORKSRC)/examples $(DOCDEST)
	cp -r $(WORKSRC)/doc/* $(DOCDEST