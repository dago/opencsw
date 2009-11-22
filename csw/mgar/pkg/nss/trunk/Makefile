# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARFLAVOR = DBG

## This file contains comments to guide you through various GAR settings.
## Please remove unnecessary comments before committing your code to the code
## repository. The comments to remove are marked with double hashes.
## If you want to remove them all in-place, use:
## gsed -i -e '/^##/d' Makefile
##
## For more information about GAR variables, please see:
## https://sourceforge.net/apps/trac/gar/wiki/GAR%20Variable%20Reference
##
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
##
## The category that your software fits in. This is not a descriptive field, but
## influences the build process. Depending on the CATEGORIES setting, different
## Makefiles are included from gar/categories/ in your trunk directory, which
## adjust the build settings for the respective category.
##
## Possible settings are:
## apps, cpan, devel, gnome, java, kde, lang, lib, meta, net, python, server,
## utils, x11, xfce, xorg, xtra
CATEGORIES = lib
##
## A one-line description of the package, which will appear in the pkginfo.
DESCRIPTION = Network Security Services library, implements PKI support
##
## A longer description of the package. This is only for descriptive purposes
## inside the Makefile and is not used elsewhere.
define BLURB
endef
##
## Upstream URL that should show up in the VENDOR field as well as on
## http://opencsw.org/packages/<packagename>.
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
##
## Whitespace-separated list of URLs to download the source package from.
## There are presets: $(SF_MIRRORS), $(GNU_MIRRORS) and $(GOOGLE_MIRROR).
# TODO: Generate RTM_NAME from GARVERSION
RTM_NAME = NSS_3_12_4_RTM
# MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_12_4_RTM/src/
##
## SF_PROJ is required if you set $(MASTER_SITES) to $(SF_MIRRORS) and the
## Sourceforge project name differs from $(GARNAME). Specifies the Sourceforge
## project name of the software you wish to download.
## SF_PROJ =
##
## A list of space separated patch filenames from files/ that are to be applied
## to the extracted software before the ./configure stage. Patches need to be
## included in the DISTFILES variable as well.
# http://bugs.gentoo.org/show_bug.cgi?id=256102
PATCHFILES  = nss-3.12.4.patch
PATCHFILES += shared-libs.patch
PATCHFILES += platlibs-sqlite3.patch
PATCHFILES += whoami.patch
PATCHFILES += runtime-search-path.patch
## PATCHFILES = freebl.patch
##
## Whitespace-separated list of files which comprise this build. mGAR will look
## for the files in the $(FILEDIR) (trunk/files) directory and on the
## $(MASTER_SITES).
# DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = $(GARNAME)-$(GARVERSION)-with-nspr-4.8.tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)-with-nspr-4.8
##
## We define upstream file regex so we can be notifed of new upstream software
## release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
##
## Catalog name is the name to be used with pkg{-get,util} -i <pkgname>.
## It is different from the system package name, which by convention is CSWpkgname.
## CATALOGNAME =
##
## Set to 1 to mark the package as architecture-independent.
## ARCHALL = 0
##
## A list of files / patterns that should be excluded from the package. Amends
## the default list of excluded filenames $(MERGE_EXCLUDE_DEFAULT), which
## contains things like libtool .la files and files with a leading ~.
## EXTRA_MERGE_EXCLUDE_FILES =
##
## A list of space separated package names that should be marked as
## incompatible with the current package. This will go into the depend file.
## When a user has one of the incompatible packages installed and installs
## your package, he will be prompted that the incompatible package must be
## removed. He will however not be prevented to install your package without
## removing the conflicting package first.
## INCOMPATIBLE_PKGS =
##
##  The name of the license file that should be included in your package. Defaults
##  to COPYING. See http://sourceforge.net/apps/trac/gar/wiki/CopyRightfor details
##  on including and displaying licenses.
## LICENSE =
##
## A list of space separated package names that should be produced from your
## Makefile. This is used when a software has different components that can be
## packaged and used individually (think runtime libraries, client tools, server
## files, development headers). You don't need to set this when you just want to
## produce one package.
##
## When you set this variable to include more than one package, you also need to
## set PKGFILES_CSWpkgname for each package (except for the first one in your
## $(PACKAGES) list) to define which files go into each package. The first
## package from $(PACKAGES) one will hold all files that are not matched by
## PKGFILES_ for other packages.
## PACKAGES =
##
## If specified, GAR feeds the almost-final package prototype file to
## $(PROTOTYPE_FILTER) and reads the final package prototype file from it.
## $(PROTOTYPE_FILTER) is usually a sed/awk/perl one-liner, which was mostly used
## to prepare the prototype file for use with cswclassutils (see
## $(SPKG_CLASSES)). Now that there are convenience variables for cswclassutils,
## you will rarely have to use this. A still valid use case would be to change
## the file permissions of a file to be set-UID.
## See http://wiki.opencsw.org/cswclassutils-package for common usage information
## PROTOTYPE_FILTER =
##
## cswclassutils settings
##
## A list of action classes. Possible values are:
## none cswpreserveconf cswcpsampleconf cswpycompile cswusergroup cswinitsmf
##	cswinetd cswetcservices
## The class 'cswinitsmf' must be the last class listed. When you use cswclassutils,
## you need to add CSWcswclassutils to REQUIRED_PKGS.
## SPKG_CLASSES = none
## Simplified settings for classes:
## PRESERVECONF =
## SAMPLECONF =
## INITSMF =
## USERGROUP =
## ETCSERVICES = <file containing an entry for /etc/services>
## INETDCONF = <file containing an inetd.conf formatted entry>
## A list of runtime package dependencies in the form of CSWfoo.
REQUIRED_PKGS = CSWnspr CSWsqlite3
##
## A list of packages necessary to build this package
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWsqlite3devel
##
## When using non-empty $(PACKAGES):
## REQUIRED_PKGS_CSWpkgname =
## SPKG_DESC_CSWpkgname =
## PKGFILES_CSWpkgname =
## CATALOGNAME_CSWpkgname =
##
## A list of space separated directories where objects should be stripped in
## addition to the bin/ and sbin/ directories.
## STRIP_DIRS =
##
## Define a custom target for the configure phase. When you set this, the target
## that will be used instead of configure: target, is named
## configure-$(CONFIGURE_SCRIPTS) and you will need to define it in your Makefile
## after including gar/gar.include.mk. If you want to skip the configure phase
## completely (for example when your software doesn't need to be compiled) assign
## this variable an empty value. The procedure works for configure, build,
## install and test steps.
CONFIGURE_SCRIPTS = nss
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
##
## Compilation settings
##
## The build directory.
## WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)
##
## BUILD_ARGS is passed as an argument to gmake during the build phase. Use this
## for example, if you need to override Makefile variables.
## BUILD_ARGS =
##
## Arguments passed to the ./configure script.
CONFIGURE_ARGS = $(DIRPATHS)
##
BUILD64 = 1
## CONFIGURE_ENV =
## EXTRA_CFLAGS =
## EXTRA_LDFLAGS =
## EXTRA_INC =
## EXTRA_LIB =
## GARFLAVOR =
## INSTALL_ARGS =
## OPT_FLAGS_SOS = -xO3
## OPT_FLAGS_GCC = -O2 -pipe
##
## The compiler to use. Defaults to SOS11, can be also: SOS12, GCC3, GCC4.
## GARCOMPILER = SOS11
##

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
# DSO_LDOPTS = -R/opt/csw/lib/$$$$ISALIST -L/opt/csw/lib
# export DSO_LDOPTS
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

