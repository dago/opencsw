#####################################################################
# OpenCSW build recipe for OpenSSL
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = openssl
VERSION = 1.0.0d
CATEGORIES = lib
SONAME=$(shell echo $(VERSION) | tr -d '[a-z]')

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

PACKAGES = CSWlibssl1-0-0 CSWlibssl1-0-0-devel CSWopenssl1-utils

SPKG_DESC_CSWlibssl1-0-0 = Openssl 1.0 runtime libraries
PKGFILES_CSWlibssl1-0-0 = $(libdir).*\.so(\.\d+)*
PKGFILES_CSWlibssl1-0-0 += $(prefix)/etc/ssl/private $(prefix)/etc/ssl/certs 
PKGFILES_CSWlibssl1-0-0 += $(docdir)/libssl1_0_0/.* 

RUNTIME_DEP_PKGS_CSWlibssl1-0-0-devel = CSWlibssl1-0-0
SPKG_DESC_CSWlibssl1-0-0-devel = Openssl 1.0 development support files
PKGFILES_CSWlibssl1-0-0-devel = $(PKGFILES_DEVEL) 
PKGFILES_CSWlibssl1-0-0-devel += $(docdir)/libssl1_0_0_devel/.*

RUNTIME_DEP_PKGS_CSWopenssl1-utils = CSWlibssl1-0-0
SPKG_DESC_CSWopenssl1-utils = Openssl 1.0 binaries and related tools
PKGFILES_CSWopenssl1-utils = $(bindir)/[^/]* $(mandir)/man1/.* $(mandir)/man5/.* $(mandir)/man7/.* 
PKGFILES_CSWopenssl1-utils += $(prefix)/ssl/misc/.* 
PKGFILES_CSWopenssl1-utils += $(prefix)/etc/ssl/openssl\.cnf.*
PKGFILES_CSWopenssl1-utils += $(docdir)/openssl1_utils/.*

PRESERVECONF = $(prefix)/etc/ssl/openssl.cnf

# We use SUN perl, not the opencsw one
CHECKPKG_OVERRIDES_CSWopenssl1-utils += missing-dependency|CSWperl

# We ship the .a files in the devel package
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/libssl.a
ifeq ($(GARCH),sparc)
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv8plus+vis/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv8plus+vis/libssl.a
else
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/pentium_pro/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/pentium_pro/libssl.a
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/libssl.a
endif
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += surplus-dependency|CSWlibssl1-0-0

# We do ship libcrypto in libssl package
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/pentium_pro/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0

# References to default path in documentation files, can be safely ignored
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0_devel/INSTALL
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0_devel/CHANGES
CHECKPKG_OVERRIDES_CSWlibssl1-0-0-devel += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0_devel/FAQ
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/INSTALL
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/FAQ
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl1-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl1_utils/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl1-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl1_utils/FAQ
CHECKPKG_OVERRIDES_CSWopenssl1-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl1_utils/INSTALL

include checkpkg.overrides

###### Upstream and opencsw files information #######

MASTER_SITES = http://www.openssl.org/source/

DISTFILES  = $(NAME)-$(VERSION).tar.gz 
DISTFILES += CSWlibssl1-0-0.checkinstall CSWlibssl1-0-0.preinstall CSWlibssl1-0-0.postinstall
DISTFILES += changelog.CSW README.CSW

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS README.ENGINE

# This patch add optimised build targets for some solaris isa, ie:
# solaris-pentium_pro-cc and solaris-sparcv9+vis-cc
PATCHFILES = more_configure_targets.patch

#PATCHFILES += fix-test-failure.patch

# We install engines libraries in /opt/csw/lib/engines/1.0.0/
# instead of /opt/csw/lib/engines to avoid clashes with 0.9.8
# and futur new release of ssl libraries
PATCHFILES += 0003-make-engines-directory-soname-dependant.patch

# Update openssl.cnf path in man page to follow opencsw standard
PATCHFILES += opencsw_paths.patch

LICENSE = LICENSE

##### Build and installation information #####

# The list of instructions set for which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis sparcv9

# we include *.a files in the devel package so we don't want them excluded
MERGE_EXCLUDE_STATICLIBS = 

# No .so files in libraries
EXTRA_MERGE_EXCLUDE_FILES = .*/libcrypto.so .*/libssl.so

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-x86-cc
pentium_OS_COMPILER	= solaris-pentium-cc
pentium_pro_OS_COMPILER	= solaris-pentium_pro-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparcv8_OS_COMPILER 		= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER		= solaris-sparcv9-cc
sparcv8plus+vis_OS_COMPILER	= solaris-sparcv9+vis-cc
sparcv9_OS_COMPILER		= solaris64-sparcv9-cc

CONFIGURE_ARGS = --prefix=$(prefix) --openssldir=$(prefix)/etc/ssl shared $($(ISA)_OS_COMPILER) --install_prefix=$(DESTDIR)

# We want the csw perl to be used
#CONFIGURE_ENV += PERL="/opt/csw/bin/perl"
# For now we want the sun perl to be used
CONFIGURE_ENV += PERL="/usr/bin/perl"

# Some optimization
EXT_CFLAGS   += -mt -xstrconst
EXT_CXXFLAGS += -noex -mt

# By default, the install target put man pages under
# /opt/csw/ssl/man, but we want them under /opt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

TEST_SCRIPTS = 

include gar/category.mk

pre-configure-modulated:
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	@$(MAKECOOKIE)

merge-doc:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$CATALOGNAME; \
		(cd $(DOWNLOADDIR)/ && ginstall README.CSW changelog.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
		(cd $(WORKSRC_FIRSTMOD)/ && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
	done
	@$(MAKECOOKIE)

post-merge: merge-doc 
