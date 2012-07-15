NAME = koha
VERSION = 4.10.05
CATEGORIES = apps
GARTYPE = v2
#WORKSRC = liblime-$(NAME)_v$(VERSION)
#DISTVERSION = $(VERSION)-$(RELEASE)
#SPKG_VERSION = $(VERSION)$(RELEASE)
DISTNAME = liblime-$(NAME)_v$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = Integrated Library System
define BLURB
  Integrated Library System
endef

MASTER_SITES = https://github.com/downloads/liblime/LibLime-Koha/
DISTFILES  = liblime-$(NAME)_v$(VERSION).tar.gz

# Temporary
ARCHALL = 1

# License not found due to changed workdir
#LICENSE = LICENSE
DISTFILES += COPYING

SPKG_SOURCEURL = http://www.koha.org

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWapache2
RUNTIME_DEP_PKGS += CSWidzebra
RUNTIME_DEP_PKGS += CSWmysql5
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWimagemagick
RUNTIME_DEP_PKGS += CSWpmalgorithmchkdig
RUNTIME_DEP_PKGS += CSWpmbiblioendnotest
RUNTIME_DEP_PKGS += CSWpmcgisession
RUNTIME_DEP_PKGS += CSWpmclassadapter
RUNTIME_DEP_PKGS += CSWpmclassfactutil
RUNTIME_DEP_PKGS += CSWpmclsaccessor
RUNTIME_DEP_PKGS += CSWpmdatecalc
RUNTIME_DEP_PKGS += CSWpmdateical
RUNTIME_DEP_PKGS += CSWpmdateleapyear
RUNTIME_DEP_PKGS += CSWpmdatemanip
RUNTIME_DEP_PKGS += CSWpmdbi
RUNTIME_DEP_PKGS += CSWpmdbdmysql
RUNTIME_DEP_PKGS += CSWpmdublincorerecord
RUNTIME_DEP_PKGS += CSWpmgdbarcode
RUNTIME_DEP_PKGS += CSWpmhtmlscrubber
RUNTIME_DEP_PKGS += CSWpmhtmltemplatepro
RUNTIME_DEP_PKGS += CSWpmjson
RUNTIME_DEP_PKGS += CSWpmldap
RUNTIME_DEP_PKGS += CSWpmlibwww
RUNTIME_DEP_PKGS += CSWpmlinguastem
RUNTIME_DEP_PKGS += CSWpmlistmoreutils
RUNTIME_DEP_PKGS += CSWpmmailsendmail
RUNTIME_DEP_PKGS += CSWpmmarccharse
RUNTIME_DEP_PKGS += CSWpmmarccrosswalkdblc
RUNTIME_DEP_PKGS += CSWpmmarcrecord
RUNTIME_DEP_PKGS += CSWpmmarcxml
RUNTIME_DEP_PKGS += CSWpmmimebase64
RUNTIME_DEP_PKGS += CSWpmmimelite
RUNTIME_DEP_PKGS += CSWpmnetz3950zoom
RUNTIME_DEP_PKGS += CSWpmpdfapi2
RUNTIME_DEP_PKGS += CSWpmpdfreuse
RUNTIME_DEP_PKGS += CSWpmpdfreusebarcode
RUNTIME_DEP_PKGS += CSWpmpoe
RUNTIME_DEP_PKGS += CSWpmscheduleat
RUNTIME_DEP_PKGS += CSWpmsmssend
RUNTIME_DEP_PKGS += CSWpmtextcsv
RUNTIME_DEP_PKGS += CSWpmtextcsvxst
RUNTIME_DEP_PKGS += CSWpmtextwrap
RUNTIME_DEP_PKGS += CSWpmxmldumper
RUNTIME_DEP_PKGS += CSWpmxmllibxml
RUNTIME_DEP_PKGS += CSWpmxmllibxslt
RUNTIME_DEP_PKGS += CSWpmxmlrss
RUNTIME_DEP_PKGS += CSWpmxmlsax
RUNTIME_DEP_PKGS += CSWpmxmlsimple
RUNTIME_DEP_PKGS += CSWpmyamlsyck

# Temporary
CHECKPKG_OVERRIDES_CSWkoha += unidentified-dependency
CHECKPKG_OVERRIDES_CSWkoha += surplus-dependency

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
#	@( cd $(WORKSRC) ; \
#	INSTALL_MODE=single perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) CONFDIR=/etc/opt/csw/koha LOCALSTATEDIR=/var/opt/csw/koha INSTALL_MODE='single' INSTALL_BASE='/opt/csw/koha' DB_TYPE='mysql' DB_HOST='localhost' DB_NAME='koha' DB_USER='kohaadmin' DB_PASS='katikoan' INSTALL_ZEBRA='yes' INSTALL_SRU='yes' INSTALL_PAZPAR2='no' AUTH_INDEX_MODE='grs1' ZEBRA_MARC_FORMAT='marc21' ZEBRA_LANGUAGE='en' ZEBRA_USER='kohauser' ZEBRA_PASS='zebrastripes' ZEBRA_SRU_HOST='localhost' ZEBRA_SRU_BIBLIOS_PORT='9998' ZEBRA_SRU_AUTHORITIES_PORT='9999' KOHA_USER='koha' KOHA_GROUP='koha' MERGE_SERVER_HOST='localhost' MERGE_SERVER_PORT='11001' PAZPAR2_HOST= 'localhost' PAZPAR2_PORT='11002' RUN_DATABASE_TESTS='no' PATH_TO_ZEBRA='' )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(NAME) (custom)"
#	@( cd $(WORKSRC) ; \
#	gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
#	@( cd $(WORKSRC) ; \
#	gmake test )
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
