GARNAME = nsca
GARVERSION = 2.7.2
CATEGORIES = apps

DESCRIPTION = passive checks for nagios
define BLURB
  NSCA allows you to integrate passive alerts and checks from remote machines and applications with Nagios. Useful for processing security alerts, as well as redundant and distributed Nagios setups.
endef

MASTER_SITES = http://mesh.dl.sourceforge.net/sourceforge/nagios/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnsca, prototype checkinstall preinstall )
DISTFILES += $(call admfiles,CSWsendnsca, preinstall )
DISTFILES += nsca nsca.xml svc-nsca

PATCHFILES += submit_check_results.diff

REQUIRED_PKGS_CSWnsca     = CSWlibmcrypt CSWlibtoolrt CSWnagios
REQUIRED_PKGS_CSWsendnsca = CSWlibmcrypt CSWlibtoolrt CSWnagios

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-nsca-port=5667

BUILD_TARGETS = nsca

SKIPTEST = 1

include gar/category.mk

NAGIOSBINDIR=$(prefix)/nagios/bin
NAGIOSCFGDIR=$(prefix)/nagios/etc
NSCADOCDIR=$(prefix)/share/doc/nsca
SENDNSCADOCDIR=$(prefix)/share/doc/send_nsca
CFGDIR=$(prefix)/etc

post-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(prefix)/nagios/bin
	ginstall -d $(DESTDIR)$(prefix)/nagios/etc
	ginstall -m 755 -d $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 755 $(WORKSRC)/src/nsca $(DESTDIR)$(NAGIOSBINDIR)
	ginstall -m 600 $(WORKSRC)/sample-config/nsca.cfg $(DESTDIR)$(NAGIOSCFGDIR)/nsca.cfg
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 755 $(WORKSRC)/src/send_nsca $(DESTDIR)$(BINDIR)
	ginstall -m 755 -d $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 755 -d $(DESTDIR)$(CFGDIR)
	ginstall -m 755 $(WORKSRC)/src/submit_check_result-sample $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 600 $(WORKSRC)/sample-config/send_nsca.cfg $(DESTDIR)$(CFGDIR)/send_nsca.cfg
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(SENDNSCADOCDIR)
	@$(MAKECOOKIE)
