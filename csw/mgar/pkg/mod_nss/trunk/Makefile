# $Id$
#
NAME = mod_nss
VERSION = 1.0.11
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Apache2 Crypto Modul using Mozilla NSS
define BLURB
An Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries.  This supports SSLv3/TLSv1 including support for client certificate authentication.  NSS provides web applications with a FIPS 140 certified crypto provider and support for a full range of PKCS11 devices.
endef

LICENSE = LICENSE

PACKAGES = CSWap2modnss

MAs://fedorahosted.org/released/$(NAME)/rt389.org/sources
# MASTER_SITES = http://directory.fedoraproject.org/sources
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWap2modnss.postinstall
DISTFILES += CSWap2mPATCHFILES += 0001-fix-ap_log_error-parameter-missmatch.patch
PATCHFILES += 0002-cleanup-includes.patch
PATCHFILES += 0003-remove-incl-protocol.patch

BUILD64BUILD64_LIBS_ONLY = 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS +
# GARCOMPILER = GCC4
GARCOMPILER = SOS12U4
# GARFLAVOR = DBG

BUILD_DEP_PKGS += CSWapache24-dev
BUILD_DEP_PKGS += CSWnspr-dev 
BUILD_DEP_PKGS += CSWlibnss-devOMPILER = SOS12U2

TEST_SCRIPTS = 
E_SOS12U4 = -xnorunpath -norunpath
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GARCOMPILER))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config
CONFIGURE_ARGS += --with-apxs=/opt/csw/bin/apxs
CONFIGURE_ARGS += --with-nss-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-nss-inc=/opt/csw/include/nss 
CONFIGURE_ARGS += --with-nspr-lib=/opt/csw/lib
CONFIGURE_ARGSONFIGURE_ARGS_OPT += --with-nspr-inc=/opt/csw/include/nspr
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

INSTALL_SCRIPTS = custom

# No test suite# STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

# RUNTIME_DEP_PKGS_CSWap2modnss += CSWapache24nss += CSWapache2
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibnss3
RUNTIME_DEP_PKGS_CSWap2mc4s += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWap2modnss += CSWlibssl3


include gar/category.mk# AP2_ROOT      = $(prefix)
AP2_LIBEXEC   = $(DESTDIR)$(libdir)/apache2/modules
AP2_CONF      = $(DESTDIR)$(sysconfdir)
AP2_SBIN      = $(DESTDIR)$(sbindir)

#	libtoolize --copy --force && \
#	automake --add-missing --copy --force-missing )
pre-configure:
	(cd $(WORKSRC) && \
	autoreconf --install )
	$(MAKECOOKIE))$(AP2_ROOT)/sbin

install-custom:
	@ginstall -m 755 -d $(AP2_LIBEXEC)
	@ginstall -m 755 -d $(AP2_CONF)
	@ginstall -m 755 -d $(AP2_SBIN)
	@ginstall -c -m 755 $(WORKSRC)/.libs/libmodnss.so $(AP2_LIBEXEC)
	@ginstall -c -m 644 $(WORKSRC)/nss.conf $(AP2_CONF)
	@ginstall -c -m 755 $(WORKSRC)/nss_pcache $(AP2_SBIN)
	@ginstall -c -m 755 $(WORKSRC)/gencert $(AP2_SBIN)
	$(MAKECOOKIE)

COPYFILES = CONFIGUR