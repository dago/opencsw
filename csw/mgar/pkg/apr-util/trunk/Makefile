GARNAME = apr-util
GARVERSION = 1.3.9
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = LICENSE
CATALOGNAME = apr_util

RUNTIME_DEP_PKGS = CSWapr CSWiconv CSWsqlite3rt CSWunixodbc CSWexpat
RUNTIME_DEP_PKGS += CSWbdb48 CSWoldaprt

CHECKPKG_OVERRIDES_CSWapr-util += binary-disallowed-placement|file=opt/csw/lib/sparcv9/libaprutil-1.so.0.3.9|arch_id=2|arch_name=sparcv8|bad_path=sparcv9
CHECKPKG_OVERRIDES_CSWapr-util += binary-disallowed-placement|file=opt/csw/lib/sparcv9/apr-util-1/apr_dbd_sqlite3-1.so|arch_id=2|arch_name=sparcv8|bad_path=sparcv9
CHECKPKG_OVERRIDES_CSWapr-util += binary-disallowed-placement|file=opt/csw/lib/sparcv9/apr-util-1/apr_ldap-1.so|arch_id=2|arch_name=sparcv8|bad_path=sparcv9
CHECKPKG_OVERRIDES_CSWapr-util += binary-disallowed-placement|file=opt/csw/lib/sparcv9/apr-util-1/apr_dbd_odbc-1.so|arch_id=2|arch_name=sparcv8|bad_path=sparcv9

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-dbm=$(prefix)/bdb48
CONFIGURE_ARGS += --without-freetds --without-sqlite2

BUILD64 = 1
STRIP_LIBTOOL = 1

include gar/category.mk
