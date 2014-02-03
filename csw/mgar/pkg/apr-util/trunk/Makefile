NAME = apr-util
VERSION = 1.5.3
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

PACKAGES += CSWlibaprutil1-0
CATALOGNAME_CSWlibaprutil1-0 = libaprutil1_0
SPKG_DESC_CSWlibaprutil1-0 += Apache Portable Runtime Utilities, libaprutil-1.so.0 and private libraries
PKGFILES_CSWlibaprutil1-0 += $(call pkgfiles_lib,libaprutil-1.so.0)
# PKGFILES_CSWlibaprutil1-0 += $(call baseisadirs,$(libdir),apr-util-1/.*)
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibiconv2
OBSOLETED_BY_CSWlibaprutil1-0 += CSWapr-util

# This is due to different interpretation of -z ignore
CHECKPKG_OVERRIDES_CSWlibaprutil1-0 += surplus-dependency|CSWlibuuid1

PACKAGES += CSWlibaprutil1-dbd-freetds
SPKG_DESC_CSWlibaprutil1-dbd-freetds = Apache Portable Runtime database binding, apr-util-1/apr_dbd_freetds-1.so
PKGFILES_CSWlibaprutil1-dbd-freetds += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_freetds.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-freetds += CSWlibsybdb5
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-freetds += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-freetds += surplus-dependency|CSWlibaprutil1-0
# FreeTDS has not been included in legacy CSWapr-util

PACKAGES += CSWlibaprutil1-dbd-odbc
SPKG_DESC_CSWlibaprutil1-dbd-odbc = Apache Portable Runtime database binding, apr-util-1/apr_dbd_odbc-1.so
PKGFILES_CSWlibaprutil1-dbd-odbc += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_odbc.*\.so)
# Depend on base library, there is no explicit binding in the dbd libraries, though
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-odbc += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-odbc += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-odbc += CSWlibodbc2
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

PACKAGES += CSWlibaprutil1-dbd-pgsql
SPKG_DESC_CSWlibaprutil1-dbd-pgsql = Apache Portable Runtime database binding, apr-util-1/apr_dbd_pgsql.so
PKGFILES_CSWlibaprutil1-dbd-pgsql += $(call baseisadirs,$(libdir),apr-util-1/apr_dbd_pgsql.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-pgsql += CSWlibpq5
RUNTIME_DEP_PKGS_CSWlibaprutil1-dbd-pgsql += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-dbd-pgsql += surplus-dependency|CSWlibaprutil1-0
# PostgreSQL has not been included in legacy CSWapr-util

PACKAGES += CSWlibaprutil1-ldap
SPKG_DESC_CSWlibaprutil1-ldap = Apache Portable Runtime database binding, apr-util-1/apr_ldap-1.so
PKGFILES_CSWlibaprutil1-ldap += $(call baseisadirs,$(libdir),apr-util-1/apr_ldap.*\.so)
RUNTIME_DEP_PKGS_CSWlibaprutil1-ldap += CSWlibaprutil1-0
CHECKPKG_OVERRIDES_CSWlibaprutil1-ldap += surplus-dependency|CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-ldap += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibaprutil1-ldap += CSWlibldap2-4-2
OBSOLETED_BY_CSWlibaprutil1-ldap += CSWapr-util

# This is due to different interpretation of -z ignore
CHECKPKG_OVERRIDES_CSWlibaprutil1-ldap += surplus-dependency|CSWliblber2-4-2

PACKAGES += CSWlibaprutil-dev
SPKG_DESC_CSWlibaprutil-dev += Apache Portable Runtime Utilities, libaprutil-dev
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibaprutil-dev += CSWlibaprutil1-0

# We need this to get bdb48/lib into the runpath
EXTRA_LIB += $(prefix)/bdb48/lib

# Having -I/opt/csw/include appear in CPPFLAGS leads to the installed headers of aprutil included first leading to
# undefined symbols
CPPFLAGS =

# EXTRA_INC += $(prefix)/instantclient_10_2/$(MM_LIBDIR)/sdk/include
# EXTRA_LIB += $(prefix)/instantclient_10_2

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-dbm=db48
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb48/include:$(prefix)/bdb48/lib/$(MM_LIBDIR)
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --without-sqlite2
CONFIGURE_ARGS += --with-sqlite3=$(prefix)
# Enabling Oracle takes some more with the current instantclient layout
#CONFIGURE_ARGS += --with-oracle=$(prefix)/instantclient_10_2/$(MM_LIBDIR)
#CONFIGURE_ARGS += --with-oracle-include=$(prefix)/instantclient_10_2/$(MM_LIBDIR)/sdk/include
CONFIGURE_ARGS += --with-freetds=$(prefix)
CONFIGURE_ARGS += --with-odbc
CONFIGURE_ARGS += --with-pgsql
CONFIGURE_ARGS += --with-iconv=$(prefix)

# How do we deal with 64 bit?
CONFIGURE_ARGS += --with-expat=$(prefix)

TEST_ARGS += EXTRA_LDFLAGS="-L$(libdir) -liconv"

# The whole testsuite requires running databases
SKIPTEST ?= 1

include gar/category.mk

post-configure:
	perl -npe 's/^(CPPFLAGS.*)/# $$1/' -i $(WORKSRC)/build/rules.mk
	@$(MAKECOOKIE)
