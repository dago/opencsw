# Squid 3
# $Id$
#
NAME = squid3
VERSION = 3.1
CATEGORIES = server
RELEASE = 15
DISTVERSION = $(VERSION).$(RELEASE)
DISTNAME = squid-$(DISTVERSION)
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9]\).*\.[0-9]*/\1/')

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

PACKAGES = CSW$(NAME)
CATALOGNAME_CSWsquid = $(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME) = CSWoldaprt CSWosslrt CSWsasl
PACKAGING_PLATFORMS =  solaris9-sparc solaris9-i386
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

PATCHFILES =  0000-Use-opt-csw-bin-bash-for-bootstrap.sh.patch
PATCHFILES += 0001-Use-opt-csw-bin-ggrep-instead-of-egrep.patch
PATCHFILES += 0002-Link-against-OpenSSL-from-OpenCSW.patch
PATCHFILES += 0003-Check-for-ber_pvt_opt_on-instead-of-main-in-libber.patch

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
CONFIGURE_ARGS += --enable-large-cache-files
CONFIGURE_ARGS += --enable-referer-log
CONFIGURE_ARGS += --enable-removal-policies=heap,lru
CONFIGURE_ARGS += --enable-select
CONFIGURE_ARGS += --enable-snmp
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --enable-useragent-log
CONFIGURE_ARGS += --disable-ident-lookups
CONFIGURE_ARGS += --disable-icmp
CONFIGURE_ARGS += --with-dl
CONFIGURE_ARGS += --with-large-files
CONFIGURE_ARGS += --with-openssl=$(prefix)

CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/squid_unix_group.8
CHECKPKG_OVERRIDES_CSW$(NAME) += pkginfo-opencsw-repository-uncommitted
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/lib|opt/csw/bin/squidclient
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib|opt/csw/bin/squidclient
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib/rw7|opt/csw/bin/squidclient
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/lib|opt/csw/libexec/cachemgr.cgi
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib|opt/csw/libexec/cachemgr.cgi
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib/rw7|opt/csw/libexec/cachemgr.cgi
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/lib|opt/csw/libexec/diskd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib|opt/csw/libexec/diskd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib/rw7|opt/csw/libexec/diskd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/lib|opt/csw/libexec/unlinkd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib|opt/csw/libexec/unlinkd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib/rw7|opt/csw/libexec/unlinkd
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/lib|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry|/opt/sunstudio12.1/lib/rw7|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWcas-initsmf
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWcas-migrateconf
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWcas-preserveconf
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWcommon
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWoldaprt
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWosslrt
CHECKPKG_OVERRIDES_CSW$(NAME) += unidentified-dependency|CSWsasl
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libsasl2.so.2|is|needed|by|opt/csw/libexec/sasl_auth
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|liblber-2.4.so.2|is|needed|by|opt/csw/libexec/squid_ldap_group
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libcrypto.so.0.9.8|is|needed|by|opt/csw/libexec/ncsa_auth
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libssl.so.0.9.8|is|needed|by|opt/csw/libexec/diskd
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libssl.so.0.9.8|is|needed|by|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libldap-2.4.so.2|is|needed|by|opt/csw/libexec/squid_ldap_group
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libssl.so.0.9.8|is|needed|by|opt/csw/libexec/unlinkd
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libssl.so.0.9.8|is|needed|by|opt/csw/libexec/ncsa_auth
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libcrypto.so.0.9.8|is|needed|by|opt/csw/libexec/diskd
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libcrypto.so.0.9.8|is|needed|by|opt/csw/libexec/unlinkd
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libltdl.so.7|is|needed|by|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libldap-2.4.so.2|is|needed|by|opt/csw/libexec/squid_ldap_auth
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|libcrypto.so.0.9.8|is|needed|by|opt/csw/sbin/squid
CHECKPKG_OVERRIDES_CSW$(NAME) += soname-not-found|liblber-2.4.so.2|is|needed|by|opt/csw/libexec/squid_ldap_auth
CHECKPKG_OVERRIDES_CSW$(NAME) += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSW$(NAME) += surplus-dependency|CSWoldaprt
CHECKPKG_OVERRIDES_CSW$(NAME) += surplus-dependency|CSWsasl
CHECKPKG_OVERRIDES_CSW$(NAME) += surplus-dependency|CSWosslrt

EXTRA_LDFLAGS += -L/opt/csw/lib -R/opt/csw/lib

TEST_TARGET = 

PROTOTYPE_MODIFIERS      = varuser
PROTOTYPE_FILES_varuser  = /var/opt/csw/$(NAME)/cache
PROTOTYPE_FILES_varuser += /var/opt/csw/$(NAME)/logs
PROTOTYPE_USER_varuser   = $(NAME)
PROTOTYPE_GROUP_varuser  = $(NAME)

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(RELEASE)

pre-configure-modulated:
	cd $(WORKSRC) && $(BUILD_ENV) ./bootstrap.sh
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/logs
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/cache
	ginstall -m 755 $(DOWNLOADDIR)/cswsquid $(DESTDIR)/etc/opt/csw/init.d/csw$(NAME)
	@$(MAKECOOKIE)

