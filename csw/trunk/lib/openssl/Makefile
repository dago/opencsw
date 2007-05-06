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
DISTFILES  = $(GARNAME)-$(GARVERSION)$(RELEASE).tar.gz 
DISTFILES += $(call admfiles,CSWopenssl,checkinstall depend preremove prototype-i386 prototype-sparc)
DISTNAME   = $(GARNAME)-$(GARVERSION)$(RELEASE)

# We will include the following previous versions of libraries 
# for comptatibility reasons
OLD_VERSIONS	= 0.9.7m 0.9.6m

# As we need to compile several versions, we need to have
# directories (or files) version dependant
WORKDIR	    	= $(WORKROOTDIR)/$(DESTIMG).d/$(GARVERSION)/$(ISA)
COOKIEROOTDIR	= cookies.$(GARVERSION).$(ISA)
CHECKSUM_FILE	= checksums.$(GARVERSION)

# add the solaris-386-cc, solaris-pentium-cc,... targets
PATCHFILES = openssl.$(GARVERSION).patch

# The list of optimized libraries we will compile
# by arch
i386_ISALIST		= pentium amd64
sparc_ISALIST		= sparcv8plus sparcv9

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-386-cc
pentium_OS_COMPILER	= solaris-pentium-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparc_OS_COMPILER 	= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER	= solaris-sparcv9-cc
sparcv9_OS_COMPILER	= solaris64-sparcv9-cc

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

INSTALL_ARGS += INSTALL_PREFIX=$(DESTDIR)

pre-configure: 
	echo " ==> Creating configure script $(ISA) $(OS_COMPILER)"
	cd $(WORKSRC) && ln -nf Configure configure
	$(MAKECOOKIE)

install-certs: build install-$(WORKSRC)/Makefile
	cp -r $(WORKSRC)/certs/* $(DESTDIR)$(prefix)/ssl/certs
	$(MAKECOOKIE)


# before making the package, we also need to install:
# 	- optimized build of libraries and binaries (pentium, sparcv9, ...)
# 	- previous build of libraries for compatibility reasons
post-install: install-certs
	( for ISA in $($(GARCH)_ISALIST); do \
		gmake GARVERSION=$(GARVERSION) RELEASE=$(RELEASE) ISA=$$ISA install-optimized-lib-and-bin; \
		for VERSION in $(OLD_VERSIONS); do \
			GARVERSION=`echo $$VERSION | sed -e 's/[a-z]//g'`; \
			RELEASE=`echo $$VERSION | sed -e 's/[^a-z]//g'`; \
			gmake GARVERSION=$$GARVERSION RELEASE=$$RELEASE ISA=$$ISA install-old-libraries; \
		done; \
	  done )

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

clean-everything: clean
	( for ISA in "" $($(GARCH)_ISALIST); do \
		gmake GARVERSION=$(GARVERSION) RELEASE=$(RELEASE) ISA=$$ISA clean; \
		for VERSION in $(OLD_VERSIONS); do \
			GARVERSION=`echo $$VERSION | sed -e 's/[a-z]//g'`; \
			RELEASE=`echo $$VERSION | sed -e 's/[^a-z]//g'`; \
			gmake GARVERSION=$$GARVERSION RELEASE=$$RELEASE ISA=$$ISA clean; \
		done; \
	  done )

