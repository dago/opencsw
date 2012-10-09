# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-admin
VERSION = 1.1.30
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = The 389 LDAP server Admin Tools
define BLURB
The enterprise-class Open Source LDAP server for Linux. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

MASTER_SITES = http://port389.org/sources/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSW389-admin.preremove

# BUILD64	= 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

GARCOMPILER = SOS12U3

LICENSE = LICENSE LICENSE.GPLv2

# GARFLAVOR=DBG

PATCHFILES += 0002-add-i386-platform-to-configure.ac.patch
PATCHFILES += 0003-correct-initscript-and-http.conf.in.patch
PATCHFILES += 0004-change-include-preferences-in-Makefile.am.patch

PACKAGES += CSWlibds-admin-serv0
CATALOGNAME_CSWlibds-admin-serv0 = libds_admin_serv0
PKGFILES_CSWlibds-admin-serv0 += $(call baseisadirs,$(libdir),libds-admin-serv\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibds-admin-serv0 += $(DESCRIPTION), libds-admin-serv.so.0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibadmsslutil0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibds-admin-serv0 += CSWlibiconv2

PACKAGES += CSW389-admin-dev
OBSOLETED_BY_CSW389-admin-dev = CSW389admin-dev
SPKG_DESC_CSW389-admin-dev += $(DESCRIPTION), development files
PKGFILES_CSW389-admin-dev += /opt/csw/lib/libds-admin-serv.so
RUNTIME_DEP_PKGS_CSW389-admin-dev += CSWlibds-admin-serv0

PACKAGES += CSW389-admin
OBSOLETED_BY_CSW389-admin = CSW389admin
SPKG_DESC_CSW389-admin += $(DESCRIPTION)
INITSMF = /etc/opt/csw/init.d/dirsrv-admin
RUNTIME_DEP_PKGS_CSW389-admin += CSWap2worker
RUNTIME_DEP_PKGS_CSW389-admin += CSWap2modnss
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibprldap60
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibldif60
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibicudata48
RUNTIME_DEP_PKGS_CSW389-admin += CSWperl
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibadmsslutil0
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibplc4
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibssldap60
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibnspr4
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibds-admin-serv0
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibplds4
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibldap60
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibsoftokn3
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibsmime3
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibiconv2
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibssl3
RUNTIME_DEP_PKGS_CSW389-admin += CSWlibnss3
RUNTIME_DEP_PKGS_CSW389-admin += CSW389-admin-console
RUNTIME_DEP_PKGS_CSW389-admin += CSW389-ds-console
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSWap2modnss
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSWap2worker
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSW389-admin-console
CHECKPKG_OVERRIDES_CSW389-admin += surplus-dependency|CSW389-ds-console
CHECKPKG_OVERRIDES_CSW389-admin += unidentified-dependency|CSW389-admin-console
CHECKPKG_OVERRIDES_CSW389-admin += unidentified-dependency|CSW389-ds-console

# remove -I/opt/csw/include
CPPFLAGS = 

EXTRA_LINKER_FLAGS = -xnorunpath -norunpath -liconv

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ldapsdk-inc=/opt/csw/include/dirsrv 
CONFIGURE_ARGS += --with-ldapsdk-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-icu-inc=/opt/csw/include 
CONFIGURE_ARGS += --with-icu-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-icu-bin=/opt/csw/bin 
CONFIGURE_ARGS += --with-sasl-inc=/opt/csw/include/sasl 
CONFIGURE_ARGS += --with-sasl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-nss-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-nss-inc=/opt/csw/include/nss 
CONFIGURE_ARGS += --with-apxs=/opt/csw/apache2/sbin/apxs
CONFIGURE_ARGS += --with-httpd=/opt/csw/apache2/sbin/httpd
CONFIGURE_ARGS += --with-modnss-lib=/opt/csw/apache2/libexec
CONFIGURE_ARGS += --with-modnss-bin=/opt/csw/apache2/sbin

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)
