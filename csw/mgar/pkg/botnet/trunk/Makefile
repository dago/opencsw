NAME = botnet
VERSION = 0.8
GARTYPE = v2

DESCRIPTION = Botnet detector plugin for SpamAssassin
define BLURB
	Botnet looks for possible botnet sources of email by checking
	various DNS values that indicate things such as other ISP's clients or
	workstations, or misconfigured DNS settings that are more likely to
	happen with client or workstation addresses than servers.
endef

MASTER_SITES = http://people.ucsc.edu/~jrudd/spamassassin/
DISTFILES  = Botnet-$(VERSION).tar

RUNTIME_DEP_PKGS = CSWspamassassin CSWperl

ARCHALL	= 1

UFILES_REGEX = -(\d+(?:\.\d+)*).tar

SAMPLECONF = /etc/opt/csw/spamassassin/Botnet.cf

MIGRATE_FILES = Botnet.cf
MIGRATE_SOURCE_DIR = /opt/csw/etc/spamassassin
MIGRATE_DEST_DIR = /etc/opt/csw/spamassassin

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
MAINFILES =  Botnet.pm Botnet.cf
DOCFILES = Botnet.api.txt Botnet.credits.txt Botnet.txt Botnet.variants.txt INSTALL

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/Botnet.pl $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)/etc/opt/csw/spamassassin
	@$(foreach FILE, $(MAINFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)/etc/opt/csw/spamassassin ;)
	@chmod 644 $(DESTDIR)/etc/opt/csw/spamassassin/Botnet.cf
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach FILE, $(DOCFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)$(docdir)/$(NAME) ;)
	@$(MAKECOOKIE)
