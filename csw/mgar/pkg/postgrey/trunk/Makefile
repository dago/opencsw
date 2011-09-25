NAME       = postgrey
VERSION    = 1.34
CATEGORIES = net

DESCRIPTION = Postfix policy server implementing greylisting
define BLURB
  Postfix policy server implementing greylisting
endef

MASTER_SITES = http://postgrey.schweikert.ch/pub/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS  = CSWperl
RUNTIME_DEP_PKGS += CSWpmiomultiplex
RUNTIME_DEP_PKGS += CSWpmnetserver
RUNTIME_DEP_PKGS += CSWpostfix
RUNTIME_DEP_PKGS += CSWpmberkeleydb

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

INITSMF     = /etc/opt/csw/init.d/cswpostgrey
USERGROUP   = /etc/opt/csw/pkg/CSWpostgrey/cswusergroup
SAMPLECONF  = /etc/opt/csw/postfix/postgrey_whitelist_clients /etc/opt/csw/postfix/postgrey_whitelist_recipients
SAMPLECONF += /etc/opt/csw/postgrey

PATCHFILES = postgrey.p

CHECKPKG_OVERRIDES_CSWpostgrey += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWpostgrey += surplus-dependency|CSWpmnetserver
CHECKPKG_OVERRIDES_CSWpostgrey += surplus-dependency|CSWpmiomultiplex
CHECKPKG_OVERRIDES_CSWpostgrey += surplus-dependency|CSWpmberkeleydb

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWpostgrey.init $(DESTDIR)/etc/opt/csw/init.d/cswpostgrey
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(WORKSRC)/postgrey_whitelist_clients $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(WORKSRC)/postgrey_whitelist_recipients $(DESTDIR)/etc/opt/csw/postfix
	@ginstall -m 644 $(FILEDIR)/postgrey $(DESTDIR)/etc/opt/csw/
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWpostgrey
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWpostgrey/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)$(sbindir)
	@ginstall -m 755 $(WORKSRC)/postgrey $(DESTDIR)$(sbindir)
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/Changes $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 755 $(WORKSRC)/policy-test $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 755 $(WORKSRC)/contrib/postgreyreport $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man1
	@pod2man --section=1 $(WORKSRC)/$(NAME) > $(DESTDIR)$(mandir)/man1/$(NAME).1
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(NAME)
	@$(MAKECOOKIE)
