# $Id$
#
NAME = 389-adminutil
VERSION = 1.1.15
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = The enterprise-class Open Source LDAP server, libadminutil, libadmsslutil
define BLURB
The enterprise-class Open Source LDAP server for Linux|Unix. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

BUNDLE = 389-ds

LICENSE = LICENSE

MASTER_SITES = http://port389.org/sources
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
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibprldap60
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibldif60
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibssldap60
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibldap60
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibssl3
RUNTIME_DEP_PKGS_CSWlibadminutil0 += CSWlibsasl2-2


PACKAGES += CSWlibadmsslutil0
CATALOGNAME_CSWlibadmsslutil0 = libadmsslutil0
SPKG_DESC_CSWlibadmsslutil0 += $(DESCRIPTION), libadmsslutil
PKGFILES_CSWlibadmsslutil0 +=  $(call baseisadirs,$(libdir),libadmsslutil\.so(\.\d+)+)
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibprldap60
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibldif60
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibssldap60
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibldap60
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibssl3
RUNTIME_DEP_PKGS_CSWlibadmsslutil0 += CSWlibsasl2-2

PACKAGES += CSW389-adminutil-dev
CATALOGNAME_CSW389-adminutil-dev = 389_adminutil_dev
ARCHALL_CSW389-adminutil-dev = 1
SPKG_DESC_CSW389-adminutil-dev += $(DESCRIPTION), development files
# PKGFILES_CSW389-adminutil-dev += $(PKGFILES_DEV)
# PKGFILES_CSW389-adminutil-dev += $(call baseisadirs,$(libdir),libadminutil\.so)
# PKGFILES_CSW389-adminutil-dev += $(call baseisadirs,$(libdir),libadmsslutil\.so)
# PKGFILES_CSW389-adminutil-dev += $(call baseisadirs,$(libdir)/pkgconfig,389adminutil\.pc)
RUNTIME_DEP_PKGS_CSW389-adminutil-dev += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSW389-adminutil-dev += CSWlibadmsslutil0
CHECKPKG_OVERRIDES_CSW389-adminutil-dev += archall-devel-package
CHECKPKG_OVERRIDES_CSW389-adminutil-dev += file-with-bad-content|/usr/share|root/opt/csw/include/libadminutil/resource.h


TEST_SCRIPTS = 
EXTRA_LINKER_FLAGS = -xnorunpath -norunpath

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_OPT += --with-ldapsdk-inc=/opt/csw/include/dirsrv 
CONFIGURE_ARGS_OPT += --with-ldapsdk-lib=/opt/csw/lib 
CONFIGURE_ARGS_OPT += --with-icu-inc=/opt/csw/include 
CONFIGURE_ARGS_OPT += --with-icu-lib=/opt/csw/lib 
CONFIGURE_ARGS_OPT += --with-icu-bin=/opt/csw/bin 
CONFIGURE_ARGS_OPT += --with-sasl-inc=/opt/csw/include/sasl 
CONFIGURE_ARGS_OPT += --with-sasl-lib=/opt/csw/lib 
CONFIGURE_ARGS_OPT += --with-nss-lib=/opt/csw/lib/64
CONFIGURE_ARGS_OPT += --with-nss-inc=/opt/csw/include/nss 
CONFIGURE_ARGS_OPT += --with-nspr-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-nspr-inc=/opt/csw/include/nspr
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# CHECKPKG_OVERRIDES_CSWlibadmsslutil0 += pkginfo-opencsw-repository-uncommitted
# CHECKPKG_OVERRIDES_CSWlibadminutil0 += pkginfo-opencsw-repository-uncommitted
# CHECKPKG_OVERRIDES_CSW389-adminutil-dev += pkginfo-opencsw-repository-uncommitted
include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)

