GARNAME = spamassassin
SPKG_NAME = Mail-SpamAssassin
GARVERSION = 3.3.0
CATEGORIES = net

DESCRIPTION = mail filter with a wide range of tests
define BLURB
  SpamAssassin is a mail filter which attempts to identify spam using
  a variety of mechanisms including text analysis, Bayesian filtering,
  DNS blocklists, and collaborative filtering databases.
endef

#MASTER_SITES = http://apache.jumper.nu/spamassassin/source/
MASTER_SITES = http://people.apache.org/~wtogami/devel/
#DISTFILES  = $(SPKG_NAME)-$(GARVERSION).tar.gz
DISTFILES  = $(SPKG_NAME)-$(GARVERSION)-beta1.tar.gz

LICENSE = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)/LICENSE

REQUIRED_PKGS  = CSWosslrt CSWperl CSWpmarchivetar CSWpmdbi CSWpmdigestsha1
REQUIRED_PKGS += CSWpmiosocketinet6 CSWpmiosocketssl CSWpmiozlib
REQUIRED_PKGS += CSWpmipcountry CSWpmldap CSWpmlibwww CSWpmmaildkim
REQUIRED_PKGS += CSWpmmailspf CSWpmmailtools CSWpmmimebase64 CSWpmnetdns
REQUIRED_PKGS += CSWpmuri CSWpmhtmlparser CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SPKG_NAME)-(\d+(?:\.\d+)*).tar.gz

SAMPLECONF  = /opt/csw/etc/spamassassin/.+\.pre\.CSW
SAMPLECONF += /opt/csw/etc/spamassassin/local\.cf\.CSW
INITSMF = /etc/opt/csw/init.d/cswspamd
USERGROUP = /opt/csw/etc/CSWspamassassin/cswusergroup

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
#TEST_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://spamassassin.apache.org/

configure-custom:
	@echo " ==> Configuring $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/opt/csw/etc/spamassassin LOCALSTATEDIR=/var/opt/csw/spamassassin CONTACT_ADDRESS=postmaster )
	@$(MAKECOOKIE)

#pre-build-modulated:
#	@echo " ==> Pre-build $(GARNAME) (custom)"
#	@( cd $(WORKSRC)/spamc ; \
#	   sed 's/CFLAGS = /CFLAGS = -xarch=v8 /' Makefile.in > Makefile.tmp ; \
#	   cp Makefile.tmp Makefile.in )
#	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake test )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@echo "LICENSE = $(WORKSRC)/LICENSE"
	@ls -l $(WORKSRC)/LICENSE
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)/var/opt/csw/$(GARNAME)
	@ginstall -d $(DESTDIR)$(sysconfdir)/CSWspamassassin
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)/etc/opt/csw/init.d/cswspamd
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.cswusergroup $(DESTDIR)$(sysconfdir)/CSWspamassassin/cswusergroup
	@cp $(FILEDIR)/CSWspamassassin.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSWspamassassin.README.spamd $(DESTDIR)$(docdir)/$(GARNAME)/README.spamd
	echo "WORKSRC: $(WORKSRC)"
	@( cd $(WORKSRC) ; \
	   gmake DESTDIR=$(DESTDIR) install )
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
