# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jss
MAJOR_VERSION = 4
FULLVERSION = 4.3.2
VERSION = 4.2.6
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = Mozilla SSL SDK for Java
define BLURB
Network Security Services for Java (JSS) is a Java interface to NSS. JSS supports most of the security standards and encryption technologies supported by NSS. JSS also provides a pure Java interface for ASN.1 types and BER/DER encoding.

JSS offers a implementation of Java SSL sockets that uses NSS's SSL/TLS implementation rather than Sun's JSSE implementation.  You might want to use JSS own SSL classes if you want to use some of the capabilities found in NSS's SSL/TLS library but not found in JSSE.

NSS is the cryptographic module where all cryptographic operations are performed. JSS essentially provides a Java JNI bridge to NSS C shared libraries. When NSS is put in FIPS mode, JSS ensures FIPS compliance by ensuring that all cryptographic operations are performed by the NSS cryptographic module.

endef
VENDOR_URL=https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/JSS

GARFLAVOR = OPT
BUILD64 = 1

# MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/mozilla.org/mozilla.org/mozilla.org/security/jss/releases/JSS_4_3_2_RTM/
# DISTFILES  = $(NAME)$(MAJOR_VERSION).jar
DISTFILES += COPYING
DISTFILES += $(DISTNAME).tar.gz

PACKAGES = CSWjss4
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

PATCHFILES += 0005-jss-key_pair_usage_with_op_flags.patch
PATCHFILES += 0007-jss-javadocs-param.patch
PATCHFILES += 0008-jss-ipv6.patch
PATCHFILES += 0001-jss-ECC-pop.patch
PATCHFILES += 0006-jss-loadlibrary.patch
PATCHFILES += 0009-jss-ocspSettings.patch
PATCHFILES += 0010-jss-ECC_keygen_byCurveName.patch
PATCHFILES += 0011-jss-VerifyCertificate.patch
PATCHFILES += 0012-jss-bad-error-string-pointer.patch
PATCHFILES += 0013-jss-VerifyCertificateReturnCU.patch
PATCHFILES += 0014-jss-ECC-HSM-FIPS.patch
PATCHFILES += 0016-jss-eliminate-native-compiler-warnings.patch
PATCHFILES += 0015-jss-eliminate-java-compiler-warnings.patch
PATCHFILES += 0017-jss-PKCS12-FIPS.patch
PATCHFILES += 0002-jss-eliminate-native-coverity-defects.patch
PATCHFILES += 0018-jss-PBE-PKCS5-V2-secure-P12.patch
PATCHFILES += 0019-jss-wrapInToken.patch
PATCHFILES += 0020-jss-HSM-manufacturerID.patch
PATCHFILES += 0021-jss-ECC-Phase2KeyArchivalRecovery.patch
PATCHFILES += 0022-jss-undo-JCA-deprecations.patch
PATCHFILES += 0003-jss-undo-BadPaddingException-deprecation.patch
PATCHFILES += 0004-jss-fixed-build-issue-on-F17-or-newer.patch
PATCHFILES += 0023-jss-SHA-OID-fix.patch
PATCHFILES += 0024-jss-RC4-strengh-verify.patch
PATCHFILES += 0025-jss-support-TLS1_1-TLS1_2.patch

PACKAGES = CSWjss4
CATALOGNAME_CSWjss4 = jss4
SPKG_DESC_CSWjss4 += $(DESCRIPTION), jss4.jar, libjss4.so

PACKAGES = CSWjss4-doc
CATALOGNAME_CSWjss4-doc = jss4_doc
PKGFILES_CSWjss4-doc = $(PKGFILES_DOC)
SPKG_DESC_CSWjss4-doc += $(DESCRIPTION), javadoc
ARCHALL_CSWjss4-doc = 1

WORKSRC = $(WORKDIR)
DISTDIR = mozilla/security/jss
LICENSE = COPYING

OBJ_PATH = $(shell uname -s)$(GAROSREL)_$(shell uname -m)_$(GARFLAVOR).OBJ

CONFIGURE_ARGS_OPT += BUILD_OPT=1
CONFIGURE_ARGS += NSPR_INCLUDE_DIR=$(shell pkg-config --cflags-only-I nspr | sed 's/-I//')
CONFIGURE_ARGS += NSPR_LIB_DIR=$(shell pkg-config --libs-only-L nspr | sed 's/-L//')
CONFIGURE_ARGS += NSS_INCLUDE_DIR=$(shell pkg-config --cflags-only-I nss | sed 's/-I//')
CONFIGURE_ARGS += NSS_LIB_DIR=$(shell pkg-config --libs-only-L nss | sed 's/-L//')
CONFIGURE_ARGS += JAVA_HOME=/usr/java
CONFIGURE_ARGS_64 += USE_64
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL_$(BUILD_ISAS)))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))
	
CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = jss
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom
JAVA_INSTALL_DIR = $(DESTDIR)$(datadir)/java/$(MM_LIBDIR)
EXTRA_INSTALL_ENV = PATH=$(PATH):/opt/csw/gnu

include gar/category.mk

build-jss:
	(cd $(WORKSRC) && \
	gmake -C mozilla/security/coreconf $(CONFIGURE_ARGS) && \
	gmake -C mozilla/security/jss $(CONFIGURE_ARGS) && \
	gmake -C mozilla/security/jss javadoc $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

install-custom: 
	(cd $(WORKSRC) && $(EXTRA_INSTALL_ENV) gmake -C mozilla/security/jss install $(CONFIGURE_ARGS))
	ginstall -d $(JAVA_INSTALL_DIR)
	ginstall -d $(DESTDIR)$(libdir)
	(cd $(WORKSRC)/mozilla/dist && \
	ginstall $(OBJ_PATH)/lib/libjss4.so $(DESTDIR)/$(libdir) && \
	ginstall xpclass.jar $(JAVA_INSTALL_DIR)/jss4.jar && \
        gcp -r jssdoc $(DESTDIR)/$(datadir)) 
	@$(MAKECOOKIE)

WORKSRC := $(WORKDIR)/$(DISTNAME)
DISTNAME := $(NAME)-$(VERSION)
