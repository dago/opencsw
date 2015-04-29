# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-admin
VERSION = 1.1.38
GARTYPE = v2

DESCRIPTION = The 389 LDAP server Admin Tools
define BLURB
The enterprise-class Open Source LDAP server for Linux. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

BUNDLE = 389-ds

MASTER_SITES = https://git.fedorahosted.org/cgit/389/admin.git/snapshot/
DISTNAME  = admin-$(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSW389-admin.preremove

BUILD64_ONLY = 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

GARCOMPILER = SOS12U4

LICENSE = LICENSE

# GARFLAVOR=DBG
# LDAP_API=mozldap
LDAP_API=openldap

PATCHFILES += 0002-add-i386-platform-to-configure.ac.patch
PATCHFILES += 0003-correct-initscript-and-http.conf.in.patch
PATCHFILES += 0004-change-include-preferences-in-Makefile.am.patch
PATCHFILES += 0005-ctime_r-params-viewdata.c.patch

BUILD_DEP_PKGS += CSWnspr-dev
BUILD_DEP_PKGS += CSWlibnss-dev
BUILD_DEP_PKGS += CSW389-adminutil-dev
BUILD_DEP_PKGS += CSWapache24-dev
BUILD_DEP_PKGS += CSWap2modnss
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWsasl-dev
BUILD_DEP_PKGS_openldap += CSWopenldap-dev
BUILD_DEP_PKGS += CSWlibtool CSWautoconf CSWautomake
BULID_DEP_PKGS += $(BUILD_DEP_PKGS_&(LDAP_API))

PACKAGES += CSWlibds-admin-serv0
CATALOGNAME_CSWlibds-admin-serv0 = libds_admin_serv0
PKGFILES_CSWlibds-admin-serv0 += $(call baseisadirs,$(libdir),libds-admin-serv\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibds-admin-serv0 += $(DESCRIPTION), libds-admin-serv.so.0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibadmsslutil0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibiconv2

PACKAGES += CSW389-admin-dev
# OBSOLETED_BY_CSW389-admin-dev = CSW389admin-dev
SPKG_DESC_CSW389-admin-dev += $(DESCRIPTION), development files
PKGFILES_CSW389-admin-dev += /opt/csw/lib/libds-admin-serv.so
RUNTIME_DEP_PKGS_CSW389-admin-dev += CSWlibds-admin-serv0

PACKAGES += CSW389-admin
# OBSOLETED_BY_CSW389-admin = CSW389admin
SPKG_DESC_CSW389-admin += $(DESCRIPTION)
INITSMF = /etc/opt/csw/init.d/dirsrv-admin
RUNTIME_DEP_PKGS_CSW389-admin += CSWap2modnss
# RUNTIME_DEP_PKGS_CSW389-admin += CSWlibldif60
RUNTIME_DEP_PKGS_CSW389-admin += CSWperl
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibadmsslutil0
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibplc4
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibnspr4
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibds-admin-serv0
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibadminutil0
# RUNTIME_DEP_PKGS_CSW389-admin += CSWlibldap60
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibsmime3
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibssl3
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibnss3
RUNTIME_DEP_PKGS_CSW389-admin += CSW389-admin-console
RUNTIME_DEP_PKGS_CSW389-admin += CSW389-ds-console
RUNTIME_DEP_PKGS_CSW389-admin += CSWpm-netaddr-ip
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibplds4
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSW389-admin_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSW389-admin += $(RUNTIME_DEP_PKGS_CSW389-admin_$(GARCH))

CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSWap2modnss
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSW389-admin-console
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSW389-ds-console
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSWpm-netaddr-ip
# hint from Maciej: let checkpkg fail the check at the package build stage. If this was the only error shown, you know that it will go away when you upload the right set of packages, so you can upload safely.
# CHECKPKG_OVERRIDES_CSW389-admin += unidentified-dependency|CSW389-admin-console
# CHECKPKG_OVERRIDES_CSW389-admin += unidentified-dependency|CSW389-ds-console

# remove -I/opt/csw/include
CPPFLAGS = 

EXTRA_LINKER_FLAGS = -xnorunpath -norunpath -liconv
EXTRA_CONFIGURE_ENV=PATH=/opt/csw/gnu:$(PATH)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_openldap += --with-openldap-inc=$(includedir)
CONFIGURE_ARGS_openldap += --with-openldap=$(prefix)
CONFIGURE_ARGS += --with-icu-inc=$(includedir) 
CONFIGURE_ARGS += --with-icu-lib=$(libdir)
CONFIGURE_ARGS += --with-icu-bin=$(bindir)
CONFIGURE_ARGS += --with-sasl-inc=$(includedir)/sasl 
CONFIGURE_ARGS += --with-sasl-lib=$(libdir)
CONFIGURE_ARGS += --with-nspr-lib=$(libdir)
CONFIGURE_ARGS += --with-nspr-inc=$(includedir)/nspr 
CONFIGURE_ARGS += --with-nss-lib=$(libdir)
CONFIGURE_ARGS += --with-nss-inc=$(includedir)/nss 
CONFIGURE_ARGS_32 += --with-apxs=/opt/csw/bin/apxs
CONFIGURE_ARGS_64 += --with-apxs=/opt/csw/bin/$(BUILD_ISAS)/apxs
CONFIGURE_ARGS_32 += --with-httpd=/opt/csw/sbin/httpd
CONFIGURE_ARGS_32 += --with-modnss-lib=/opt/csw/lib/apache2/modules
CONFIGURE_ARGS_64 += --with-httpd=/opt/csw/sbin/$(BUILD_ISAS)/httpd
CONFIGURE_ARGS_64 += --with-modnss-lib=/opt/csw/lib/$(BUILD_ISAS)/apache2/modules
CONFIGURE_ARGS += --with-modnss-bin=/opt/csw/sbin
# CONFIGURE_ARGS += --with-adminutil=/opt/csw
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL_$(BUILD_ISAS)))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(LDAP_API))


include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm -f ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)
