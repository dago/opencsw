GARNAME = openssl
GARVERSION = 0.9.8
GARREVISION = e
CATEGORIES = lib

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

MASTER_SITES = http://www.openssl.org/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)$(GARREVISION).tar.gz 
DISTFILES += $(call admfiles,CSWopenssl,checkinstall depend preremove prototype)
DISTNAME   = $(GARNAME)-$(GARVERSION)$(GARREVISION)

# We will compile older versions to include previous libraries
# for the sake of comptability, so we need to have the following
# directories (or files) version dependant
WORKDIR	    	= $(WORKROOTDIR)/$(DESTIMG).d/$(GARVERSION)
COOKIEROOTDIR	= cookies.$(GARVERSION)
CHECKSUM_FILE	= checksums.$(GARVERSION)

# add the solaris-386-cc, solaris-pentium-cc,... targets
PATCHFILES = openssl.$(GARVERSION).patch

# We will compile optimized version of libraries
i386_FLAVORS		 = pentium amd64
sparc_FLAVORS		 = sparcv8plus sparcv9

i386_CONFIGURE_OS_COMPILER	 	= solaris-386-cc
pentium_CONFIGURE_OS_COMPILER 		= solaris-pentium-cc
amd64_CONFIGURE_OS_COMPILER	 	= solaris64-x86_64-cc

sparc_CONFIGURE_OS_COMPILER	 	= solaris-sparcv8-cc
sparcv8plus_CONFIGURE_OS_COMPILER	= solaris-sparcv9-cc
sparcv9_CONFIGURE_OS_COMPILER		= solaris64-sparcv9-cc

CONFIGURE_ARGS = --prefix=$(prefix) shared

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
CLEAN_SCRIPTS = custom

include ../category.mk

CFLAGS   += -mt -xstrconst
CXXFLAGS += -noex -mt



INSTALL_ARGS += INSTALL_PREFIX=$(DESTDIR)

post-patch: flavors-post-patch

pre-configure: flavors-pre-configure
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	$(MAKECOOKIE)

configure-custom: flavors-configure
	gmake CONFIGURE_ARGS="$(CONFIGURE_ARGS) $($(GARCH)_CONFIGURE_OS_COMPILER)" configure-$(WORKSRC)/configure

build-custom: build-$(WORKSRC)/Makefile flavors-build

install-custom: install-$(WORKSRC)/Makefile flavors-install
	cp -r $(WORKSRC)/certs/* $(DESTDIR)$(prefix)/ssl/certs
	$(MAKECOOKIE)

# That's not finished ! we now compile and install 
# older version of libraries
post-install:
	gmake GARVERSION=0.9.7 GARREVISION=m install_lib
	gmake GARVERSION=0.9.6 GARREVISION=m install_lib


# This target is used to only install libraries from 
# previous openssl versions included in the package
install_lib: build flavors-install_lib
	ginstall -d $(DESTDIR)$(libdir) 
	ginstall -d $(DESTDIR)$(bindir) 
	cd $(WORKSRC) && cp -f libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) $(DESTDIR)$(libdir)/
	$(MAKECOOKIE)


# we should also clean previous build
clean-custom: clean-all
	gmake GARVERSION=0.9.7 GARREVISION=m clean-all
	gmake GARVERSION=0.9.6 GARREVISION=m clean-all

#
# The following targets deals with generation of 
# pentium/amd64/sparcv9/... optimized libraries and binaries
#
flavors-%:
	@( if [ "$*" = "configure" ]; then \
       	  	TARGET="/$*"; \
	   elif [ "$*"  = "pre-configure" ] || [ "$*" = "post-patch" ]; then \
	   	TARGET=""; \
	   else \
	   	TARGET="/Makefile"; \
	   fi; \
	   for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-$*-$$FLAVOR$$TARGET; \
	   done )

flavor-post-patch-%:
	echo " ==> Creating $* flavor"
	rm -rf $(WORKSRC).$*
	gcp -a $(WORKSRC) $(WORKSRC).$*
	$(MAKECOOKIE)

flavor-pre-configure-%:
	echo " ==> Creating configure script for $* flavor"
	cd $(WORKSRC).$* && ln -nf Configure configure
	$(MAKECOOKIE)

flavor-configure-%/configure:
	gmake CONFIGURE_ARGS="$(CONFIGURE_ARGS) $($(*)_CONFIGURE_OS_COMPILER)" configure-$(WORKSRC).$*/configure

flavor-build-%/Makefile:
	gmake build-$(WORKSRC).$*/Makefile 

flavor-install-%/Makefile:
	@echo " ==> Installing libraries and binaries from $(WORKSRC).$*"
	ginstall -d $(DESTDIR)$(bindir)/$* 
	ginstall -d $(DESTDIR)$(libdir)/$* 
	cd $(WORKSRC).$* && cp -f libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) libcrypto.a libssl.a $(DESTDIR)$(libdir)/$*
	cd $(WORKSRC).$* && cp -f apps/openssl $(DESTDIR)$(bindir)/$*
	$(MAKECOOKIE)

flavor-install_lib-%/Makefile:
	@echo " ==> Installing libraries from $(WORKSRC).$*"
	ginstall -d $(DESTDIR)$(libdir)/$* 
	cd $(WORKSRC).$* && cp -f libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) $(DESTDIR)$(libdir)/$*
	$(MAKECOOKIE)


