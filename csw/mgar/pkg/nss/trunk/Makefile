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

NAME = nss
MAJOR_VERSION = 3
MINOR_VERSION = 12
PATCHLEVEL    = 11
VERSION = $(MAJOR_VERSION).$(MINOR_VERSION).$(PATCHLEVEL)
CATEGORIES = lib
define BLURB
  Network Security Services (NSS) is a set of libraries designed to support
  cross-platform development of security-enabled client and server
  applications. Applications built with NSS can support SSL v2 and v3, TLS,
  PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and
  other security standards.
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NAME from VERSION
RTM_NAME = NSS_$(MAJOR_VERSION)_$(MINOR_VERSION)_$(PATCHLEVEL)_RTM
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += mpl-tri-license-txt
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibnss3 CSWlibnss-dev CSWlibnss3-tools

SPKG_DESC_CSWlibnss3 = Network Security Services library, implements crypto, PKI, SSL, and S/MIME support
SPKG_DESC_CSWlibnss-dev = libnss development files
SPKG_DESC_CSWlibnss3-tools = libnss3 command-line utilities

PKGFILES_CSWlibnss-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibnss3-tools = $(bindir).*

CATALOGNAME_CSWlibnss-dev = libnss_dev
CATALOGNAME_CSWlibnss3-tools = libnss3_tools
OBSOLETED_BY_CSWlibnss-dev = CSWlibnss3-devel

RUNTIME_DEP_PKGS_CSWlibnss3 = CSWnspr CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibnss3-tools += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibnss3-tools += CSWnspr
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWnspr-dev CSWlibsqlite3-dev

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
BUILD64 = 1
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64   = $(libdir)

EXTRA_INC = $(prefix)/include

libdir_install = $(prefix)/lib
includedir = $(prefix)/include/nss

ifneq (DBG,$(GARFLAVOR))
	BUILD_OPT = 1
	export BUILD_OPT
	CONFIGURE_ARGS += --disable-debug --enable-optimize
endif

# NSPR is installed in /opt/csw/lib/nspr, nspr.pc is in /opt/csw/lib/pkgconfig
NSPR_INCLUDE_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --cflags-only-I nspr | gsed 's/-I//')
export NSPR_INCLUDE_DIR

NSS_ENABLE_ECC = 1
export NSS_ENABLE_ECC

# To avoid creating /opt/csw/lib/libsqlite3.so (already exists)
NSS_USE_SYSTEM_SQLITE = 1
export NSS_USE_SYSTEM_SQLITE

# 64-bit suppport
ifeq ($(MODULATION),isa-sparcv9)
	USE_64 = 1
	export USE_64
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
else
ifeq ($(MODULATION),isa-amd64)
	USE_64 = 1
	export USE_64
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
else
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')
endif
endif
export NSPR_LIB_DIR

ifeq ($(USE_64),1) 
SQLITE_LIB_DIR = /opt/csw/lib/64
else
SQLITE_LIB_DIR = /opt/csw/lib
endif
export SQLITE_LIB_DIR
SQLITE_INCLUDE_DIR = /opt/csw/include
export SQLITE_INCLUDE_DIR

# Based on:
# http://mxr.mozilla.org/security/source/security/nss/pkg/solaris/SUNWtlsu/prototype_com
NSS_BINARIES  = addbuiltin
NSS_BINARIES += certutil
NSS_BINARIES += cmsutil
NSS_BINARIES += crlutil
NSS_BINARIES += modutil
NSS_BINARIES += pk12util
NSS_BINARIES += signtool
NSS_BINARIES += signver
NSS_BINARIES += ssltap

LICENSE = mpl-tri-license-txt

# For DBG builds
# PATCHFILES  = whoami.patch

# Required patches.
PATCHFILES += include.patch
PATCHFILES += ld-options.patch
# PATCHFILES += platlibs-sqlite3.patch
PATCHFILES_isa-sparcv8 = sqlite3-32.patch
PATCHFILES_isa-i386 = sqlite3-32.patch
PATCHFILES_isa-sparcv9  = sqlite3-64.patch
# PATCHFILES_isa-sparcv9 += platlibs-sqlite3-64.patch
PATCHFILES_isa-amd64  = sqlite3-64.patch
# PATCHFILES_isa-amd64 += platlibs-sqlite3-64.patch
PATCHFILES += 0004-fix-xarch-and-add-SQLITE_LIB_DIR-var.patch
PATCHFILES += 0005-platlibs.mk-linking-bltest.patch

# http://lists.opencsw.org/pipermail/pkgsubmissions/2010-February/000167.html
# NOISAEXEC = 1

CPPFLAGS=

include gar/category.mk

build-nss: build-coreconf build-dbm build-nss-compile
	@$(MAKECOOKIE)

build-coreconf:
	(cd $(WORKSRC)/mozilla/security/coreconf \
		&& \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
	gmake -j1)
	@$(MAKECOOKIE)

build-dbm:
	(cd $(WORKSRC)/mozilla/security/dbm \
		&& \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
	gmake -j1)
	@$(MAKECOOKIE)

# There's an extra interpolation somehwere inside nss' build system, so $$$$
# needs to be used instead of $$.
build-nss-compile:
	(cd $(WORKSRC)/mozilla/security/nss \
		&& \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS) -R/opt/csw/lib/$$$$ISALIST' \
	gmake -j1)
	@$(MAKECOOKIE)

install-nss:
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	for f in $(WORKSRC)/mozilla/dist/SunOS5*/lib/*.so; do \
	  ginstall -m 755 $${f} $(DESTDIR)$(libdir); \
	  if [ -r $(WORKSRC)/mozilla/dist/SunOS5*/lib/`basename $${f} .so`.chk ]; then \
	    ginstall -m 644 \
	      $(WORKSRC)/mozilla/dist/SunOS5*/lib/`basename $${f} .so`.chk \
	      $(DESTDIR)$(libdir); \
	  fi \
	done
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	# TODO: nss-config
	# gcp -a $(WORKSRC)/mozilla/dist/*/bin/nss-config $(DESTDIR)$(bindir)
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f in \
			$(WORKSRC)/mozilla/dist/public/nss/*.h; \
		do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	for bin in $(NSS_BINARIES); do \
	  ginstall -m 755 \
	    $(WORKSRC)/mozilla/dist/*/bin/$${bin} \
	    $(DESTDIR)$(bindir)/`basename $${file}`; \
	done
	# Asserting that we have the right version in the .pc file
	ggrep "Version: $(VERSION)" $(FILEDIR)/nss.pc \
		|| ( \
			echo "Please adjust nss version in $(FILEDIR)/nss.pc" \
				&& \
			false \
		)
	ginstall -d -m 755 $(DESTDIR)$(libdir)/pkgconfig
	ginstall -m 644 \
		$(FILEDIR)/nss.pc \
		$(DESTDIR)$(libdir)/pkgconfig
	if [ $(MEMORYMODEL) = 64 ]; then \
		gsed -i -e 's+/lib$$+lib/64+' $(DESTDIR)$(libdir)/pkgconfig/nss.pc ; \
	fi
	@$(MAKECOOKIE)
