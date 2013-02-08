NAME = cvsproxy
VERSION = 1.0.1

DESCRIPTION = Provides a CVS proxy

MASTER_SITES = http://www.sra.co.jp/people/m-kasahr/cvsproxy/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.sra.co.jp/people/m-kasahr/cvsproxy

ETCSERVICES = /opt/csw/etc/pkg/$(NAME)/services
INETDCONF = /opt/csw/etc/pkg/$(NAME)/inetd.conf

include gar/category.mk

post-install-modulated:
	@echo "==> Post-install fixes"
	ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	cp $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	cp $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(NAME)
	cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(NAME)
	ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	cp $(FILEDIR)/services $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	cp $(FILEDIR)/inetd.conf $(DESTDIR)/opt/csw/etc/pkg/$(NAME)
	@$(MAKECOOKIE)
