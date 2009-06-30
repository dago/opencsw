GARNAME = dnswalk
GARVERSION = 2.0.2
CATEGORIES = utils

DESCRIPTION = dnswalk is a DNS debugger
define BLURB
  dnswalk is a DNS debugger. It performs zone transfers of specified domains, and checks
  the database in numerous ways for internal consistency, as well as accuracy. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWdnswalk
REQUIRED_PKGS = CSWperl CSWpmnetdns
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
UPSTREAM_USE_SF = 1
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=1103

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

BINLIST = dnswalk do-dnswalk makereports sendreports
DOCLIST = CHANGES README TODO dnswalk.errors rfc1912.txt

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@$(foreach BIN,$(BINLIST),cp $(WORKDIR)/$(BIN) $(DESTDIR)$(bindir);)
	@( cd $(DESTDIR)$(bindir) ; \
	   sed 's|^#!/usr/contrib|#!/opt/csw|' dnswalk > dnswalk.sed ; \
	   mv dnswalk.sed dnswalk )
	@( cd $(DESTDIR)$(bindir) ; \
	   sed 's|^#!/usr/contrib|#!/opt/csw|' makereports > makereports.sed ; \
	   mv makereports.sed makereports )
	@cp $(WORKDIR)/$(GARNAME).1 $(DESTDIR)$(mandir)/man1
	@$(foreach DOC,$(DOCLIST),cp $(WORKDIR)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	@$(MAKECOOKIE)
