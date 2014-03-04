# $Id$
#
NAME = 389-adminutil
VERSION = 1.1.18
GARTYPE = v2

DESCRIPTION = The enterprise-class Open Source LDAP server, libadminutil, libadmsslutil
define BLURB
The enterprise-class Open Source LDAP server for Linux|Unix. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

BUNDLE = 389-ds

LICENSE = LICENSE

MASTER_SITES = http://port389.org/sources/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# BUILD64 = 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
GARCOMPILER = SOS12U2

PACKAGES += CSWlibadminutil0
CATALOGNAME_CSWlibadminutil0 = libadminutil0
SPKG_DESC_CSWlibadminutil0 += $(DESCRIPTION), libadminutil
PKGFILES_CSWlibadminutil0 +=  $(call baseisadirs,$(libdir),libadminutil\.so(\.\d+)+)
PKGFILES_CSWlibadminutil0 +=  $(call baseisadirs,$(sharedstatedir),.*\.res)
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibadminutil0_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibadminutil0_sparc += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWlibadminutil0_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibadminutil0 += $(RUNTIME_DEP_PKGS_CSWlibadminutil0_$(GARCH))

PACKAGES += CSWlibadmsslutil0
CATALOGNAME_CSWlibadmsslutil0 = libadmsslutil0
SPKG_DESC_CSWlibadmsslutil0 += $(DESCRIPTION), libadmsslutil
PKGFILES_CSWlibadmsslutil0 +=  $(call baseisadirs,$(libdir),libadmsslutil\.so(\.\d+)+)
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibssl3
RUNTIME_DEP_PKGS_CSWlibadmsslutil0_sparc += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibadmsslutil0_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibadmsslutil0_sparc += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWlibadmsslutil0_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += $(RUNTIME_DEP_PKGS_CSWlibadmsslutil0_$(GARCH))

PACKAGES += CSW389-adminutil-dev
CATALOGNAME_CSW389-adminutil-dev = 389_adminutil_dev
ARCHALL_CSW389-adminutil-dev = 1
SPKG_DESC_CSW389-adminutil-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSW389-adminutil-dev += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSW389-adminutil-dev += CSWlibadmsslutil0
CHECKPKG_OVERRIDES_CSW389-adminutil-dev += archall-devel-package
CHECKPKG_OVERRIDES_CSW389-adminutil-dev += file-with-bad-content|/usr/share|root/opt/csw/include/libadminutil/resource.h


TEST_SCRIPTS = 
EXTRA_LINKER_FLAGS = -xnorunpath -norunpath

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --with-ldapsdk-inc=$(includedir)/dirsrv 
# CONFIGURE_ARGS += --with-ldapsdk-lib=$(libdir)
CONFIGURE_ARGS += --with-openldap=$(prefix)
CONFIGURE_ARGS += --with-openldap-inc=$(includedir)
CONFIGURE_ARGS += --with-icu-inc=$(includedir)
CONFIGURE_ARGS += --with-icu-lib=$(libdir)
CONFIGURE_ARGS += --with-icu-bin=$(bindir)
CONFIGURE_ARGS += --with-sasl-inc=$(includedir)/sasl 
CONFIGURE_ARGS += --with-sasl-lib=$(libdir)
CONFIGURE_ARGS += --with-nss-lib=$(libdir)
CONFIGURE_ARGS += --with-nss-inc=$(includedir)/nss 
CONFIGURE_ARGS += --with-nspr-lib=$(libdir)
CONFIGURE_ARGS += --with-nspr-inc=$(includedir)/nspr

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)

