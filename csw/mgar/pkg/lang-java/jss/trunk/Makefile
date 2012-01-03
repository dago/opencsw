# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jss
MAJOR_VERSION = 4
FULLVERSION = 4.3.2
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = Mozilla SSL SDK for Java
define BLURB
Network Security Services for Java (JSS) is a Java interface to NSS. JSS supports most of the security standards and encryption technologies supported by NSS. JSS also provides a pure Java interface for ASN.1 types and BER/DER encoding.

JSS offers a implementation of Java SSL sockets that uses NSS's SSL/TLS implementation rather than Sun's JSSE implementation.  You might want to use JSS own SSL classes if you want to use some of the capabilities found in NSS's SSL/TLS library but not found in JSSE.

NSS is the cryptographic module where all cryptographic operations are performed. JSS essentially provides a Java JNI bridge to NSS C shared libraries. When NSS is put in FIPS mode, JSS ensures FIPS compliance by ensuring that all cryptographic operations are performed by the NSS cryptographic module.

https://developer.mozilla.org/En/JSS
endef



MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/mozilla.org/mozilla.org/mozilla.org/security/jss/releases/JSS_4_3_2_RTM
DISTFILES  = $(NAME)$(MAJOR_VERSION).jar
DISTFILES += COPYING

PACKAGES = CSWjss4
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386


ARCHALL = 1

CATALOGNAME_CSWjss4 = jss4

WORKSRC = $(WORKDIR)
DISTDIR = mozilla/security/jss
LICENSE = COPYING

# JAVA_HOME = /usr/j2sdk1.4.2_17

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(CATALOGNAME_CSWjss4).jar $(DESTDIR)$(datadir)/java
	@$(MAKECOOKIE)

