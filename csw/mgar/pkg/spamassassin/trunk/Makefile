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
#DISTFILES += $(call admfiles,CSWspamassassin,checkinstall depend postinstall)

LICENSE = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)/LICENSE

REQUIRED_PKGS = CSWosslrt CSWperl CSWpmarchivetar CSWpmdbi CSWpmdigestsha1 CSWpmiosocketinet6 CSWpmiosocketssl CSWpmiozlib CSWpmipcountry CSWpmldap CSWpmlibwww CSWpmmaildkim CSWpmmailspf CSWpmmailtools CSWpmmimebase64 CSWpmnetdns CSWpmuri CSWpmhtmlparser CSWzlib CSWcswclassutils

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SPKG_NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES_CSWspamassassin = none cswusergroup cswcpsampleconf cswinitsmf

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

PROTOTYPE_FILTER  = awk ' \
   $$$$3 ~ /\/opt\/csw\/etc\/spamassassin\/.+\.pre\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
   $$$$3 ~ /\/opt\/csw\/etc\/spamassassin\/local\.cf\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
   $$$$3 ~ /\/opt\/csw\/etc\/CSWspamassassin\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
   $$$$3 ~ /\/init.d\/cswspamd$$$$/ { $$$$2 = "cswinitsmf" } \
   { print }'

include gar/category.mk

WORKSRC = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://spamassassin.apache.org/

configure-custom:
	@echo " ==> Configuring $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/opt/csw/etc/spamassassin LOCALSTATEDIR=/var/opt/csw/spamassassin CONTACT_ADDRESS=postmaster )
	@$(MAKECOOKIE)

pre-build-modulated:
	@echo " ==> Pre-build $(GARNAME) (custom)"
	@( cd $(WORKSRC)/spamc ; \
	   pwd ; \
	   sed 's/CFLAGS = /CFLAGS = -xarch=v8 /' Makefile.in > Makefile.tmp ; \
	   cp Makefile.tmp Makefile.in )
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
	@ginstall -d $(DESTDIR)$(sysconfdir)/CSWspamassassin
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)/etc/opt/csw/init.d/cswspamd
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.cswusergroup $(DESTDIR)$(sysconfdir)/CSWspamassassin/cswusergroup
	@cp $(FILEDIR)/CSWspamassassin.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSWspamassassin.README.spamd $(DESTDIR)$(docdir)/$(GARNAME)/README.spamd
#	@cp $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)$(docdir)/$(GARNAME)/cswspamd
#	@cp $(FILEDIR)/CSWspamassassin.spamd.xml.CSW $(DESTDIR)$(docdir)/$(GARNAME)/spamd.xml.CSW
#	@cp $(FILEDIR)/CSWspamassassin.svc-spamd.CSW $(DESTDIR)$(docdir)/$(GARNAME)/svc-spamd.CSW
	@( cd $(WORKSRC) ; \
	   gmake install )
	@( cd $(WORKSRC) ; \
	   cp -r C* INSTALL NOTICE README TRADEMARK U* ldap/ sql/ procmailrc.example sample-* $(DESTDIR)$(docdir)/$(GARNAME)/ )
	@( cd $(DESTDIR)/opt/csw/etc/spamassassin ; \
	   mv local.cf local.cf.CSW ; \
	   mv init.pre init.pre.CSW ; \
	   mv v310.pre v310.pre.CSW ; \
	   mv v312.pre v312.pre.CSW ; \
	   mv v320.pre v320.pre.CSW )
	@rm -rf $(DESTDIR)/opt/csw/lib
	@$(MAKECOOKIE)
