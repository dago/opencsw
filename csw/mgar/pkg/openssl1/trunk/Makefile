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

GARNAME = openssl
GARVERSION = 1.0.0-beta3
CATEGORIES = lib

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

PACKAGES = CSWossl1rt CSWossl1devel CSWossl1utils

CATALOGNAME_CSWossl1rt = openssl1_rt
REQUIRED_PKGS_CSWossl1rt = CSWcacertificates
SPKG_DESC_CSWossl1rt = Openssl 1.0 runtime libraries
PKGFILES_CSWossl1rt = $(libdir).*\.so(\.\d+)*
PKGFILES_CSWossl1rt += $(sysconfdir)/etc/ssl/private $(prefix)/ssl/private $(prefix)/ssl/certs /etc/$(prefix)/ssl/private
PKGFILES_CSWossl1rt += $(docdir)/openssl1_rt/.* 

CATALOGNAME_CSWossl1devel = openssl1_devel
REQUIRED_PKGS_CSWossl1devel = CSWossl1rt
SPKG_DESC_CSWossl1devel = Openssl 1.0 development support files
PKGFILES_CSWossl1devel = $(PKGFILES_DEVEL) 
PKGFILES_CSWossl1devel += $(docdir)/openssl1_devel/.*

CATALOGNAME_CSWossl1utils = openssl1_utils
REQUIRED_PKGS_CSWossl1utils = CSWossl1rt
SPKG_DESC_CSWossl1utils = Openssl 1.0 binaries and related tools
SPKG_CLASSES_CSWossl1utils = none cswpreserveconf
PKGFILES_CSWossl1utils = $(bindir)/[^/]* $(mandir)/man1/.* $(mandir)/man5/.* $(mandir)/man7/.* 
PKGFILES_CSWossl1utils += $(prefix)/ssl/misc/.* 
PKGFILES_CSWossl1utils += $(prefix)/ssl/openssl\.cnf $(sysconfdir)/ssl/openssl\.cnf.*
PKGFILES_CSWossl1utils += $(docdir)/openssl1_utils/.*

PROTOTYPE_MODIFIERS = conf
PROTOTYPE_FILES_conf = $(sysconfdir)/ssl/openssl.cnf.CSW
PROTOTYPE_CLASS_conf = cswpreserveconf
PROTOTYPE_PERMS_conf = 0644


###### Upstream and opencsw files information #######

MASTER_SITES = http://www.openssl.org/source/ http://openssl.org/news/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*[a-z]?).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWossl1rt.checkinstall CSWossl1rt.preinstall CSWossl1rt.postinstall
DISTFILES += changelog.CSW README.CSW

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS README.ENGINE

# This patch add optimised build targets for some solaris isa, ie:
# solaris-pentium_pro-cc and solaris-sparcv9+vis-cc
PATCHFILES = more_configure_targets.patch


##### Build and installation information #####

# The list of instructions set for which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis sparcv9

# we don't yet use isaexec support so we disable
# isa relocation for default isa
NO_ISAEXEC = 1

# GAR wants and puts sparcv9 in lib/64 but openssl build system
# isn't the standard autoconf/automake one so we disable this
# relocation for now
ISALIBDIR_sparcv9 = .
libdir = /opt/csw/lib

# we include *.a files in the devel package so we don't want them excluded
MERGE_EXCLUDE_STATICLIBS = 

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
	ginstall -d $(PKGROOT)/etc/$(prefix)/ssl/private
	rm -rf $(PKGROOT)/$(prefix)/ssl/openssl.cnf && ln -s ../etc/ssl/openssl.cnf $(PKGROOT)/$(prefix)/ssl/openssl.cnf
	rm -rf $(PKGROOT)/$(prefix)/ssl/certs && ln -s ../etc/ssl/certs $(PKGROOT)/$(prefix)/ssl/certs
	rm -rf $(PKGROOT)/$(prefix)/ssl/private && ln -s ../../../etc/opt/csw/ssl/private $(PKGROOT)/$(prefix)/ssl/private
	rm -rf $(PKGROOT)/$(prefix)/etc/ssl/private && ln -s ../../../../etc/opt/csw/ssl/private $(PKGROOT)/$(prefix)/etc/ssl/private 
	@$(MAKECOOKIE)

post-merge: install-certs install-changelog install-doc
