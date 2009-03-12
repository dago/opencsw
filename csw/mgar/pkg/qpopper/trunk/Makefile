GARNAME = qpopper
GARVERSION = 4.0.16
WORKSRC = $(WORKDIR)/$(GARNAME)$(GARVERSION)
CATEGORIES = apps

DESCRIPTION = the most widely-used POP3 server for Unix
define BLURB
  Qpopper supports the widely used POP3 protocol for downloading Internet
  e-mail used by many popular e-mail clients. Qpopper does not include a
  message transfer agent or SMTP support and normally works with standard
  UNIX mail transfer agents such as sendmail or smail.
endef

MASTER_SITES = ftp://ftp.qualcomm.com/eudora/servers/unix/popper/
DISTFILES  = $(GARNAME)$(GARVERSION).tar.gz
DISTFILES += README.CSW

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWqpopper
CATALOGNAME_CSWqpopper = qpopper
SPKG_DESC_CSWqpopper = $(DESCRIPTION)

SPKG_SOURCEURL = http://www.eudora.com/qpopper

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Install for $(GARNAME) (custom)"
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(sbindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@( cd $(WORKSRC) ; \
	   cp License.txt $(DESTDIR)$(docdir)/$(GARNAME)/license ; \
	   cp popper/popper $(DESTDIR)$(sbindir) ; \
	   cp man/* $(DESTDIR)$(mandir)/man8 )
	@cp $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
