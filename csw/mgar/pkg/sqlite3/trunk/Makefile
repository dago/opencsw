NAME = sqlite3
VERSION = 3070701
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

PACKAGES += CSWsqlite3
CATALOGNAME_CSWsqlite3 = sqlite3
SPKG_DESC_CSWsqlite3 = $(DESCRIPTION)
PKGFILES_CSWsqlite3 = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWlibreadline6

PACKAGES += CSWlibsqlite3-0
CATALOGNAME_CSWlibsqlite3-0 = libsqlite3_0
SPKG_DESC_CSWlibsqlite3-0 = SQLite library providing libsqlite3.so.0
PKGFILES_CSWlibsqlite3-0 = $(call pkgfiles_lib,libsqlite3.so.0)
OBSOLETED_BY_CSWlibsqlite3-0 = CSWsqlite3rt
CATALOGNAME_CSWsqlite3rt = sqlite3_rt_stub

PACKAGES += CSWlibsqlite3-dev
CATALOGNAME_CSWlibsqlite3-dev = libsqlite3_dev
SPKG_DESC_CSWlibsqlite3-dev = Development files for libsqlite3.so
PKGFILES_CSWlibsqlite3-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsqlite3-dev = CSWlibsqlite3-0
OBSOLETED_BY_CSWlibsqlite3-dev = CSWsqlite3devel
CATALOGNAME_CSWsqlite3devel = sqlite3_devel_stub

BUILD_DEP_PKGS += CSWreadline

BUILD64 = 1
EXTRA_MERGE_DIRS_isa-extra = $(bindir)

include gar/category.mk

