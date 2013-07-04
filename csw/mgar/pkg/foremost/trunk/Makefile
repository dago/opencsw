# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = foremost
VERSION = 1.5.7

DESCRIPTION = Forensic file recovery and data carving tool
define BLURB
endef

# MASTER_SITES = $(SF_MIRROR)
MASTER_SITES = http://foremost.sourceforge.net/pkg/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://foremost.sourceforge.net/

BUILD_DEP_PKGS = CSWtofrodos

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /usr/local/etc/foremost.conf
REINPLACE_WITH_conf = $(sysconfdir)/foremost.conf
REINPLACE_FILES_conf += config.c

CONFIGURE_SCRIPTS = 

BUILD_OVERRIDE_VARS = RAW_CC RAW_FLAGS
BUILD_OVERRIDE_VAR_RAW_CC = $(CC)
BUILD_OVERRIDE_VAR_RAW_FLAGS = $(CFLAGS) -DVERSION=\\\"$(VERSION)\\\"
BUILD_ARGS = solaris

# There is no testsuite
TEST_SCRIPTS =

# We need ginstall as install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

INSTALL_OVERRIDE_VARS += BIN
INSTALL_OVERRIDE_VAR_BIN = $(DESTDIR)$(bindir)
INSTALL_OVERRIDE_VARS += MAN
INSTALL_OVERRIDE_VAR_MAN = $(DESTDIR)$(mandir)/man8
INSTALL_OVERRIDE_VARS += CONF
INSTALL_OVERRIDE_VAR_CONF = $(DESTDIR)$(sysconfdir)

PRESERVECONF += $(sysconfdir)/foremost.conf

MIGRATE_FILES += foremost.conf

include gar/category.mk

post-extract:
	fromdos $(WORKSRC)/*
	@$(MAKECOOKIE)

pre-install:
	ginstall -d $(INSTALL_OVERRIDE_VAR_BIN)
	ginstall -d $(INSTALL_OVERRIDE_VAR_MAN)
	ginstall -d $(INSTALL_OVERRIDE_VAR_CONF)
	@$(MAKECOOKIE)

post-install:
	gunzip $(INSTALL_OVERRIDE_VAR_MAN)/foremost.8.gz
	@$(MAKECOOKIE)
