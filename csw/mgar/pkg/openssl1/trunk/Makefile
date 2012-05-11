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

PKCS11 = 1
T4 = 1

###### Package information #######

NAME = openssl
VERSION = 1.0.1c
CATEGORIES = lib
GARTYPE = v2
SONAME=$(shell echo $(VERSION) | tr -d '[a-z]')

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

PACKAGES = CSWlibssl1-0-0 CSWlibssl-dev CSWopenssl-utils

SPKG_DESC_CSWlibssl1-0-0 = Openssl 1.0 runtime libraries
PKGFILES_CSWlibssl1-0-0 = $(libdir).*\.so(\.\d+)*
PKGFILES_CSWlibssl1-0-0 += $(prefix)/etc/ssl/private $(prefix)/etc/ssl/certs 
PKGFILES_CSWlibssl1-0-0 += $(docdir)/libssl1_0_0/.* 

RUNTIME_DEP_PKGS_CSWlibssl-dev = CSWlibssl1-0-0
SPKG_DESC_CSWlibssl-dev = Openssl 1.0 development support files
PKGFILES_CSWlibssl-dev = $(PKGFILES_DEVEL) 
PKGFILES_CSWlibssl-dev += $(docdir)/libssl_dev/.*

RUNTIME_DEP_PKGS_CSWopenssl-utils = CSWlibssl1-0-0
SPKG_DESC_CSWopenssl-utils = Openssl 1.0 binaries and related tools
PKGFILES_CSWopenssl-utils = $(bindir)/[^/]* $(mandir)/man1/.* $(mandir)/man5/.* $(mandir)/man7/.* 
PKGFILES_CSWopenssl-utils += $(prefix)/ssl/misc/.* 
PKGFILES_CSWopenssl-utils += $(prefix)/ssl/openssl\.cnf.*
PKGFILES_CSWopenssl-utils += $(sysconfdir)/ssl/openssl\.cnf.*
PKGFILES_CSWopenssl-utils += $(docdir)/openssl_utils/.*

PRESERVECONF = $(sysconfdir)/ssl/openssl.cnf

# We do ship libcrypto in libssl package
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
ifeq ($(shell /usr/bin/uname -p),sparc) 
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv8plus+vis/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
else
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
endif


# We use SUN perl, not the opencsw one
CHECKPKG_OVERRIDES_CSWopenssl-utils += missing-dependency|CSWperl


# References to default path in documentation files, can be safely ignored
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/INSTALL
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/CHANGES
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/FAQ
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/INSTALL
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/FAQ
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl1_0_0/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/FAQ
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/INSTALL

# We have a lot of collision until libssl1.0.0 will replace libssl0.9.8
#include checkpkg.overrides

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
#
# Let's always block some compromised CA, whatever the CA configured
# (patchs taken from Debian Package)
PATCHFILES += block_bad_certificates.patch

# Add old-style certificates hash generation to maintain compatibilies
# with gnutls and programs linked with openssl 0.9.8 
# Patch taken from Debian
PATCHFILES += c_rehash-compat.patch

# support for pkcs11 engine http://blogs.sun.com/chichang1/entry/how_to_integrate_pkcs11_engine
ifdef PKCS11
ifneq ($(shell /usr/bin/uname -r),5.9)
        PATCHFILES += pkcs11_engine-1.0.1b.patch.2012-04-30
endif
endif

# support for sparc t4 crypto engine 
# see http://bubbva.blogspot.fr/2011/11/exciting-crypto-advances-with-t4.html
#     https://blogs.oracle.com/DanX/entry/sparc_t4_openssl_engine
# patch taken from https://hg.openindiana.org/upstream/oracle/userland-gate/
ifdef T4
ifneq ($(shell /usr/bin/uname -r),5.9)
	PATCHFILES += 0007-Engine-t4-patch.patch
endif
endif

LICENSE = LICENSE

##### Build and installation information #####

# The list of instructions set for which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis sparcv9

# we include *.a files in the devel package so we don't want them excluded
#MERGE_EXCLUDE_STATICLIBS = 

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

CONFIGURE_ARGS = --prefix=$(prefix) shared $($(ISA)_OS_COMPILER) --install_prefix=$(DESTDIR)

# PKCS11 is only for Solaris 10 so we must create solaris 10 specific packages
ifdef PKCS11
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386
ifneq ($(shell /usr/bin/uname -r),5.9)
        CONFIGURE_ARGS += --pk11-libname=$(abspath /usr/lib/$(MM_LIBDIR)/libpkcs11.so) 
endif
endif 


# For now we want the sun perl to be used
CONFIGURE_ENV += PERL="/usr/bin/perl"

# Some optimization
EXT_CFLAGS   += -mt -xstrconst
EXT_CXXFLAGS += -noex -mt

# By default, the install target put man pages under
# /opt/csw/ssl/man, but we want them under /opt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

# library files are not automatically stripped
STRIP_DIRS = $(DESTDIR)/$(libdir) $(DESTDIR)/$(libdir)/openssl-$(SONAME)/engines/

TEST_SCRIPTS = 

include gar/category.mk

pre-configure-modulated:
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	@$(MAKECOOKIE)

fix-paths:
	gsed -i -e 's,/usr/local/ssl/lib,$(sysconfdir)/ssl,' $(PKGROOT)$(mandir)/man1/ca.1
	gsed -i -e 's,/usr/local/ssl,$(prefix)/ssl,' $(PKGROOT)$(bindir)/c_rehash

install-conf-misc: 
	if [ -f "$(PKGROOT)$(prefix)/ssl/openssl.cnf" ] && [ ! -h "$(PKGROOT)$(prefix)/ssl/openssl.cnf" ]; then \
		ginstall -d "$(PKGROOT)$(sysconfdir)/ssl"; \
		mv "$(PKGROOT)$(prefix)/ssl/openssl.cnf" $(PKGROOT)$(sysconfdir)/ssl/openssl.cnf.CSW; \
		ln -sf ../../..$(sysconfdir)/ssl/openssl.cnf $(PKGROOT)$(prefix)/ssl/openssl.cnf; \
	fi	
	[ ! -d "$(PKGROOT)$(sysconfdir)/ssl/misc" ] || \
		mv "$(PKGROOT)$(sysconfdir)/ssl/misc" "$(PKGROOT)/$(prefix)/ssl/"
		
merge-doc:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$CATALOGNAME; \
		(cd $(DOWNLOADDIR)/ && ginstall -m 0644 README.CSW changelog.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
		(cd $(WORKSRC_FIRSTMOD)/ && ginstall -m 0644 $(DOCFILES) $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
	done
	@$(MAKECOOKIE)

post-merge: merge-doc install-conf-misc fix-paths
