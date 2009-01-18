GARNAME = botnet
GARVERSION = 0.8
CATEGORIES = net

DESCRIPTION = Botnet detector plugin for SpamAssassin
define BLURB
	Botnet looks for possible botnet sources of email by checking
	various DNS values that indicate things such as other ISP's clients or
	workstations, or misconfigured DNS settings that are more likely to
	happen with client or workstation addresses than servers.
endef

MASTER_SITES = http://people.ucsc.edu/~jrudd/spamassassin/
DISTFILES  = Botnet-$(GARVERSION).tar
DISTFILES += $(call admfiles,CSWbotnet,)

SPKG_DESC_CSWspamassassin = mail filter with a wide range of tests
REQUIRED_PKGS = CSWspamassassin CSWcswclassutils

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar

SPKG_CLASSES = none cswcpsampleconf

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

#ENABLE_CHECK = 0

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/Botnet.cf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } { print }'

include gar/category.mk

WORKSRC = $(WORKDIR)
MAINFILES =  Botnet.pm Botnet.cf.CSW
DOCFILES = Botnet.api.txt Botnet.credits.txt Botnet.txt Botnet.variants.txt INSTALL

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@mv $(WORKSRC)/Botnet.cf $(WORKSRC)/Botnet.cf.CSW
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/Botnet.pl $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(sysconfdir)/mail/spamassassin
	@$(foreach FILE, $(MAINFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)$(sysconfdir)/mail/spamassassin ;)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach FILE, $(DOCFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)$(docdir)/$(GARNAME) ;)
	@cp -r $(WORKSRC)/COPYING $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE
	@$(MAKECOOKIE)
