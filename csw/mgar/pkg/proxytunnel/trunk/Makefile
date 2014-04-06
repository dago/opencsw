NAME = proxytunnel
VERSION = 1.9.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Tunnels network connections through a HTTPS proxy
define BLURB
  ProxyTunnel is a program that connects stdin and stdout to a server somewhere
  on the network, through a standard HTTPS proxy. We mostly use it to tunnel 
  SSH sessions through HTTP(S) proxies, allowing us to do many things that 
  wouldn't be possible without ProxyTunnel.
endef

MASTER_SITES = $(SF_+= $(DISTNAME).tgz
DISTFILES += changelog.CSW
PATCHFILES = patch-Makefile.diff

VENDOR_URL = http://proxytunnel.sourceforge.net/

BUILD_DEP_PKGS += CSWlibssl-dev

PACKAGES += CSWproxytunnel
SPKG_DESC_CSWproxytunnel = Tunnels network connections through a HTTPS proxy
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWproxytunnel = CSWlibssl1-0-0

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS = 

EXTRA_CFLAGS += -I$(includedir)
EXTRA_LDFLAGS += -lnsl -lsocket_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -dWORKDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
