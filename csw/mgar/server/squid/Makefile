GARNAME = squid
GARVERSION = 2.7
CATEGORIES = server
RELEASE = STABLE3
DISTVERSION = $(GARVERSION).$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

MASTER_SITES = http://www.squid-cache.org/Versions/v2/2.7/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += $(call admfiles,CSWsquid, depend prototype copyright postinstall preremove)

CONFIGURE_ARGS  = --prefix=$(prefix) --mandir=/opt/csw/share/man
CONFIGURE_ARGS += --localstatedir=/var/$(prefix)
CONFIGURE_ARGS += --datadir=$(datadir)/$(GARNAME)
CONFIGURE_ARGS += --with-large-files
CONFIGURE_ARGS += --enable-large-cache-files
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --enable-icmp
CONFIGURE_ARGS += --enable-delay-pools
CONFIGURE_ARGS += --enable-useragent-log
CONFIGURE_ARGS += --enable-referer-log
CONFIGURE_ARGS += --enable-arp-acl
CONFIGURE_ARGS += --enable-snmp
CONFIGURE_ARGS += --enable-auth=basic
CONFIGURE_ARGS += --enable-basic-auth-helpers=LDAP,SMB,YP,PAM,SASL,NCSA

TEST_TARGET = check

include ../category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(RELEASE)

post-install:
	( cp -r $(FILEDIR)/etc $(DESTDIR)/etc )
	@$(MAKECOOKIE)
