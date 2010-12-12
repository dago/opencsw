NAME = cvsproxy
VERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = Provides a CVS proxy
define BLURB
  Provides a CVS proxy
endef

MASTER_SITES = http://www.sra.co.jp/people/m-kasahr/cvsproxy/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWtcpwrap
SPKG_SOURCEURL = http://www.sra.co.jp/people/m-kasahr/cvsproxy

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

ETCSERVICES = /opt/csw/etc/pkg/$(NAME)/services
INETDCONF = /opt/csw/etc/pkg/$(NAME)/inetd.conf

include gar/category.mk

post-install-modulated:
	@echo "==> Post-install fixes"
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(NAME)
	@mv $(DESTDIR)/opt/csw/libexec/cvsproxy $(DESTDIR)/opt/csw/libexec/cvsproxy.tmp
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/libexec/$(NAME)
	@mv $(DESTDIR)/opt/csw/libexec/cvsproxy.tmp $(DESTDIR)/opt/csw/libexec/$(NAME)/cvsproxy
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@cp $(FILEDIR)/services $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@cp $(FILEDIR)/inetd.conf $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@$(MAKECOOKIE)
