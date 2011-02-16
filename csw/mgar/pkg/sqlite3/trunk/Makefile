NAME = sqlite3
VERSION = 3070500
CATEGORIES = lib

DESCRIPTION  = An embeddable SQL engine in a C library
define BLURB
  SQLite is a in-process library that implements a self-contained, serverless,
  zero-configuration, transactional SQL database engine.
endef

# Download informations
MASTER_SITES = http://sqlite.org/
DISTNAME = sqlite-autoconf-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += copyright-release.html

LICENSE = copyright-release.html

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = sqlite-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWsqlite3
CATALOGNAME_CSWsqlite3 = sqlite3
SPKG_DESC_CSWsqlite3 = $(DESCRIPTION)
PKGFILES_CSWsqlite3 = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWreadline

PACKAGES += CSWlibsqlite3-0
CATALOGNAME_CSWlibsqlite3-0 = libsqlite3_0
SPKG_DESC_CSWlibsqlite3-0 = SQLite library providing libsqlite3.so.0
PKGFILES_CSWlibsqlite3-0 = $(call baseisadirs,$(libdir),libsqlite3\.so\.0(\.\d+)*)

PACKAGES += CSWlibsqlite3-dev
CATALOGNAME_CSWlibsqlite3-dev = libsqlite3_dev
SPKG_DESC_CSWlibsqlite3-dev = Development files for libsqlite3.so
PKGFILES_CSWlibsqlite3-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsqlite3-dev = CSWlibsqlite3-0

PACKAGES += CSWsqlite3rt
CATALOGNAME_CSWsqlite3rt = sqlite3_rt
SPKG_DESC_CSWsqlite3rt = Transitional package as contents moved to CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsqlite3rt = CSWlibsqlite3-0
CHECKPKG_OVERRIDES_CSWsqlite3rt += surplus-dependency|CSWlibsqlite3-0
PKGFILES_CSWsqlite3rt = NOFILES
ARCHALL_CSWsqlite3rt = 1

PACKAGES += CSWsqlite3devel
CATALOGNAME_CSWsqlite3devel = sqlite3_devel
SPKG_DESC_CSWsqlite3devel = Transitional package as contents moved to CSWlibsqlite3-dev
PKGFILES_CSWsqlite3devel = NOFILES

BUILD_DEP_PKGS += CSWreadline

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

