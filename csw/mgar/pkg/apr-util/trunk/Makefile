NAME = apr-util
VERSION = 1.5.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE

#PATCHFILES = 0001-Make-sure-to-find-newly-built-libs-earlier.patch

PACKAGES += CSWlibaprutil1-0
CATALOGNAME_CSWlibaprutil1-0 = libaprutil1_0
SPKG_DESC_CSWlibaprutil1-0 += Apache Portable Runtime Utilities, libaprutil-1.so.0 and private libraries
PKGFILES_CSWlibaprutil1-0 += $(call pkgfiles_lib,libaprutil-1.so.0)
# PKGFILES_CSWlibaprutil1-0 += $(call baseisadirs,$(libdir),apr-util-1/.*)
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibexpat1
OBSOLETED_BY_CSWlibaprutil1-0 += CSWapr-util


PACKAGES += CSWlibaprutil1-dbd-freetds
SPKG_DESC_CSWlibaprutil1-dbd-freetds = Apache Portable Runtime database binding, apr-util-1/apr_dbd_freetds-1.so
PKGFILES_CSWlibaprutil1-dbd-freetds += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_freetds.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-freetds += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-freetds += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-freetds += CSWfreetds
# FreeTDS has not been included in legacy CSWapr-util

PACKAGES += CSWlibaprutil1-dbd-odbc
SPKG_DESC_CSWlibaprutil1-dbd-odbc = Apache Portable Runtime database binding, apr-util-1/apr_dbd_odbc-1.so
PKGFILES_CSWlibaprutil1-dbd-odbc += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_odbc.*\.so)
# Depend on base library, there is no explicit binding in the dbd libraries, though
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-odbc += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-odbc += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-odbc += CSWunixodbc
OBSOLETED_BY_CSWlibaprutil1-dbd-odbc += CSWapr-util

PACKAGES += CSWlibaprutil1-dbd-sqlite3
SPKG_DESC_CSWlibaprutil1-dbd-sqlite3 = Apache Portable Runtime database binding, apr-util-1/apr_dbd_sqlite3-1.so
PKGFILES_CSWlibaprutil1-dbd-sqlite3 += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_sqlite3.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-sqlite3 += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-sqlite3 += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-sqlite3 += CSWlibsqlite3-0
OBSOLETED_BY_CSWlibaprutil1-dbd-sqlite3 += CSWapr-util

PACKAGES += CSWlibaprutil1-dbm-db
SPKG_DESC_CSWlibaprutil1-dbm-db = Apache Portable Runtime database binding, apr-util-1/apr_dbm_db-1.so
PKGFILES_CSWlibaprutil1-dbm-db += $(call baseisadirs,$(libdir),apr-util-1/apr_dbm_db.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbm-db += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbm-db += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbm-db += CSWbdb48
OBSOLETED_BY_CSWlibaprutil1-dbm-db += CSWapr-util

PACKAGES += CSWlibaprutil1-ldap
SPKG_DESC_CSWlibaprutil1-ldap = Apache Portable Runtime database binding, apr-util-1/apr_ldap-1.so
PKGFILES_CSWlibaprutil1-ldap += $(call baseisadirs,$(libdir),apr-util-1/apr_ldap.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-ldap += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-ldap += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-ldap += CSWoldaprt
OBSOLETED_BY_CSWlibaprutil1-ldap += CSWapr-util

PACKAGES += CSWlibaprutil-dev
SPKG_DESC_CSWlibaprutil-dev += Apache Portable Runtime Utilities, libaprutil-dev
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibaprutil-dev += CSWlibaprutil1-0

# We need this to get bdb48/lib into the runpath
EXTRA_LIB += $(prefix)/bdb48/lib

# EXTRA_INC += $(prefix)/instantclient_10_2/$(MM_LIBDIR)/sdk/include
# EXTRA_LIB += $(prefix)/instantclient_10_2

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-dbm=db48
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb48/include:$(prefix)/bdb48/lib/$(MM_LIBDIR)
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-freetds
CONFIGURE_ARGS += --without-sqlite2
CONFIGURE_ARGS += --with-sqlite3
# Enabling Oracle takes some more with the current instantclient layout
#CONFIGURE_ARGS += --with-oracle=$(prefix)/instantclient_10_2/$(MM_LIBDIR)
#CONFIGURE_ARGS += --with-oracle-include=$(prefix)/instantclient_10_2/$(MM_LIBDIR)/sdk/include
CONFIGURE_ARGS += --with-freetds
CONFIGURE_ARGS += --with-odbc

include gar/category.mk
