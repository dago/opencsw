GARNAME = postgrey
GARVERSION = 1.32
CATEGORIES = net

DESCRIPTION = Postfix policy server implementing greylisting
define BLURB
  Postfix policy server implementing greylisting
endef

MASTER_SITES = http://postgrey.schweikert.ch/pub/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWperl CSWpmiomultiplex CSWpmnetserver CSWbdb48 CSWpostfix
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

INITSMF = /etc/opt/csw/init.d/cswpostgrey
USERGROUP = /etc/opt/csw/pkg/CSWpostgrey/cswusergroup
SAMPLECONF = /etc/opt/csw/postfix/postgrey_whitelist_clients /etc/opt/csw/postfix/postgrey_whitelist_recipients

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWpostgrey.init $(DESTDIR)/etc/opt/csw/init.d/cswpostgrey
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(WORKSRC)/postgrey_whitelist_clients $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(WORKSRC)/postgrey_whitelist_recipients $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWpostgrey
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWpostgrey/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)$(sbindir)
	@ginstall -m 755 $(WORKSRC)/postgrey $(DESTDIR)$(sbindir)
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/Changes $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 $(WORKSRC)/policy-test $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 $(WORKSRC)/contrib/postgreyreport $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man1
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/$(GARNAME).1
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)
	@$(MAKECOOKIE)
