GARNAME = openssl
GARVERSION = 0.9.8j
CATEGORIES = lib

OPENSSL_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z]//g')
OPENSSL_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/[^a-z]//g')

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

MASTER_SITES = http://www.openssl.org/source/ http://openssl.org/news/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*[a-z]?).tar.gz

DISTNAME   = $(GARNAME)-$(GARVERSION)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWossl,depend prototype)
DISTFILES += $(call admfiles,CSWosslrt,checkinstall preinstall postinstall depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWossldevel,depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWosslutils,depend prototype)
DISTFILES += changelog.CSW README.CSW
DISTFILES += i.conf r.conf

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS README.ENGINE

SPKG_CLASSES = none conf

PATCHFILES = openssl.$(OPENSSL_VERSION).patch

GARCOMPILER = SOS11

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

# we redefine the default merge exclude so *.a files are not excluded
MERGE_EXCLUDE_DEFAULT = $(MERGE_EXCLUDE_INFODIR)

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

SKIPTEST = 1


# support for pkcs11 engine http://blogs.sun.com/chichang1/entry/how_to_integrate_pkcs11_engine
ifdef PKCS11
	PATCHFILES += pkcs11_engine-0.9.8h.patch.2008-07-29
	ifeq ($(GARCH),sparc)
		ifeq ($(ISA),sparcv9)
			CONFIGURE_ARGS += --pk11-libname=/usr/lib/sparcv9/libpkcs11.so
		else
			CONFIGURE_ARGS += --pk11-libname=/usr/lib/libpkcs11.so
		endif
	else
		ifeq ($(ISA),amd64)
			CONFIGURE_ARGS += --pk11-libname=/usr/lib/sparcv9/libpkcs11.so
		else
			CONFIGURE_ARGS += --pk11-libname=/usr/lib/libpkcs11.so
		endif
	endif
endif 

include gar/category.mk

# we redefine the timestamp to fulfill opencsw standard
SPKG_VERSION := $(OPENSSL_VERSION)
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(OPENSSL_RELEASE)


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
	ginstall -D $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/changelog.CSW $(SPKG_PKGBASE)/changelog.CSW
	@$(MAKECOOKIE)

install-doc:
	cd $(WORKSRC_FIRSTMOD)/ && ginstall $(DOCFILES) $(SPKG_PKGBASE)/
	ginstall -D $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/README.CSW $(SPKG_PKGBASE)/README.CSW
	@$(MAKECOOKIE)

install-certs: 
	[ -f $(PKGROOT)$(prefix)/ssl/openssl.cnf ] && \
		ginstall -D $(PKGROOT)$(prefix)/ssl/openssl.cnf $(PKGROOT)$(sysconfdir)/ssl/openssl.cnf

install-oldlibs: $(addprefix install-oldlibs-,$(OLDLIBS))
install-oldlibs-%:
	@echo " ==> Installing old libraries $* from archive oldlibs.$*-$(GARCH).tar.gz"
	cd $(PKGROOT) && gunzip -c $(CURDIR)/$(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz | tar xvf -
	@$(MAKECOOKIE)

post-merge: install-certs install-oldlibs install-changelog install-doc
