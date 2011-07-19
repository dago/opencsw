NAME = apr-util
VERSION = 1.3.12
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE

PATCHFILES = 0001-Make-sure-to-find-newly-built-libs-earlier.patch

PACKAGES += CSWlibaprutil1-0
CATALOGNAME_CSWlibaprutil1-0 = libaprutil1_0
SPKG_DESC_CSWlibaprutil1-0 += Apache Portable Runtime Utilities, libaprutil-1.so.0
OBSOLETED_BY_CSWlibaprutil1-0 += CSWlibaprutil
PKGFILES_CSWlibaprutil1-0 += $(call baseisadirs,$(libdir),libaprutil-1\.so\.0\.3\.12)
PKGFILES_CSWlibaprutil1-0 += $(call baseisadirs,$(libdir),libaprutil-1\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWapr
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibexpat1


PACKAGES += CSWapr-util-dev
CATALOGNAME_CSWapr-util-dev = apr_util_dev
SPKG_DESC_CSWapr-util-dev += Apache Portable Runtime Utilities, libaprutil-dev
PKGFILES_CSWapr-util-dev += /opt/csw/lib/apr-util-1/apr_dbd_odbc.so
PKGFILES_CSWapr-util-dev += /opt/csw/lib/apr-util-1/apr_dbd_sqlite3.so
PKGFILES_CSWapr-util-dev += /opt/csw/lib/apr-util-1/apr_dbm_db.so
PKGFILES_CSWapr-util-dev += /opt/csw/lib/apr-util-1/apr_ldap.so

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-berkeley-db=/opt/csw/bdb48
CONFIGURE_ARGS += --without-freetds --without-sqlite2

include gar/category.mk
