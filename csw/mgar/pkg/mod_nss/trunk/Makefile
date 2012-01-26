# $Id$
#
NAME = mod_nss
VERSION = 1.0.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Apache2 Crypto Modul using Mozilla NSS
define BLURB
An Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries.  This supports SSLv3/TLSv1 including support for client certificate authentication.  NSS provides web applications with a FIPS 140 certified crypto provider and support for a full range of PKCS11 devices.
endef

LICENSE = LICENSE

PACKAGES = CSWap2modnss

MASTER_SITES = http://port389.org/sources
# MASTER_SITES = http://directory.fedoraproject.org/sources
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWap2modnss.postinstall
DISTFILES += CSWap2modnss.preremove

# BUILD64_LIBS_ONLY = 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
GARCOMPILER = SOS12U2

TEST_SCRIPTS = 
EXTRA_LINKER_FLAGS = -xnorunpath -norunpath

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_OPT += --with-apr-config
CONFIGURE_ARGS_OPT += --with-apxs=/opt/csw/apache2/sbin/apxs
CONFIGURE_ARGS_OPT += --with-nss-lib=/opt/csw/lib/64
CONFIGURE_ARGS_OPT += --with-nss-inc=/opt/csw/include/nss 
CONFIGURE_ARGS_OPT += --with-nspr-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-nspr-inc=/opt/csw/include/nspr
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

INSTALL_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

RUNTIME_DEP_PKGS_CSWap2modnss += CSWapache2
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibnss3
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibplds4
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibplc4
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibssl3


include gar/category.mk

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_CONF      = $(DESTDIR)$(AP2_ROOT)/etc
AP2_SBIN      = $(DESTDIR)$(AP2_ROOT)/sbin

install-custom:
	@ginstall -m 755 -d $(AP2_LIBEXEC)
	@ginstall -m 755 -d $(AP2_CONF)
	@ginstall -m 755 -d $(AP2_SBIN)
	@ginstall -c -m 755 $(WORKSRC)/.libs/libmodnss.so $(AP2_LIBEXEC)
	@ginstall -c -m 644 $(WORKSRC)/nss.conf $(AP2_CONF)
	@ginstall -c -m 755 $(WORKSRC)/nss_pcache $(AP2_SBIN)
	@ginstall -c -m 755 $(WORKSRC)/gencert $(AP2_SBIN)
	$(MAKECOOKIE)

COPYFILES = CONFIGURE CHANGES README
