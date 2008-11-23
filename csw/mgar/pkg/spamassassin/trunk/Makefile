GARNAME = spamassassin
SPKG_NAME = Mail-SpamAssassin
GARVERSION = 3.2.5
CATEGORIES = net

DESCRIPTION = mail filter with a wide range of tests
define BLURB
  SpamAssassin is a mail filter which attempts to identify spam using
  a variety of mechanisms including text analysis, Bayesian filtering,
  DNS blocklists, and collaborative filtering databases.
endef

MASTER_SITES = http://apache.jumper.nu/spamassassin/source/
DISTFILES  = $(SPKG_NAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWspamassassin,checkinstall depend postinstall)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://spamassassin.apache.org/

configure-custom:
	@echo " ==> Configuring $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/opt/csw/etc/spamassassin LOCALSTATEDIR=/var/opt/csw/spamassassin CONTACT_ADDRESS=postmaster )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(GARNAME) (custom)"
#	@( cd $(WORKSRC) ; \
#	   gmake test )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)/var/opt/csw/$(GARNAME)
	@cp $(FILEDIR)/CSWspamassassin.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSWspamassassin.README.spamd $(DESTDIR)$(docdir)/$(GARNAME)/README.spamd
	@cp $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)$(docdir)/$(GARNAME)/cswspamd
	@cp $(FILEDIR)/CSWspamassassin.spamd.xml.CSW $(DESTDIR)$(docdir)/$(GARNAME)/spamd.xml.CSW
	@cp $(FILEDIR)/CSWspamassassin.svc-spamd.CSW $(DESTDIR)$(docdir)/$(GARNAME)/svc-spamd.CSW
	@( cd $(WORKSRC) ; \
	   gmake install )
	@( cd $(WORKSRC) ; \
	   cp -r C* INSTALL LICENSE NOTICE README TRADEMARK U* ldap/ sql/ procmailrc.example sample-* $(DESTDIR)$(docdir)/$(GARNAME)/ )
	@( cd $(DESTDIR)/opt/csw/etc/spamassassin ; \
	   mv local.cf local.cf.CSW ; \
	   mv init.pre init.pre.CSW ; \
	   mv v310.pre v310.pre.CSW ; \
	   mv v312.pre v312.pre.CSW ; \
	   mv v320.pre v320.pre.CSW )
	@rm -rf $(DESTDIR)/opt/csw/lib
	@$(MAKECOOKIE)
