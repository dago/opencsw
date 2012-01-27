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

# Uncomment to enable PKCS11 engine
PKCS11 = 1

###### Package information #######

NAME = openssl
VERSION = 0.9.8t
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

PACKAGES = CSWopenssl CSWlibssl0-9-8 CSWlibssl-dev CSWopenssl-utils

SPKG_DESC_CSWopenssl = Openssl meta package
CATALOGNAME_CSWopenssl = openssl
RUNTIME_DEP_PKGS_CSWopenssl = CSWlibssl-dev CSWopenssl-utils CSWlibssl0-9-8
ARCHALL_CSWopenssl = 1
OBSOLETED_BY_CSWopenssl = CSWossl
CHECKPKG_OVERRIDES_CSWossl += surplus-dependency|CSWopenssl

SPKG_DESC_CSWlibssl0-9-8 = Openssl runtime libraries
CATALOGNAME_CSWlibssl0-9-8 = libssl0_9_8
RUNTIME_DEP_PKGS_CSWlibssl0-9-8 = CSWcacertificates
OBSOLETED_BY_CSWlibssl0-9-8 = CSWosslrt
CHECKPKG_OVERRIDES_CSWosslrt += surplus-dependency|CSWlibssl0-9-8

SPKG_DESC_CSWlibssl-dev = Openssl development libraries and headers
CATALOGNAME_CSWlibssl-dev = libssl_dev
RUNTIME_DEP_PKGS_CSWlibssl-dev = CSWlibssl0-9-8
OBSOLETED_BY_CSWlibssl-dev = CSWossldevel
CHECKPKG_OVERRIDES_CSWossldevel += archall-devel-package

SPKG_DESC_CSWopenssl-utils = Openssl binaries and related tools 
CATALOGNAME_CSWopenssl-utils = openssl_utils
RUNTIME_DEP_PKGS_CSWopenssl-utils = CSWlibssl0-9-8
SPKG_CLASSES_CSWopenssl-utils = none cswpreserveconf
OBSOLETED_BY_CSWopenssl-utils = CSWosslutils
CHECKPKG_OVERRIDES_CSWosslutils += surplus-dependency|CSWopenssl-utils

# openssl is a meta-package
CHECKPKG_OVERRIDES_CSWopenssl += surplus-dependency|CSWopenssl-utils
CHECKPKG_OVERRIDES_CSWopenssl += surplus-dependency|CSWlibssl-dev
CHECKPKG_OVERRIDES_CSWopenssl += surplus-dependency|CSWlibssl0-9-8

# we use sun perl not csw one
CHECKPKG_OVERRIDES_CSWopenssl-utils += missing-dependency|CSWperl

#CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += surplus-dependency|CSWcacertificates

# this package contains several libraries files and we will not split
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += non-uniform-lib-versions-in-package|sonames=libcrypto.so.0.9.7,libcrypto.so.0.9.8,libssl.so.0.9.7,libssl.so.0.9.8

# we will not recompile old 0.9.7 version for now
ifeq ($(shell /usr/bin/uname -p),sparc) 
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += bad-rpath-entry|/opt/csw/lib/sparcv8plus+vis|opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += bad-rpath-entry|/opt/csw/lib/sparcv8plus+vis|opt/csw/lib/sparcv8plus+vis/libssl.so.0.9.7
else
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/pentium_pro/libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/pentium_pro/libssl.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/libssl.so.0.9.7
endif


# we do ship .a files in the devel package
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libssl.a
ifeq ($(shell /usr/bin/uname -p),sparc) 
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv8plus+vis/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv8plus+vis/libssl.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/libssl.a
else
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/libssl.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/pentium_pro/libcrypto.a
CHECKPKG_OVERRIDES_CSWlibssl-dev += discouraged-path-in-pkgmap|/opt/csw/lib/pentium_pro/libssl.a
endif

# the /usr/local references in the documents files are relevant
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/FAQ
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/INSTALL
CHECKPKG_OVERRIDES_CSWopenssl-utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl_utils/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl/INSTALL
CHECKPKG_OVERRIDES_CSWopenssl += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl/CHANGES
CHECKPKG_OVERRIDES_CSWopenssl += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssl/FAQ
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl0_9_8/INSTALL
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl0_9_8/FAQ
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl0_9_8/CHANGES
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/CHANGES
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/FAQ
CHECKPKG_OVERRIDES_CSWlibssl-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libssl_dev/INSTALL



###### Upstream and opencsw files information #######

MASTER_SITES = http://www.openssl.org/source/ http://openssl.org/news/
UPSTREAM_MASTER_SITES = http://www.openssl.org/source/ 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(0.9.8[a-z]).tar.gz

DISTFILES  = $(NAME)-$(VERSION).tar.gz 
DISTFILES += CSWopenssl.prototype
DISTFILES += CSWlibssl0-9-8.checkinstall CSWlibssl0-9-8.preinstall CSWlibssl0-9-8.postinstall CSWlibssl0-9-8.prototype-i386 CSWlibssl0-9-8.prototype-sparc
DISTFILES += CSWlibssl-dev.prototype-i386 CSWlibssl-dev.prototype-sparc
DISTFILES += CSWopenssl-utils.prototype 
DISTFILES += changelog.CSW README.CSW

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS README.ENGINE

# This patch add optimised build targets for some solaris isa, ie:
# solaris-386-cc, solaris-pentium-cc, solaris-pentium_pro-cc, solaris-sparcv9+vis-cc
PATCHFILES = more_configure_targets.patch

# Update openssl.cnf path in man page to follow opencsw standard
PATCHFILES += opencsw_paths.patch

# Let's always block some compromised CA, whatever the CA configured
# (patchs taken from Debian Package)
PATCHFILES += block_bad_certificates.patch

LICENSE=LICENSE

##### Build and installation information #####

# Sun Studio 12 incorrectly outputs v8plus code instead of
# v8 code under Solaris 10 so we use Sun Studio 12 update 1
ifneq ($(shell /usr/bin/uname -r),5.9)
	GARCOMPILER = SOS12U1
endif

# The list of instructions set for which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis sparcv9

# GAR wants and puts sparcv9 in lib/64 but openssl build system
# isn't the standard autoconf/automake one so we disable this
# relocation for now
ISALIBDIR_sparcv9 = .
libdir = /opt/csw/lib

# we include *.a files in the devel package so we don't want them excluded
MERGE_EXCLUDE_STATICLIBS = 

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-386-cc
pentium_OS_COMPILER	= solaris-pentium-cc
pentium_pro_OS_COMPILER	= solaris-pentium_pro-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparcv8_OS_COMPILER 		= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER		= solaris-sparcv9-cc
sparcv8plus+vis_OS_COMPILER	= solaris-sparcv9+vis-cc
sparcv9_OS_COMPILER		= solaris64-sparcv9-cc

CONFIGURE_ARGS = --prefix=$(prefix) shared $($(ISA)_OS_COMPILER) --install_prefix=$(DESTDIR)

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

# we include previous release of libraries file for comptability purpose
OLDLIBS                 = 0.9.7m

# support for pkcs11 engine http://blogs.sun.com/chichang1/entry/how_to_integrate_pkcs11_engine
ifdef PKCS11
	PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386
ifneq ($(shell /usr/bin/uname -r),5.9) 
	PATCHFILES += pkcs11_engine-0.9.8o.patch.2010-09-03
	CONFIGURE_ARGS += --pk11-libname=$(abspath /usr/lib/$(MM_LIBDIR)/libpkcs11.so) 
endif
endif 

TEST_SCRIPTS =

include gar/category.mk


pre-configure-modulated: 
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	@$(MAKECOOKIE)

# we remove every debug information except symbol table
# (should rather be done in the gar scripts)
post-install-modulated:
	echo " ==> Stripping libraries"
	chmod -R u+w $(DESTDIR)$(libdir)
	find $(DESTDIR)$(libdir) -name "*.so*" -exec strip -x '{}' ';'

install-changelog:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/changelog.CSW; \
	done	
	@$(MAKECOOKIE)

install-doc:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$CATALOGNAME; \
		(cd $(WORKSRC_FIRSTMOD)/ && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
		ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/README.CSW; \
	done
	@$(MAKECOOKIE)

install-certs: 
	[ -f $(PKGROOT)$(prefix)/ssl/openssl.cnf ] && \
		ginstall -D $(PKGROOT)$(prefix)/ssl/openssl.cnf $(PKGROOT)$(sysconfdir)/ssl/openssl.cnf.CSW

fix-paths:
	gsed -i -e 's,/usr/local/ssl/lib,/opt/csw/etc/ssl,' $(PKGROOT)$(mandir)/man1/ca.1
	gsed -i -e 's,/usr/local/ssl,/opt/csw/ssl,' $(PKGROOT)$(bindir)/c_rehash
	@$(MAKECOOKIE)

install-oldlibs: $(addprefix install-oldlibs-,$(OLDLIBS))
install-oldlibs-%:
	@echo " ==> Installing old libraries $* from archive oldlibs.$*-$(GARCH).tar.gz"
	cd $(PKGROOT) && gunzip -c $(CURDIR)/$(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz | tar xvf -
	@$(MAKECOOKIE)

pre-package: install-certs install-oldlibs install-changelog install-doc fix-paths
