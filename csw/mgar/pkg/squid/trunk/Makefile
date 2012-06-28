NAME = squid
VERSION = 2.7
CATEGORIES = server
GARTYPE = v2
RELEASE = STABLE9
DISTVERSION = $(VERSION).$(RELEASE)
DISTNAME = $(NAME)-$(DISTVERSION)
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9]\).*\.[0-9]*/\1/')

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

PACKAGES = CSWsquid
CATALOGNAME_CSWsquid = squid

RUNTIME_DEP_PKGS_CSWsquid += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWsquid += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsquid += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWsquid += CSWlibldap2-4-2

INITSMF = /etc/opt/csw/init.d/csw$(NAME)
PRESERVECONF = /etc/opt/csw/$(NAME)/cachemgr.conf
PRESERVECONF = /etc/opt/csw/$(NAME)/squid.conf
PRESERVECONF = /etc/opt/csw/$(NAME)/mime.conf

MIGRATE_SOURCE_DIR = /opt/csw/etc
MIGRATE_DEST_DIR = /etc/opt/csw/$(NAME)
MIGRATE_FILES  = cachemgr.conf
MIGRATE_FILES += mime.conf
MIGRATE_FILES += squid.conf

MASTER_SITES = http://www.squid-cache.org/Versions/v$(RELVER)/$(VERSION)/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += cswsquid

EXTRA_CPPFLAGS += -DDEFAULT_SQUID_ERROR_DIR=\\\"/etc/opt/csw/squid/errors\\\"

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/$(NAME)
CONFIGURE_ARGS += --datadir=$(datadir)/$(NAME)
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(NAME)
CONFIGURE_ARGS += --enable-arp-acl
CONFIGURE_ARGS += --enable-auth=basic
CONFIGURE_ARGS += --enable-basic-auth-helpers=LDAP,SMB,YP,PAM,SASL,NCSA
CONFIGURE_ARGS += --enable-cache-digests
CONFIGURE_ARGS += --enable-carp
CONFIGURE_ARGS += --enable-delay-pools
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

PROTOTYPE_MODIFIERS      = varuser
PROTOTYPE_FILES_varuser  = /var/opt/csw/squid/cache
PROTOTYPE_FILES_varuser += /var/opt/csw/squid/logs
PROTOTYPE_USER_varuser   = nobody
PROTOTYPE_GROUP_varuser  = nobody

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(RELEASE)

pre-configure-modulated:
	cd $(WORKSRC) && $(BUILD_ENV) ./bootstrap.sh
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/logs
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/cache
	ginstall -m 755 $(DOWNLOADDIR)/cswsquid $(DESTDIR)/etc/opt/csw/init.d/cswsquid
	@$(MAKECOOKIE)

