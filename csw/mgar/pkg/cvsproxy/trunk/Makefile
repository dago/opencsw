NAME = cvsproxy
VERSION = 1.0.1
GARTYPE = v2

DESCRIPTION = Provides a CVS proxy
define BLURB
  Provides a CVS proxy
endef

MASTER_SITES = http://www.sra.co.jp/people/m-kasahr/cvsproxy/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.sra.co.jp/people/m-kasahr/cvsproxy
RUNTIME_DEP_PKGS = CSWtcpwrap

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

ETCSERVICES = /opt/csw/etc/pkg/$(NAME)/services
INETDCONF = /opt/csw/etc/pkg/$(NAME)/inetd.conf

# We use tcpd from TCPwrappers, this is ok.
CHECKPKG_OVERRIDES_CSWcvsproxy += surplus-dependency|CSWtcpwrap

include gar/category.mk

post-install-modulated:
	@echo "==> Post-install fixes"
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@cp $(FILEDIR)/services $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@cp $(FILEDIR)/inetd.conf $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@$(MAKECOOKIE)
