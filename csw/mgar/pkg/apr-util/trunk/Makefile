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

PATCHFILES = 0001-Make-sure-to-find-newly-built-libs-earlier.patch

PACKAGES = CSWapr-util
CATALOGNAME = apr_util

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWapr CSWiconv CSWsqlite3rt CSWunixodbc CSWexpat
RUNTIME_DEP_PKGS += CSWbdb48 CSWoldaprt 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

# It looks like Solars 9 x86 has a problem with libuuid, investigate later:
# testing9x# cd /usr/lib
# testing9x# ls -l libuuid*
# -rwxr-xr-x   1 root     bin        22344 Dec 23  2004 libuuid.so.1
# testing9x# ln -s libuuid.so.1 libuuid.so

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-berkeley-db=/opt/csw/bdb48
CONFIGURE_ARGS += --without-freetds --without-sqlite2

#BUILD64 = 1
#reason is that no sparcv9 binaries are built for some reason and checkpkg suggests:
#CHECKPKG_OVERRIDES_CSWapr-util += binary-disallowed-placement|file=opt/csw/lib/sparcv9/libaprutil-1.so.0.3.9|arch_id=2|arch_name=sparcv8|bad_path=sparcv9
# dam: The reason is the files are actually built as sparcv8, because we don't have a separate
#   /opt/csw/share/build-1/apr_rules.mk
# for 32 and 64 bit. We need to inspire us from
#   http://cvs.opensolaris.org/source/xref/sfw/usr/src/cmd/apr/apr-1.3/Makefile.sfw
# for some unification.

# add new checkpkg remarks for the moment to get security fix out
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbd_odbc.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbd_sqlite3.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbm_db.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_ldap.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libaprutil-1.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-pkgname-mismatch|file=opt/csw/lib/libaprutil-1.so.0.3.10|soname=libaprutil-1.so.0|pkgname=CSWapr-util|expected=['CSWlibaprutil-10',|'CSWlibaprutil-1-0']
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbd_odbc.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbd_sqlite3.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_dbm_db.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/apr-util-1/apr_ldap.so
CHECKPKG_OVERRIDES_CSWapr-util += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libaprutil-1.so


include gar/category.mk
