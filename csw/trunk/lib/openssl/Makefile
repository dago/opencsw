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

i386_FLAVORS		 = pentium amd64
sparc_FLAVORS		 = sparcv8plus sparcv9

i386_CONFIGURE_TARGET	 = solaris-386-cc
pentium_CONFIGURE_TARGET = solaris-pentium-cc
amd64_CONFIGURE_TARGET	 = solaris64-x86_64-cc

sparc_CONFIGURE_TARGET	 = solaris-sparcv8-cc
sparcv8plus_CONFIGURE_TARGET	 = solaris-sparcv9-cc
sparcv9_CONFIGURE_TARGET	 = solaris64-sparcv9-cc


# add the solaris-386-cc, solaris-pentium-cc targets
PATCHFILES = openssl.patch

CONFIGURE_ARGS = --prefix=$(prefix) shared

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include ../category.mk

CFLAGS   += -mt -xstrconst
CXXFLAGS += -noex -mt

INSTALL_ARGS += INSTALL_PREFIX=$(DESTDIR)


flavor-post-patch-%:
	echo " ==> Creating $* flavor"
	rm -rf $(WORKSRC).$*
	cp -a $(WORKSRC) $(WORKSRC).$*
	$(MAKECOOKIE)

flavor-pre-configure-%:
	echo " ==> Creating configure script for  $* flavor"
	rm -f $(WORKSRC).$*/configure
	ln -s Configure $(WORKSRC).$*/configure
	$(MAKECOOKIE)

flavor-configure-%/configure:
	gmake CONFIGURE_ARGS="$(CONFIGURE_ARGS) $($(*)_CONFIGURE_TARGET)" configure-$(WORKSRC).$*/configure

flavor-build-%/Makefile:
	gmake build-$(WORKSRC).$*/Makefile 

flavor-install-%/Makefile:
	@echo " ==> Installing libraries and binaries from $(WORKSRC).$*"
	ginstall -d $(DESTDIR)$(libdir)/$* 
	ginstall -d $(DESTDIR)$(bindir)/$* 
	cd $(WORKSRC).$* && cp libcrypto.so.$(GARVERSION) libssl.so.$(GARVERSION) libcrypto.a libssl.a $(DESTDIR)$(libdir)/$*
	cd $(WORKSRC).$* && cp apps/openssl $(DESTDIR)$(bindir)/$*


post-patch:
	@( for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-post-patch-$$FLAVOR; \
	   done )

pre-configure:
	echo " ==> Creating configure script for  $* flavor"
	rm -f $(WORKSRC)/configure 
	ln -s Configure $(WORKSRC)/configure
	@( for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-pre-configure-$$FLAVOR; \
	   done )

configure-custom:
	gmake CONFIGURE_ARGS="$(CONFIGURE_ARGS) $($(GARCH)_CONFIGURE_TARGET)" configure-$(WORKSRC)/configure
	@( for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-configure-$$FLAVOR/configure; \
	   done )

build-custom: build-$(WORKSRC)/Makefile
	@( for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-build-$$FLAVOR/Makefile; \
	   done )
	

install-custom: install-$(WORKSRC)/Makefile
	@( for FLAVOR in $($(GARCH)_FLAVORS); do \
		gmake flavor-install-$$FLAVOR/Makefile \
	   done )

