NAME = koha
VERSION = 3.00.06
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Integrated Library System
define BLURB
  Integrated Library System
endef

MASTER_SITES = http://downloads.ptfsinc.com/harley/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

#ARCHALL = 1

LICENSE = LICENSE

SPKG_SOURCEURL = http://www.koha.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWperl CSWmysql5 CSWapache2 CSWidzebra
RUNTIME_DEP_PKGS += CSWimagemagickCSWpmclassadapter CSWpmclassfactutil
RUNTIME_DEP_PKGS += CSWpmalgorithmchkdig CSWpmbiblioendnotest CSWpmcgisession CSWpmclsaccessor
RUNTIME_DEP_PKGS += CSWpmdbdmysql CSWpmdbi CSWpmdatecalc CSWpmdateical
RUNTIME_DEP_PKGS += CSWpmdateleapyear CSWpmdatemanip CSWpmdublincorerecord CSWpmgdbarcode
RUNTIME_DEP_PKGS += CSWpmhtmltemplatepro CSWpmlibwww CSWpmjson CSWpmlinguastem
RUNTIME_DEP_PKGS += CSWpmmarccrosswalkdblc CSWpmmarcxml CSWpmmarcrecord CSWpmmimebase64
RUNTIME_DEP_PKGS += CSWpmmailsendmail CSWpmldap CSWpmnetz3950zoom CSWpmpdfapi2
RUNTIME_DEP_PKGS += CSWpmpdfreusebarcode CSWpmpoe CSWpmscheduleat CSWpmsmssend
RUNTIME_DEP_PKGS += CSWpmtextwrap CSWpmxmldumper CSWpmxmllibxml CSWpmxmllibxslt
RUNTIME_DEP_PKGS += CSWpmxmlsax CSWpmxmlsimple CSWpmyamlsyck CSWpmhtmlscrubber
RUNTIME_DEP_PKGS += CSWpmdatecalc CSWpmmimelite CSWpmpdfreuse CSWpmxmlrss
RUNTIME_DEP_PKGS += CSWpmlistmoreutils CSWpmmarccharse CSWpmtextcsv CSWpmtextcsvxst

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	INSTALL_MODE=single perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/etc/opt/csw/koha LOCALSTATEDIR=/var/opt/csw/koha INSTALL_MODE='single' INSTALL_BASE='/opt/csw/koha' DB_TYPE='mysql' DB_HOST='localhost' DB_NAME='koha' DB_USER='kohaadmin' DB_PASS='katikoan' INSTALL_ZEBRA='yes' INSTALL_SRU='yes' INSTALL_PAZPAR2='no' AUTH_INDEX_MODE='grs1' ZEBRA_MARC_FORMAT='marc21' ZEBRA_LANGUAGE='en' ZEBRA_USER='kohauser' ZEBRA_PASS='zebrastripes' ZEBRA_SRU_HOST='localhost' ZEBRA_SRU_BIBLIOS_PORT='9998' ZEBRA_SRU_AUTHORITIES_PORT='9999' KOHA_USER='koha' KOHA_GROUP='koha' MERGE_SERVER_HOST='localhost' MERGE_SERVER_PORT='11001' PAZPAR2_HOST= 'localhost' PAZPAR2_PORT='11002' RUN_DATABASE_TESTS='no' PATH_TO_ZEBRA='' )
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

#DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
#	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/init.d
#	@ginstall -m 755 $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/opt/csw/etc/init.d/cswnamed
#	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw
#	@ginstall -m 644 $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf
#	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWbind
#	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWbind/
#	@ginstall -m 644 $(FILEDIR)/bind.CSW $(DESTDIR)/etc/opt/csw/pkg/CSWbind/bind
#	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
#	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
#	( cd $(WORKSRC) ; \
#	  gmake DESTDIR=$(DESTDIR) install )
#	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named
#	@touch $(DESTDIR)/var/opt/csw/named/named.pid
#	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/dev
#	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/etc/opt/csw
#	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/var/named
	@$(MAKECOOKIE)
