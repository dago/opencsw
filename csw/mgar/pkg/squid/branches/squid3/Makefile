# Squid 3
# $Id$
#
NAME = squid
VERSION = 3.1
CATEGORIES = server
RELEASE = 19
DISTVERSION = $(VERSION).$(RELEASE)
DISTNAME = squid-$(DISTVERSION)
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9]\).*\.[0-9]*/\1/')
GARTYPE = v2

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

PACKAGES = CSWsquid
RUNTIME_DEP_PKGS += CSWliblber2-4-2
RUNTIME_DEP_PKGS += CSWlibldap2-4-2
RUNTIME_DEP_PKGS += CSWlibssl0-9-8
RUNTIME_DEP_PKGS += CSWlibsasl2-2
RUNTIME_DEP_PKGS += CSWlibltdl7
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWbdb48

PACKAGING_PLATFORMS =  solaris10-sparc solaris10-i386

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
DISTFILES = squid-$(DISTVERSION).tar.bz2

PATCHFILES =  0000-Use-opt-csw-bin-bash-for-bootstrap.sh.patch
PATCHFILES += 0002-Link-against-OpenSSL-from-OpenCSW.patch
PATCHFILES += 0003-Check-for-ber_pvt_opt_on-instead-of-main-in-libber.patch
PATCHFILES += 0006-Replace-usr-local-squid-libexec-with-opt-csw-libexec.patch
PATCHFILES += 0006-Use-default-cache_dir.patch
PATCHFILES += 0006-Use-usr-xpg4-bin-egrep.patch
PATCHFILES += 0007-Use-OpenCSW-specific-paths-for-various-helper-tests.patch

sysconfdir = /etc/opt/csw/$(NAME)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=${sysconfdir}
CONFIGURE_ARGS += --datadir=$(datadir)/$(NAME)
CONFIGURE_ARGS += --docdir=$(datadir)/$(NAME)
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(NAME)
CONFIGURE_ARGS += --enable-arp-acl
CONFIGURE_ARGS += --enable-auth=basic,ntlm,digest,negotiate
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
CONFIGURE_ARGS += --enable-ipf-transparent
CONFIGURE_ARGS += --disable-ident-lookups
CONFIGURE_ARGS += --disable-icmp
CONFIGURE_ARGS += --with-dl
CONFIGURE_ARGS += --with-large-files
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-default-user=$(NAME)

GARCOMPILER = GNU
EXTRA_LDFLAGS += -L$(prefix)/bdb48/lib
EXTRA_INC += $(prefix)/bdb48/include

TEST_TARGET = 

SAMPLECONF = squid.conf
SAMPLECONF += cachemgr.conf
SAMPLECONF += mime.conf
USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS      = varuser
PROTOTYPE_FILES_varuser  = \/var\/opt\/csw\/$(NAME)\/cache
PROTOTYPE_FILES_varuser += \/var\/opt\/csw\/$(NAME)\/logs
PROTOTYPE_CLASS_varuser  = ugfiles
PROTOTYPE_USER_varuser   = $(NAME)
PROTOTYPE_GROUP_varuser  = $(NAME)

# Needed for CSWlibsmbclient0: ntlm_auth and winbindd
# CHECKPKG_OVERRIDES_CSWsquid += surplus-dependency|CSWlibsmbclient0

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(RELEASE)

pre-configure-modulated:
	cd $(WORKSRC) && $(BUILD_ENV) ./bootstrap.sh
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/logs
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/cache
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	ginstall -m 755 $(FILEDIR)/cswsquid3 $(DESTDIR)/etc/opt/csw/init.d/csw$(NAME)
	ginstall -m 644 $(FILEDIR)/CSWsquid3.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)/cswusergroup
	@$(MAKECOOKIE)

