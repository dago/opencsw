# TODO
# * Add init script
GARNAME = snmptt
GARVERSION = 1.3
CATEGORIES = apps

DESCRIPTION = SNMP trap handler for use with the snmptrad program
define BLURB
endef

VENDOR_URL   = http://snmptt.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTNAME     = $(GARNAME)_$(GARVERSION)
DISTFILES    = $(GARNAME)_$(GARVERSION).tgz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1
RUNTIME_DEP_PKGS = CSWperl CSWpmcfginifls

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SAMPLECONF = /etc/opt/csw/snmptt.ini

CHECKPKG_OVERRIDES_CSWsnmptt += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWsnmptt += surplus-dependency|CSWpmcfginifls

include gar/category.mk

install-custom: BIN=snmpttconvertmib
install-custom: SBIN=snmptt snmptthandler
install-custom: DOCS=ChangeLog
install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
install-custom:
	ginstall -d $(DESTDIR)$(bindir) 
	ginstall -d $(DESTDIR)$(sbindir) 
	ginstall -d $(DESTDIR)/etc/opt/csw/
	ginstall -d $(DESTDIR)/var/opt/csw/log/snmptt
	ginstall -d $(DESTDIR)/var/opt/csw/spool/snmptt/
	ginstall -d $(DOCDEST) $(DOCDEST)/examples

	ginstall -m 755 $(addprefix $(WORKSRC)/, $(BIN)) $(DESTDIR)$(bindir)
	ginstall -m 755 $(addprefix $(WORKSRC)/,$(SBIN)) $(DESTDIR)$(sbindir)
	gsed -i 's,/usr/bin/perl,/opt/csw/bin/perl,' $(DESTDIR)$(bindir)/*
	gsed -i 's,/usr/bin/perl,/opt/csw/bin/perl,' $(DESTDIR)$(sbindir)/*

	cp $(WORKSRC)/snmptt.ini $(DESTDIR)/etc/opt/csw/snmptt.ini
	gsed \
		-e 's,/var/,/var/opt/csw/,' \
		-e 's,/var/opt/csw/run/snmptt.pid,/var/run/cswsnmptt.pid,' \
		$(DESTDIR)/etc/opt/csw/snmptt.ini

	cp $(WORKSRC)/examples/* $(WORKSRC)/sample-* $(DOCDEST)/examples
	cp $(WORKSRC)/docs/* $(DOCDEST)
	@$(MAKECOOKIE)
