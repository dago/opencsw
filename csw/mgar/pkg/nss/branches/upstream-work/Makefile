# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$


# Based on the following resources:
# - http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nss/nss-3.12.4-r1.ebuild?view=markup
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Build_instructions
# - https://developer.mozilla.org/en/NSS_reference/NSS_environment_variables
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Installation_guide

# Debugging mode, this is work in progress.
GARFLAVOR = DBG

GARNAME = nss
GARVERSION = 3.12.4
CATEGORIES = lib
DESCRIPTION = Network Security Services library, implements PKI support
define BLURB
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NAME from GARVERSION
RTM_NAME = NSS_3_12_4_RTM
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
DIST_SUFFIX = -with-nspr-4.8
DISTFILES  = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX).tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)$(DIST_SUFFIX).tar.gz
REQUIRED_PKGS = CSWnspr CSWsqlite3
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWsqlite3devel
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
BUILD64 = 1

ifeq (OPT,$(GARFLAVOR))
	BUILD_OPT = 1
endif

# NSPR is installed in /opt/csw/lib/nspr, nspr.pc is in /opt/csw/lib/pkgconfig
NSPR_INCLUDE_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --cflags-only-I nspr | gsed 's/-I//')
export NSPR_INCLUDE_DIR
NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')
export NSPR_LIB_DIR

# 64-bit suppport
ifeq ($(MODULATION),isa-sparcv9)
	USE_64 = 1
	export USE_64
endif
ifeq ($(MODULATION),isa-amd64)
	USE_64 = 1
	export USE_64
endif

include gar/category.mk

build-nss: build-coreconf build-dbm build-nss-compile

build-coreconf:
	(cd $(WORKSRC)/mozilla/security/coreconf \
		&& \
	$(BUILD_ENV) \
		&& \
	gmake -j1 CC="$(CC)")
	@$(MAKECOOKIE)

build-dbm:
	(cd $(WORKSRC)/mozilla/security/dbm \
		&& \
	$(BUILD_ENV) \
		&& \
	gmake -j1 CC="$(CC)")
	@$(MAKECOOKIE)

build-nss-compile:
	(cd $(WORKSRC)/mozilla/security/nss \
		&& \
	$(BUILD_ENV) \
		&& \
	gmake -j1 CC="$(CC)")
	@$(MAKECOOKIE)
