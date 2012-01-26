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

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tgz
PATCHFILES = patch-Makefile.diff

SPKG_SOURCEURL = http://proxytunnel.sourceforge.net/

BUILD_DEP_PKGS = CSWossldevel
RUNTIME_DEP_PKGS = CSWosslrt

# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
