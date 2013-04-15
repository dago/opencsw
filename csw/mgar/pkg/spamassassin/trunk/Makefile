NAME = spamassassin
SPKG_NAME = Mail-SpamAssassin
VERSION = 3.3.2
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Mail filter with a wide range of tests
define BLURB
  SpamAssassin is a mail filter which attempts to identify spam using
  a variety of mechanisms including text analysis, Bayesian filtering,
  DNS blocklists, and collaborative filtering databases.
endef

MASTER_SITES = http://apache.dataphone.se/spamassassin/source/
#MASTER_SITES = http://people.apache.org/~jm/devel/
DISTFILES  = $(SPKG_NAME)-$(VERSION).tar.gz
#DISTFILES  = $(SPKG_NAME)-$(VERSION)-rc3.tar.gz
DISTFgar/category.mk

WORKSRC = $(WORKDIR)/$(SPKG_NAME)-$(VERSION)
SPKG_SOURCEURL = http://spamassasRUNTIME_DEP_PKGS  = CSWgnupgPKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpm-dbi
RUNTIME_DEP_PKGS += CSWpm-html-parser
RUNTIME_DEP_PKGS += CSWpm-io-socket-inet6
RUNTIME_DEP_PKGS += CSWpmiozlib
RUNTIME_DEP_PKGS += CSWpmipcountry
RUNTIME_DEP_PKGS += CSWpm-ldap
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpmmaildkim
RUNTIME_DEP_PKGS += CSWpmmailspf
RUNTIME_DEP_PKGS += CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpm-mime-base64
RUNTIME_DEP_PKGS += CSWpm-netaddr-ip
RUNTIME_-net-dns
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWrazor
RUNTIME_DEP_PKGS += CSWlibz1P_PKGS += CSWzlib

SAMPLECONF  = /etc/opt/csw/spamassassin/.+\.pre\.CSW
SAMPLECONF += /etc/opt/csw/spamassassin/local\.cf\.CSW
SAMPLECONF += /etc/opt/csw/spamassassin/spamd\.CSW
USERGROUP   = /etc/opt/csw/pkg/CSWspamassassin/cswusergroup
INITSMF     = /etc/opt/csw/init.d/cswspamd
POSTMSG     = /opt/csw/share/doc/spamassassin/README.upgrade

MIGRATE_FILES      = init.pre local.cf v310.pre v312.pre v320.pre
MIGRATE_SOURCE_DIR = /opt/csw/etc/spamassassin
MIGRATE_DEST_DIR   = /etc/opt/csw/spamassassin

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPINSTALL_SCRIPTS   = custom

# Doc samples
CHECKPKG_OVERRIDES_CSWspamassassin += file-with-bad-content
# Checkpkg can't determine perl depscy|CSWpmipcountry
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpmmaildkim
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-html-parser
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-mime-base64
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-netaddr-ip
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-ldap
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-dbi
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpmmailspf
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWrazor
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-io-socket-inet6
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpmmailtools
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm-libwww-perl
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpmiozlib
CHECKPKG_OVERRIDES_CSWspamassassin += surplpmipcountry
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-dependency|CSWpm--dependency|CSWpmuri
CHECKPKG_OVERRIDES_CSWspamassassin += surplus-net-dns
# Couldn't make this work...
CHECKPKG_OVERRIDES_CSWspamassassin += no-direct-binding|/opt/csw/bin/spamc|is|not|directly|bound|to|soname|libz.so.1

include gar/category.mkEDCFLAGS = 
endif

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/etc/opt/csw/spamassassin LOCALSTATEDIR=/var/opt/csw/spamassassin CONTACT_ADDRESS=postmaster )
#pre-build-modulated:
#	@echo " ==> Pre-build $(NAME) (custom)"
#	@( cd $(WORKSRC)/spamc ; \
#	   sed 's/LDFLAGS = /LDFLAGS = -Bdirect -z ignore /' Makefile.in > Makefile.tmp ; \
#	   cp Makefile.tmp Makefile.in )
#mp Makefile.in )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake test )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
#	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/init.d
#	@ginstall -m 755 $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)/opt/csw/etc/init.d/cswspamd
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWspamassassin.cswspamd $(DESTDIR)/etc/opt/csw/init.d/cswspamd
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWspamassassin
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWspamassassin/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/spamassassin
	@ginstall -m 644 $(FILEDIR)/CSWspamassassin.spamd.CSW $(DESTDIR)/etc/opt/csw/spamassassin/spamd.CSW
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@cp $(FILEDIR)/CSWspamassassin.README.CSW $(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@cp $(FILEDIR)/CSWspamassassin.README.spamd $(DESTDIR)$(docdir)/$(NAME)/README.spamd
	@cp $(FILEDIR)/CSWspamassassin.postmsg $(DESTDIR)$(docdir)/$(NAME)/README.upgrade
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(NAME)
	echo "WORKSRC: $(WORKSRC)"
	@( cd $(WORKSRC) ; \
	   gmake DESTDIR=$(DESTDIR) install )
	@( cd $(WORKSRC) ; \
	   cp -r C* INSTALL NOTICE README TRADEMARK U* ldap/ sql/ procmailrc.example sample-* $(DESTDIR)$(docdir)/$(NAME)/ )
	@( cd $(DESTDIR)/etc/opt/csw/spamassassin ; \
	   mv local.cf local.cf.CSW ; \
	   mv init.pre init.pre.CSW ; \
	   mv v310.pre v310.pre.CSW ; \
	   mv v312.pre v312.pre.CSW ; \
	   mv v330.pre v330.pre.CSW ; \
	   mv v320.pre v320.pre.CSW )
	@rm -rf $(DESTDIR)/opt/csw/lib