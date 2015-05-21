# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = redis
VERSION = 3.0.1

DESCRIPTION = An advanced key-value store

MASTER_SITES = http://download.redis.io/releases/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswredis.xml

VENDOR_URL = http://redis.io

PACKAGES += CSWredis
SPKG_DESC_CSWredis = An advanced key-value store

BUILD64 = 1
ISAEXEC = 1

GARCOMPILER = GNU

PATCHFILES += 0001-Fix-tclsh-finding.patch
PATCHFILES += 0001-Use-substitute-for-flock.patch

GARCis is the path to the SMF DTD
CHECKPKG_OVERRIDES_CSWredis += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswredis.xml

GARCOMPILER = GCC4

# These are set in the Makefile and are not inherited when we force our CFLAGS in
EXTRA_CFLAGS += -std=c99 -pedantic -Wall -W -D__EEXTRA_CFLAGS += -Du_int32_t=uint32_tEXTENSIONS__ -D_XPG6

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_ARGS += V=1

# Some tests fail
#SKIPTEST ?= 1

INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX = $(DESTDIR)$(prefix)
INSTALL_OVERRIDE_VARS += INSTALL_BIN
INSTALL_OVERRIDE_VAR_INSTALL_BIN = $(DESTDIR)$(bindir)

# This is for tail taking -n namely gtail for us
TEST_ENV_PATH = $(prefix)/gnu:$(PATH)

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswredis.xml
PROTOTYPE_CLASS_smf = manifest

PRESERVECONF += $(sysconfdir)/redis/redis.conf
PRESERVECONF += $(sysconfdir)/redis/sentinel.conf

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKSRC)/redis.conf $(DESTDIR)$(sysconfdir)/redis/redis.conf
	ginstall -D -m 0644 $(WORKSRC)/sentinel.conf $(DESTDIR)$(sysconfdir)/redis/sentinel.conf
	ginstall -D -m 0644 $(WORKDIR)/cswredis.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswredis.xml
	ginstall -d -m 0755 $(DESTDIR)/var/opt/csw/redis/data
	@$(MAKECOOKIE)
