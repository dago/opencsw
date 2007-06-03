GARNAME = openssl
GARVERSION = 0.9.8
RELEASE = e
CATEGORIES = lib

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

MASTER_SITES = http://www.openssl.org/source/
DISTNAME   = $(GARNAME)-$(GARVERSION)$(RELEASE)
DISTFILES  = $(GARNAME)-$(GARVERSION)$(RELEASE).tar.gz 
DISTFILES += $(call admfiles,CSWossl,depend prototype)
DISTFILES += $(call admfiles,CSWosslrt,checkinstall depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWossldevel,depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWosslutils,depend prototype)
DISTFILES += changelog.CSW
DISTFILES += i.conf r.conf

SPKG_CLASSES = none conf

# We will include the following previous versions of libraries 
# for comptatibility reasons
OLD_VERSIONS	= 0.9.7m

# As we need to compile several versions, we need to have
# directories (or files) version dependant
WORKDIR	    	= $(WORKROOTDIR)/$(DESTIMG).d/$(GARVERSION)/$(ISA)
COOKIEROOTDIR	= cookies.$(GARVERSION).$(ISA)
CHECKSUM_FILE	= checksums.$(GARVERSION)

# add the solaris-386-cc, solaris-pentium-cc,... targets
PATCHFILES = openssl.$(GARVERSION).patch

# The list of optimized libraries we will compile
# by arch
i386_ISALIST		= pentium_pro amd64
sparc_ISALIST		= sparcv8plus+vis sparcv9

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-386-cc
pentium_OS_COMPILER	= solaris-pentium-cc
pentium_pro_OS_COMPILER	= solaris-pentium_pro-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparc_OS_COMPILER 		= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER		= solaris-sparcv9-cc
sparcv8plus+vis_OS_COMPILER	= solaris-sparcv9+vis-cc
sparcv9_OS_COMPILER		= solaris64-sparcv9-cc

# Let's determine the appropriate os/compiler couple
# to pass to the openssl Configure script
ifndef ISA
OS_COMPILER = $($(GARCH)_OS_COMPILER)
else
OS_COMPILER = $($(ISA)_OS_COMPILER)
NOISALIST   = 1
endif

CONFIGURE_ARGS = --prefix=$(prefix) shared $(OS_COMPILER)

include ../category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

CFLAGS   += -mt -xstrconst
CXXFLAGS += -noex -mt

# If we are building optimized libraries, we will install
# the libraries in $(libdir)/$(ISA) and will set the RUNPATH
# accordingly
ifdef ISA
LDOPT_LIBS = $(libdir)/$(ISA) 
LDFLAGS  += -L$(libdir)/$(ISA)
ISA_LIBDIR = $(ISA)
endif

CONFIGURE_ENV += PERL="/usr/bin/perl"

# By default, the install target put man page under
# /opt/csw/ssl/man, but we want them under /opt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

# Openssl Makefile use INSTALL_PREFIX variable
# instead of the commonly used DESTDIR
INSTALL_ARGS += INSTALL_PREFIX=$(DESTDIR)


pre-configure: 
	echo " ==> Creating configure script $(ISA) $(OS_COMPILER)"
	cd $(WORKSRC) && ln -nf Configure configure
	$(MAKECOOKIE)

install-certs: build install-$(WORKSRC)/Makefile
	cp -r $(WORKSRC)/certs/* $(DESTDIR)$(prefix)/ssl/certs
	$(MAKECOOKIE)

# we remove every debug information except symbol table
# (should rather be done in the gar scripts)
striplib:
	chmod -R u+w $(DESTDIR)$(libdir)
	strip -x $(DESTDIR)$(libdir)/*.so*
	( for ISA in $($(GARCH)_ISALIST); do \
		strip -x $(DESTDIR)$(libdir)/$$ISA/*.so*; \
	  done )
	chmod -R u+w $(DESTDIR)$(libdir)/engines
	strip -x $(DESTDIR)$(libdir)/engines/*.so*

# before making the package, we also need to install:
# 	- optimized build of libraries and binaries (pentium, sparcv9, ...)
# 	- previous build of libraries for compatibility reasons
#
# we also add write access to ensure library stripping will work
# 
post-install: install-certs 
	[ -f $(DESTDIR)$(prefix)/ssl/openssl.cnf ] && \
		ginstall -D $(DESTDIR)$(prefix)/ssl/openssl.cnf $(DESTDIR)$(sysconfdir)/ssl/openssl.cnf
	( for ISA in $($(GARCH)_ISALIST); do \
		gmake GARVERSION=$(GARVERSION) RELEASE=$(RELEASE) ISA=$$ISA install-optimized-lib-and-bin; \
	  done )
	( for VERSION in $(OLD_VERSIONS); do \
		GARVERSION=`echo $$VERSION | sed -e 's/[a-z]//g'`; \
		RELEASE=`echo $$VERSION | sed -e 's/[^a-z]//g'`; \
		for ISA in "" $($(GARCH)_ISALIST); do \
			gmake GARVERSION=$$GARVERSION RELEASE=$$RELEASE ISA=$$ISA install-old-libraries; \
		done; \
	  done )
	gmake striplib

# For optimized flavor build (pentium, sparvc9, ...), we only
# install binaries and libraries
install-optimized-lib-and-bin: build 
	@echo " ==> Installing optimized libraries and binaries from $(WORKSRC)"
	ginstall -d $(DESTDIR)$(libdir)/$(ISA)
	cd $(WORKSRC) && ginstall libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) libcrypto.a libssl.a $(DESTDIR)$(libdir)/$(ISA_LIBDIR)
	ginstall -d $(DESTDIR)$(bindir)/$(ISA_LIBDIR)
	cd $(WORKSRC) && ginstall apps/openssl $(DESTDIR)$(bindir)/$(ISA_LIBDIR)
	$(MAKECOOKIE)

# For previous versions build, we will only install the so files
install-old-libraries: build 
	@echo " ==> Installing old libraries from $(WORKSRC)"
	ginstall -d $(DESTDIR)$(libdir)/$(ISA_LIBDIR)
	cd $(WORKSRC) && ginstall libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) $(DESTDIR)$(libdir)/$(ISA_LIBDIR)
	$(MAKECOOKIE)

makesum-everything: makesum
	( for ISA in "" $($(GARCH)_ISALIST); do \
		gmake GARVERSION=$(GARVERSION) RELEASE=$(RELEASE) ISA=$$ISA makesum; \
		for VERSION in $(OLD_VERSIONS); do \
			GARVERSION=`echo $$VERSION | sed -e 's/[a-z]//g'`; \
			RELEASE=`echo $$VERSION | sed -e 's/[^a-z]//g'`; \
			gmake GARVERSION=$$GARVERSION RELEASE=$$RELEASE ISA=$$ISA makesum; \
		done; \
	  done )

clean-everything: clean
	( for ISA in "" $($(GARCH)_ISALIST); do \
		gmake GARVERSION=$(GARVERSION) RELEASE=$(RELEASE) ISA=$$ISA clean; \
		for VERSION in $(OLD_VERSIONS); do \
			GARVERSION=`echo $$VERSION | sed -e 's/[a-z]//g'`; \
			RELEASE=`echo $$VERSION | sed -e 's/[^a-z]//g'`; \
			gmake GARVERSION=$$GARVERSION RELEASE=$$RELEASE ISA=$$ISA clean; \
		done; \
	  done )

