# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARFLAVOR = DBG

# Based on:
# http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nss/nss-3.12.4-r1.ebuild?view=markup
# and
# https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Build_instructions
# and
# https://developer.mozilla.org/en/NSS_reference/NSS_environment_variables
# and
# https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Installation_guide
GARNAME = nss
GARVERSION = 3.12.4
# http://www.gentoo-portage.com/AJAX/Ebuild/96014
CATEGORIES = lib
DESCRIPTION = Network Security Services library, implements PKI support
define BLURB
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NAME from GARVERSION
RTM_NAME = NSS_3_12_4_RTM
# MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_12_4_RTM/src/
# http://bugs.gentoo.org/show_bug.cgi?id=256102
PATCHFILES  = nss-3.12.4.patch
PATCHFILES += shared-libs.patch
PATCHFILES += platlibs-sqlite3.patch
PATCHFILES += whoami.patch
PATCHFILES += runtime-search-path.patch
# DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = $(GARNAME)-$(GARVERSION)-with-nspr-4.8.tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)-with-nspr-4.8
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS = CSWnspr CSWsqlite3
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWsqlite3devel
CONFIGURE_SCRIPTS = nss
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
ifeq (OPT,$(GARFLAVOR))
	BUILD_OPT = 1
endif
NSS_USE_SYSTEM_SQLITE = 1
NSPR_INCLUDE_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --cflags-only-I nspr | gsed 's/-I//')
NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')
USE_SYSTEM_ZLIB = 1
ZLIB_LIBS = -lz
NSDISTMODE = copy
NSS_ENABLE_ECC = 1
XCFLAGS=$(CFLAGS)
FREEBL_NO_DEPEND = 1
LDOPTS = $(LD_OPTIONS)
ifeq ($(MODULATION),isa-sparcv9)
	USE_64 = 1
	export USE_64
endif
ifeq ($(MODULATION),isa-amd64)
	USE_64 = 1
	export USE_64
endif
export BUILD_OPT NSS_USE_SYSTEM_SQLITE NSPR_INCLUDE_DIR NSPR_LIB_DIR
export USE_SYSTEM_ZLIB ZLIB_LIBS NSDISTMODE NSS_ENABLE_ECC XCFLAGS FREEBL_NO_DEPEND

include gar/category.mk

configure-nss: respect-ldflags add-runtime-search-path
	@$(MAKECOOKIE)

respect-ldflags:
	(cd $(WORKSRC)/mozilla/security/coreconf \
		&& \
	gsed -e 's:SOURCE_PREFIX = $$(CORE_DEPTH)/\.\./dist:SOURCE_PREFIX = $$(CORE_DEPTH)/dist:' \
		-i source.mk \
		&& \
	gsed -i -e 's/\$$(MKSHLIB) -o/\$$(MKSHLIB) \$$(LDFLAGS) -o/g' rules.mk)
	@$(MAKECOOKIE)

add-runtime-search-path:
	# Make sure that the runtime search path is added for NSPR libraries.
	for f in \
			mozilla/security/nss/cmd/pk11mode/Makefile \
			mozilla/security/nss/cmd/platlibs.mk \
			mozilla/security/nss/cmd/shlibsign/Makefile \
			mozilla/security/nss/cmd/shlibsign/mangle/Makefile \
			mozilla/security/nss/lib/ckfw/builtins/Makefile \
			mozilla/security/nss/lib/ckfw/capi/Makefile \
			mozilla/security/nss/lib/ckfw/nssmkey/Makefile \
			mozilla/security/nss/lib/freebl/config.mk \
			mozilla/security/nss/lib/nss/config.mk \
			mozilla/security/nss/lib/smime/config.mk \
			mozilla/security/nss/lib/softoken/config.mk \
			mozilla/security/nss/lib/softoken/legacydb/config.mk \
			mozilla/security/nss/lib/ssl/config.mk \
			mozilla/security/nss/lib/util/config.mk; do \
		gsed -i -e 's|-L\$$(NSPR_LIB_DIR)|-L$$(NSPR_LIB_DIR) -R$$(NSPR_LIB_DIR)/$$$$ISALIST|' $(WORKSRC)/$$f; \
	done;
	# A form of assert
	ggrep -- -R $(WORKSRC)/mozilla/security/nss/lib/freebl/config.mk
	@$(MAKECOOKIE)

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

