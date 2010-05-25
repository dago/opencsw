GARNAME = policyd-weight
GARVERSION = 0.1.14
CATEGORIES = net

DESCRIPTION = Policy daemon for the Postfix MTA (2.1 and later)
define BLURB
  Policy daemon for the Postfix MTA (2.1 and later) intended to eliminate
  forged envelope senders and HELOs (i.e. in bogus mails)
endef

MASTER_SITES = http://www.policyd-weight.org/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

ARCHALL = 1

CATALOGNAME = policydweight

RUNTIME_DEP_PKGS = CSWperl CSWpmnetdns

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

INITSMF = /opt/csw/etc/init.d/csw$(GARNAME)
USERGROUP = /etc/opt/csw/pkg/CSW$(GARNAME)/cswusergroup
SAMPLECONF  = /etc/opt/csw/postfix/policyd-weight.conf

CHECKPKG_OVERRIDES += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES += surplus-dependency|CSWpmnetdns

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 755 $(FILEDIR)/$(GARNAME).init $(DESTDIR)/opt/csw/etc/init.d/csw$(GARNAME)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(WORKSRC)/policyd-weight.conf.sample $(DESTDIR)/etc/opt/csw/postfix/policyd-weight.conf
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(GARNAME)
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(GARNAME)/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)$(sbindir)
	@ginstall -m 755 $(WORKSRC)/$(GARNAME) $(DESTDIR)$(sbindir)
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/changes.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/documentation.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 $(WORKSRC)/todo.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man5
	@ginstall -m 755 $(WORKSRC)/man/man5/policyd-weight.conf.5 $(DESTDIR)$(mandir)/man5
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 $(WORKSRC)/man/man8/policyd-weight.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)
