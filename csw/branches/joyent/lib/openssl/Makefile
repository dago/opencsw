GARNAME = openssl
GARVERSION = 0.9.7d
CATEGORIES = lib

SPKG_PKGNAME = CSWopenssl
SPKG_BITNAME = openssl

DESCRIPTION = The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

MASTER_SITES = http://www.openssl.org/source/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# Don't ask for confirmation about compile config
PATCHFILES = dontask.diff

CONFIGURE_ARGS = --prefix=$(prefix) shared zlib threads

include ../category.mk

CFLAGS   += -mt -xstrconst
CXXFLAGS += -noex -mt

pre-configure: 
	(cd $(WORKSRC); ln -sf config configure)
	$(MAKECOOKIE)
