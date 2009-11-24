# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Based on the following resources:
# - http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nss/nss-3.12.4-r1.ebuild?view=markup
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Build_instructions
# - https://developer.mozilla.org/en/NSS_reference/NSS_environment_variables
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Installation_guide
#
# A discussion:
# - https://groups.google.com/group/mozilla.dev.tech.crypto/browse_thread/thread/709646e32fc4fad0#
#
# TODO: nss-config
# TODO: a better nss.pc

GARNAME = nss
MAJOR_VERSION = 3
MINOR_VERSION = 12
PATCHLEVEL    = 4
GARVERSION = $(MAJOR_VERSION).$(MINOR_VERSION).$(PATCHLEVEL)
CATEGORIES = lib
DESCRIPTION = Network Security Services library, implements PKI support
define BLURB
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NAME from GARVERSION
RTM_NAME = NSS_3_12_4_RTM
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
DIST_SUFFIX = -with-nspr-4.8
DISTFILES = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX).tar.gz
DISTNAME  = $(GARNAME)-$(GARVERSION)$(DIST_SUFFIX)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)$(DIST_SUFFIX).tar.gz
REQUIRED_PKGS = CSWnspr CSWsqlite3
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWsqlite3devel
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
BUILD64 = 1

libdir_install = $(prefix)/lib/nss
# libdir = $(prefix)/lib/nss
includedir = $(prefix)/include/nss

ifeq (OPT,$(GARFLAVOR))
	BUILD_OPT = 1
	export BUILD_OPT
endif

# NSPR is installed in /opt/csw/lib/nspr, nspr.pc is in /opt/csw/lib/pkgconfig
NSPR_INCLUDE_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --cflags-only-I nspr | gsed 's/-I//')
export NSPR_INCLUDE_DIR

# To consider in the future.
# NSS_ENABLE_ECC = 1
# export NSS_ENABLE_ECC

# 64-bit suppport
ifeq ($(MODULATION),isa-sparcv9)
	USE_64 = 1
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
	export USE_64
else
ifeq ($(MODULATION),isa-amd64)
	USE_64 = 1
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
	export USE_64
else
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')
endif
endif
export NSPR_LIB_DIR

# For DBG builds
PATCHFILES = whoami.patch

include gar/category.mk

build-nss: build-coreconf build-dbm build-nss-compile
	@$(MAKECOOKIE)

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
	for f in $(WORKSRC)/mozilla/dist/SunOS5*/lib/*.so; do \
		ginstall -m 755 $${f} $(DESTDIR)$(libdir); \
	done
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	# TODO: nss-config
	# gcp -a $(WORKSRC)/mozilla/dist/*/bin/nss-config $(DESTDIR)$(bindir)
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in \
			$(WORKSRC)/mozilla/dist/private/nss/*.h \
			$(WORKSRC)/mozilla/dist/public/nss/*.h; \
		do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	cd $(DESTDIR)$(libdir) && for file in *.so; do \
		if [ ! -h $${file} ]; then \
			gmv -v $${file} $${file}.$(MINOR_VERSION); \
			gln -s $${file}.$(MINOR_VERSION) $${file}; \
		fi; \
	done
	for file in $(WORKSRC)/mozilla/dist/*/bin/* ; do \
		ginstall -m 755 $${file} $(DESTDIR)$(bindir)/nss`basename $${file}`; \
	done
	# Asserting that we have the right version in the .pc file
	ggrep "Version: $(GARVERSION)" $(FILEDIR)/nss.pc \
		|| ( \
			echo "Please adjust nss version in $(FILEDIR)/nss.pc" \
				&& \
			false \
		)
	ginstall -d -m 755 $(DESTDIR)$(prefix)/lib/pkgconfig
	ginstall -m 644 \
		$(FILEDIR)/nss.pc \
		$(DESTDIR)$(prefix)/lib/pkgconfig
	@$(MAKECOOKIE)

# Create symlinks allowing to use -L/opt/csw/lib/nss/64 for 64-bit
# architectures.
post-merge:
	if [ "$(GARCH)" = sparc ]; then \
		gln -sf sparcv9 $(PKGROOT)$(libdir)/64; \
	elif [ "$(GARCH)" = i386 ]; then \
		gln -sf amd64 $(PKGROOT)$(libdir)/64; \
	fi
	@$(MAKECOOKIE)
