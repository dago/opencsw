NAME = qpopper
VERSION = 4.1.0
WORKSRC = $(WORKDIR)/$(NAME)$(VERSION)
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The most widely-used POP3 server for Unix
define BLURB
  Qpopper supports the widely used POP3 protocol for downloading Internet
  e-mail used by many popular e-mail clients. Qpopper does not include a
  message transfer agent or SMTP support and normally works with standard
  UNIX mail transfer agents such as sendmail or smail.
endef

MASTER_SITES = ftp://ftp.qualcomm.com/eudora/servers/unix/popper/
DISTFILES  = $(NAME)$(VERSION).tar.gz
DISTFILES += README.CSW

PACKAGES = CSWqpopper
CATALOGNAME_CSWqpopper = qpopper
SPKG_DESC_CSWqpopper = $(DESCRIPTION)

INETDCONF = /etc/opt/csw/pkg/CSWqpopper/inetd.conf

SPKG_SOURCEURL = http://www.eudora.com/qpopper

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-specialauth

TEST_SCRIPTS    =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWqpopper += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/popper.8

include gar/category.mk

install-custom:
	@echo " ==> Install for $(NAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	@cp $(FILEDIR)/inetd.conf $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(sbindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@( cd $(WORKSRC) ; \
	   cp License.txt $(DESTDIR)$(docdir)/$(NAME)/license ; \
	   cp popper/popper $(DESTDIR)$(sbindir) ; \
	   cp man/* $(DESTDIR)$(mandir)/man8 )
	@cp $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
