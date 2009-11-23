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
MAJOR_VERSION = 3
MINOR_VERSION = 12
PATCHLEVEL = 4
GARVERSION = $(MAJOR_VERSION).$(MINOR_VERSION).$(PATCHLEVEL)
CATEGORIES = lib
DESCRIPTION = Network Security Services library, implements PKI support
define BLURB
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NAME from GARVERSION
RTM_NAME = NSS_3_12_4_RTM
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
# This patch taken from http://bugs.gentoo.org/show_bug.cgi?id=256102
PATCHFILES  = nss-3.12.4.patch
PATCHFILES += shared-libs.patch
PATCHFILES += platlibs-sqlite3.patch
PATCHFILES += platlibs-sunos.patch
PATCHFILES += whoami.patch
PATCHFILES += runtime-search-path.patch
PATCHFILES += nss-3.12.4-gentoo-fixups-1.diff
PATCHFILES += csw-include.patch
PATCHFILES += gln.patch
DIST_SUFFIX = -with-nspr-4.8
DISTFILES  = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX).tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)$(DIST_SUFFIX).tar.gz
REQUIRED_PKGS = CSWnspr CSWsqlite3
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWsqlite3devel
CONFIGURE_SCRIPTS = nss
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
BUILD64 = 1

install_libdir = $(prefix)/lib/nss
includedir = $(prefix)/include/nss

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
XCFLAGS = $(CFLAGS)
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
export USE_SYSTEM_ZLIB ZLIB_LIBS NSDISTMODE NSS_ENABLE_ECC XCFLAGS

include gar/category.mk

configure-nss: respect-ldflags add-runtime-search-path
	@$(MAKECOOKIE)

respect-ldflags:
	(cd $(WORKSRC)/mozilla/security/coreconf \
		&& \
	gsed -i -e 's:SOURCE_PREFIX = $$(CORE_DEPTH)/\.\./dist:SOURCE_PREFIX = $$(CORE_DEPTH)/dist:' \
			source.mk \
		&& \
	gsed -i -e 's/\$$(MKSHLIB) -o/\$$(MKSHLIB) \$$(LDFLAGS) -o/g' rules.mk)
	@$(MAKECOOKIE)

add-runtime-search-path:
	# Make sure that the runtime search path is added in all Makefiles.
	gfind $(WORKSRC) \( -name Makefile -o -name '*.mk' \) \
		-exec gsed -i -e 's|-L\$$(NSPR_LIB_DIR)|-L$$(NSPR_LIB_DIR) -R$$(NSPR_LIB_DIR)/$$$$ISALIST|' \
		{} \;
	# A form of assert
	gegrep -- '-R.*ISALIST' $(WORKSRC)/mozilla/security/nss/lib/freebl/config.mk
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

install-nss:
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	gcp -a $(WORKSRC)/mozilla/security/dist/*/lib/*.so $(DESTDIR)$(libdir)
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	gcp -a $(WORKSRC)/mozilla/security/dist/*/bin/nss-config $(DESTDIR)$(bindir)
	ginstall -d -m 755 $(DESTDIR)/lib/pkgconfig
	ginstall -m 644 \
		$(WORKSRC)/mozilla/security/dist/*/lib/pkgconfig/nss.pc \
		$(DESTDIR)/lib/pkgconfig
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	gcp -a $(WORKSRC)/mozilla/security/dist/private/nss/*.h $(DESTDIR)$(includedir)
	gcp -a $(WORKSRC)/mozilla/security/dist/public/nss/*.h $(DESTDIR)$(includedir)
	(cd $(DESTDIR)$(libdir); for file in *.so; do \
		mv $${file} $$(file).$(MINOR_VERSION); \
		ln -s $${file}.$(MINOR_VERSION) $${file}; \
	done)
	(for file in $(WORKSRC)/mozilla/security/dist/*/bin/*; do \
		ginstall -m 755 $${file} $(DESTDIR)$(bindir)/nss$$(basename $${file}); \
	done)
	@$(MAKECOOKIE)
