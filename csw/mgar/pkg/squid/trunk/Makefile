GARNAME = squid
GARVERSION = 2.7
CATEGORIES = server
RELEASE = STABLE6
DISTVERSION = $(GARVERSION).$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)
RELVER = $(shell echo $(GARVERSION) |gsed 's/\(^[0-9]\).*\.[0-9]*/\1/')

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

PACKAGES = CSWsquid
CATALOGNAME_CSWsquid = squid
SPKG_DESC_CSWsquid = $(DESCRIPTION)
SPKG_CLASSES_CSWsquid = none cswinitsmf
REQUIRED_PKGS_CSWsquid = CSWoldaprt CSWosslrt CSWsasl CSWcswclassutils
PROTOTYPE_FILTER = awk '$$$$3 ~/\/init.d\/cswsquid$$$$/ { $$$$2 = "cswinitsmf" } { print }'

MASTER_SITES = http://www.squid-cache.org/Versions/v$(RELVER)/$(GARVERSION)/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWsquid.postinstall CSWsquid.preremove cswsquid

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --datadir=$(datadir)/$(GARNAME)
CONFIGURE_ARGS += --enable-arp-acl
CONFIGURE_ARGS += --enable-auth=basic
CONFIGURE_ARGS += --enable-basic-auth-helpers=LDAP,SMB,YP,PAM,SASL,NCSA
CONFIGURE_ARGS += --enable-cache-digests
CONFIGURE_ARGS += --enable-carp
CONFIGURE_ARGS += --enable-delay-pools
CONFIGURE_ARGS += --enable-devpoll
CONFIGURE_ARGS += --enable-forw-via-db
CONFIGURE_ARGS += --enable-htcp
CONFIGURE_ARGS += --enable-icmp
CONFIGURE_ARGS += --enable-large-cache-files
CONFIGURE_ARGS += --enable-referer-log
CONFIGURE_ARGS += --enable-removal-policies=heap,lru
CONFIGURE_ARGS += --enable-select
CONFIGURE_ARGS += --enable-snmp
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --enable-useragent-log
CONFIGURE_ARGS += --with-dl
CONFIGURE_ARGS += --with-large-files
CONFIGURE_ARGS += --with-openssl=$(prefix)

TEST_TARGET = check

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(RELEASE)

pre-configure-modulated:
	cd $(WORKSRC) && $(BUILD_ENV) ./bootstrap.sh
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)$(localstatedir)/cache
	gcp $(DOWNLOADDIR)/cswsquid $(DESTDIR)/etc/opt/csw/init.d/
	chmod 0755 $(DESTDIR)/etc/opt/csw/init.d/cswsquid
	gmv $(DESTDIR)$(sysconfdir)/squid.conf \
		$(DESTDIR)$(sysconfdir)/squid.conf.CSW
	@$(MAKECOOKIE)

