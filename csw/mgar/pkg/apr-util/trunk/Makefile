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
SPKG_DESC_CSWlibaprutil1-0 += Apache Portable Runtime Utilities, libaprutil-1.so.0 and private libraries
PKGFILES_CSWlibaprutil1-0 += $(call pkgfiles_lib,libaprutil-1.so.0)
PKGFILES_CSWlibaprutil1-0 += $(call baseisadirs,$(libdir),apr-util-1/.*)
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWunixodbc
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWbdb48
RUNTIME_DEP_PKGS_CSWlibaprutil1-0 += CSWoldaprt
OBSOLETED_BY_CSWlibaprutil1-0 += CSWapr-util
# These are private libraries in lib/apr-util-1/ and it is ok to have no soname
CHECKPKG_OVERRIDES_CSWlibaprutil1-0 += shared-lib-package-contains-so-symlink

PACKAGES += CSWlibaprutil-dev
SPKG_DESC_CSWlibaprutil-dev += Apache Portable Runtime Utilities, libaprutil-dev
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibaprutil-dev += CSWlibaprutil1-0

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

BUILD64 = 1

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-berkeley-db=/opt/csw/bdb48/include:/opt/csw/bdb48/lib/$(MM_LIBDIR)
CONFIGURE_ARGS += --without-freetds
CONFIGURE_ARGS += --without-sqlite2

include gar/category.mk
