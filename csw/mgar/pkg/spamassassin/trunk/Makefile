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

#MASTER_SITES = http://people.apache.org/~jm/devel/
MASTER_SITES = http://apache.dataphone.se/spamassassin/source/
DISTFILES  = $(SPKG_NAME)-$(GARVERSION).tar.gz
#DISTFILES  = $(SPKG_NAME)-$(GARVERSION)-rc3.tar.gz
DISTFILES += COPYING

RUNTIME_DEP_PKGS  = CSWgnupg CSWosslrt CSWperl CSWpmarchivetar CSWpmdbi CSWpmdigestsha
RUNTIME_DEP_PKGS += CSWpmiosocketinet6 CSWpmiosocketssl CSWpmiozlib
RUNTIME_DEP_PKGS += CSWpmipcountry CSWpmldap CSWpmlibwww CSWpmmaildkim
RUNTIME_DEP_PKGS += CSWpmmailspf CSWpmmailtools CSWpmmimebase64 CSWpmnetaddrip CSWpmnetdns
RUNTIME_DEP_PKGS += CSWrazor CSWpmuri CSWpmhtmlparser CSWzlib

UFILES_REGEX = $(SPKG_NAME)-(\d+(?:\.\d+)*).tar.gz

SAMPLECONF  = /etc/opt/csw/spamassassin/.+\.pre\.CSW
SAMPLECONF += /etc/opt/csw/spamassassin/local\.cf\.CSW
SAMPLECONF += /etc/opt/csw/spamassassin/spamd\.CSW
USERGROUP = /etc/opt/csw/pkg/CSWspamassassin/cswusergroup
INITSMF = /opt/csw/etc/init.d/cswspamd
POSTMSG = /opt/csw/share/doc/spamassassin/README.upgrade

MIGRATE_FILES = init.pre local.cf v310.pre v312.pre v320.pre
MIGRATE_SOURCE_DIR = /opt/csw/etc/spamassassin
MIGRATE_DEST_DIR = /etc/opt/csw/spamassassin

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
#TEST_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)/$(SPKG_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://spamassassin.apache.org/

ifeq ($(shell uname -p), sparc)
  SEDCFLAGS = -xarch=v8
else
  SEDCFLAGS = 
endif

configure-custom:
	@echo " ==> Configuring $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/etc/opt/csw/spamassassin LOCALSTATEDIR=/var/opt/csw/spamassassin CONTACT_ADDRESS=postmaster )
	@$(MAKECOOKIE)

pre-build-modulated:
	@echo " ==> Pre-build $(GARNAME) (custom)"
	@( cd $(WORKSRC)/spamc ; \
	   sed 's/CFLAGS = /CFLAGS = $(SEDCFLAGS) /' Makefile.in > Makefile.tmp ; \
	   cp Makefile.tmp Makefile.in )
	@$(MAKECOOKIE)

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
	@rm -rf $(DESTDIR)
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 755 $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)/opt/csw/etc/init.d/cswspamd
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWspamassassin
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWspamassassin/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/spamassassin
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.spamd.CSW $(DESTDIR)/etc/opt/csw/spamassassin/spamd.CSW
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/CSWspamassassin.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSWspamassassin.README.spamd $(DESTDIR)$(docdir)/$(GARNAME)/README.spamd
	@cp $(FILEDIR)/CSWspamassassin.postmsg $(DESTDIR)$(docdir)/$(GARNAME)/README.upgrade
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)
	echo "WORKSRC: $(WORKSRC)"
	@( cd $(WORKSRC) ; \
	   gmake DESTDIR=$(DESTDIR) install )
	@( cd $(WORKSRC) ; \
	   cp -r C* INSTALL NOTICE README TRADEMARK U* ldap/ sql/ procmailrc.example sample-* $(DESTDIR)$(docdir)/$(GARNAME)/ )
	@( cd $(DESTDIR)/etc/opt/csw/spamassassin ; \
	   mv local.cf local.cf.CSW ; \
	   mv init.pre init.pre.CSW ; \
	   mv v310.pre v310.pre.CSW ; \
	   mv v312.pre v312.pre.CSW ; \
	   mv v330.pre v330.pre.CSW ; \
	   mv v320.pre v320.pre.CSW )
	@rm -rf $(DESTDIR)/opt/csw/lib
	@$(MAKECOOKIE)
