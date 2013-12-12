NAME = koha
VERSION = 4.10.05
CATEGORIES = apps
GARTYPE = v2
DISTNAME = liblime-$(NAME)_v$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = Integrated Library System
define BLURB
  Integrated Library System
endef

MASTER_SITES = https://github.com/downloads/liblime/LibLime-Koha/
DISTFILES  = liblime-$(NAME)_v$(VERSION).tar.gz

# Temporary?
ARCHALL = 1

LICENSE = LICENSE

SPKG_SOURCEURL = http://www.koha.org

CONFIGURE_AR# DependenciesRGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWapache2
RUNTIME_DEP_PKGS += CSWidzebra
RUNTIME_DEP_PKGS += CSWmysql5
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DE Already in experimental
RUNTIME_DEP_PKGS += CSWpm-business-isbn
RUNTIME_DEP_PKGS += CSWpm-cgi-session-serializ-yaml
RUNTIME_DEP_PKGS += CSWpm-email-date
RUNTIME_DEP_PKGS += CSWpm-http-oai
RUNTIME_DEP_PKGS += CSWpm-xml-sax-writer
# Needs to be built
RUNTIME_DEP_PKGS += CSWpm-cache-memcached-fast
RUNTIME_DEP_PKGS += CSWpm-chi
RUNTIME_DEP_PKGS += CSWpm-datetime-format-dateparse
RUNTIME_DEP_PKGS += CSWpm-datetime-format-strptime
RUNTIME_DEP_PKGS += CSWpm-dbix-connector
RUNTIME_DEP_PKGS += CSWpm-http-exception
RUNTIME_DEP_PKGS += CSWpm-http-message
RUNTIME_DEP_PKGS += CSWpm-modern-perl
RUNTIME_DEP_PKGS += CSWpm-moose
RUNTIME_DEP_PKGS += CSWpm-moosex-role-parameterized
RUNTIME_DEP_PKGS += CSWpm-rose-db
RUNTIME_DEP_PKGS += CSWpm-rose-db-object
RUNTIME_DEP_PKGS += CSWpm-squatting
RUNTIME_DEP_PKGS += CSWpm-squatting-on-psgi
RUNTIME_DEP_PKGS += CSWpm-text-aspell
RUNTIME_DEP_PKGS += CSWpm-xml-sax-expatxs
# Perl modules needed
RUNTIME_DEP_PKGS += CSWpm-algorithm-checkdigits
RUNTIME_DEP_PKGS += CSWpm-cache-memcached
RUNTIME_DEP_PKGS += CSWpm-cgi-session
RUNTIME_DEP_PKGS += CSWpm-class-accessor
RUNTIME_DEP_PKGS += CSWpm-dbi
RUNTIME_DEP_PKGS += CSWpm-json
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpm-list-moreutils
RUNTIME_DEP_PKGS += CSWpm-marc-charset
RUNTIME_DEP_PKGS += CSWpm-mime-base64
RUNTIME_DEP_PKGS += CSWpm-plack
RUNTIME_DEP_PKGS += CSWpm-poe
RUNTIME_DEP_PKGS += CSWpm-schedule-at
RUNTIME_DEP_PKGS += CSWpm-try-tiny
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWpm-xml-sax
# Old style modules
RUNTIME_DEP_PKGS += CSWpmbiblioendnotest+= CSWpmcgisession
RUNTIME_DEP_PKGS += CSWpmclassadapter
RUNTIME_DEP_PKGS += CSWpmclassfactutil
RUNTIMEdataical
RUNTIME_DEP_PKGS += CSWpmdatecalc
RUNTIME_DEP_PKGS += CSWpmdateical
RUNTIME_DEP_PKGS += CSWpmdatemanip
RUNTIME_DEP_PKGS += CSWpmdatetime
RUNTIME_DEP_PKGS += CSWpmdbdmysql
RUNTIME_DEP_PKGS += CSWpmfileslurpWpmdublincorerecrd
RUNTIME_DEP_PKGS += CSWpmgdbarcode
RUNTIME_DEP_PKGS += CSWpmhtmlscrubber
RUNTIME_DEP_PKGS += CSWpmhtmltemplatepro
RUNTIMElinguastem
RUNTIME_DEP_PKGS += CSWpmmailsendmailCSWpm-marc-charset
RUNTIME_DEP_PKGS += CSWpmmarccrswlkdblc
RUNTIME_DEP_PKGS += CSWpmmarcrecord
RUNTIME_DEP_PKGS += CSWpmmarcxml
RUNTIME_DEPlite
RUNTIME_DEP_PKGS += CSWpmnetip
RUNTIME_DEP_PKGS += CSWpmnetserverS += CSWpmmimelite
RUNTIME_DEP_PKGS += CSWpmnetz3950zoom
RUNTIME_DEP_PKGS += CSWpmpdfapi2
RUNTIME_DEP_PKGS += CSWpmpdfreuse
RUNTIME_DEP_PKGS += CSWpmpdfreusebarcode
RUNTIMEsmssend
RUNTIME_DEP_PKGS += CSWpmtextcsv
RUNTIME_DEP_PKGS += CSWpmtextcsvxs
RUNTIME_DEP_PKGS += CSWpmtexticonv
RUNTIME_DEP_PKGS += CSWpmtextwrapperS += CSWpmtextwrap
RUNTIME_DEP_PKGS += CSWpmxmldumper
RUNTIME_DEP_PKGS += CSWpmxmllibxml
RUNTIME_DEP_PKGS += CSWpmxmllibxslt
RUNTIME_DEP_PKGS += CSWpmxmlrss
RUNTIME_DEPimple
RUNTIME_DEP_PKGS += CSWpmyamlsyck
# Suspected not needed, try without
#RUNTIME_DEP_PKGS += CSWimagemagick
#RUNTIME_DEP_PKGS += CSWpmdateleapyear
#RUNTIME_DEP_PKGS += CSWpmdublincorerecrd
#RUNTIME_DEP_PKGS += CSWpm-ldapS += CSWpmyamlsyck

# Temporary
#CHECKPKG_OVERRIDES_CSWkoha += unidentified-dependency
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
#	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/var/name