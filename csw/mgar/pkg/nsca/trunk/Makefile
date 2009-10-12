GARNAME = nsca
GARVERSION = 2.7.2
CATEGORIES = apps

SPKG_DESC_CSWnsca = nagios service check acceptor
SPKG_DESC_CSWsendnsca = sends check results to nsca daemon

define BLURB
  NSCA allows you to integrate passive alerts and checks from remote machines and applications with Nagios. Useful for processing security alerts, as well as redundant and distributed Nagios setups.
endef

MASTER_SITES = http://mesh.dl.sourceforge.net/sourceforge/nagios/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

#
## Distfiles for CSWnsca
#

DISTFILES += CSWnsca.prototype CSWnsca.preinstall
DISTFILES += cswnsca CSWnsca.cswusergroup

#
## Distfiles for CSWsendnsca
#

DISTFILES += CSWsendnsca.prototype CSWsendnsca.preinstall
DISTFILES += CSWsendnsca.cswusergroup

PATCHFILES += submit_check_results.diff

PACKAGES = CSWnsca CSWsendnsca
CATALOGNAME_CSWnsca = nsca
CATALOGNAME_CSWsendnsca = send_nsca

REQUIRED_PKGS_CSWnsca     = CSWlibmcrypt CSWlibtoolrt CSWcswclassutils
REQUIRED_PKGS_CSWsendnsca = CSWlibmcrypt CSWlibtoolrt CSWcswclassutils

SPKG_CLASSES_CSWnsca = none cswusergroup cswpreserveconf cswinitsmf
SPKG_CLASSES_CSWsendnsca = none cswusergroup cswpreserveconf

NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-nsca-port=5667
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/nagios

BUILD_TARGETS = nsca

SKIPTEST = 1

include gar/category.mk

BINDIR=$(prefix)/bin
NAGIOSBINDIR=$(prefix)/nagios/bin
NAGIOSCFGDIR=/etc$(prefix)/nagios
NSCADOCDIR=$(prefix)/share/doc/nsca
SENDNSCADOCDIR=$(prefix)/share/doc/send_nsca

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/bin
	ginstall -d $(DESTDIR)$(prefix)/etc
	ginstall -d $(DESTDIR)$(NAGIOSBINDIR)
	ginstall -d $(DESTDIR)$(NAGIOSCFGDIR)
	ginstall -m 755 -d $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 755 $(WORKSRC)/src/nsca $(DESTDIR)$(NAGIOSBINDIR)
	ginstall -m 600 $(WORKSRC)/sample-config/nsca.cfg $(DESTDIR)$(NAGIOSCFGDIR)/nsca.cfg.CSW
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(NSCADOCDIR)
	ginstall -m 755 $(WORKSRC)/src/send_nsca $(DESTDIR)$(BINDIR)
	ginstall -m 755 -d $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 755 $(WORKSRC)/src/submit_check_result-sample $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 600 $(WORKSRC)/sample-config/send_nsca.cfg $(DESTDIR)$(NAGIOSCFGDIR)/send_nsca.cfg.CSW
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(SENDNSCADOCDIR)
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d/
	ginstall -m 755 $(FILEDIR)/cswnsca $(DESTDIR)/etc/opt/csw/init.d/
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWsendnsca
	@ginstall -m 644 $(FILEDIR)/CSWsendnsca.cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWsendnsca/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWnsca
	@ginstall -m 644 $(FILEDIR)/CSWnsca.cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWnsca/cswusergroup
	@$(MAKECOOKIE)
