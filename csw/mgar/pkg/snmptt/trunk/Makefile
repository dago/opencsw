# TODO
# * Add init script
NAME = snmptt
VERSION = 1.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = SNMP trap handler for use with the snmptrad program
define BLURB
endef

VENDOR_URL   = http://snmptt.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTNAME     = $(NAME)_$(VERSION)
DISTFILES    = $(NAME)_$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1
RUNTIME_DEP_PKGS = CSWperl CSWpmcfginifls

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SAMPLECONF = /etc/opt/csw/snmptt.ini /etc/opt/csw/snmptt.conf

CHECKPKG_OVERRIDES_CSWsnmptt += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWsnmptt += surplus-dependency|CSWpmcfginifls

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

include gar/category.mk

install-custom: BIN=snmpttconvertmib
install-custom: SBIN=snmptt snmptthandler
install-custom: DOCS=ChangeLog
install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom:
	ginstall -d $(DESTDIR)$(bindir) 
	ginstall -d $(DESTDIR)$(sbindir) 
	ginstall -d $(DESTDIR)$(sysconfdir)/snmp
	ginstall -d $(DESTDIR)$(localstatedir)/log/snmptt
	ginstall -d $(DESTDIR)$(localstatedir)/spool/snmptt/

	ginstall -m 755 $(addprefix $(WORKSRC)/, $(BIN)) $(DESTDIR)$(bindir)
	ginstall -m 755 $(addprefix $(WORKSRC)/,$(SBIN)) $(DESTDIR)$(sbindir)
	gsed -i \
		-e 's,/usr/bin/perl,/opt/csw/bin/perl,' \
		-e 's,/etc/snmp/,$(sysconfdir)/snmp/,' \
		$(DESTDIR)$(bindir)/* $(DESTDIR)$(sbindir)/*

	cp $(WORKSRC)/snmptt.ini $(DESTDIR)$(sysconfdir)/snmp/snmptt.ini
	gsed -i \
		-e 's,/etc/snmp/,/etc/opt/csw/snmp/,' \
		-e 's,/var/,/var/opt/csw/,' \
		-e 's,/var/opt/csw/run/snmptt.pid,/var/run/cswsnmptt.pid,' \
		$(DESTDIR)$(sysconfdir)/snmp/snmptt.ini
	cp $(WORKSRC)/examples/snmptt.conf.generic \
		$(DESTDIR)$(sysconfdir)/snmp/snmptt.conf

	cp $(WORKSRC)/docs/* $(DOCDEST)
	@$(MAKECOOKIE)
