GARNAME      = sqlite3
GARVERSION   = 3.6.20
CATEGORIES   = lib

DESCRIPTION  = An embeddable SQL engine in a C library
define BLURB
  SQLite is a in-process library that implements a self-contained, serverless,
  zero-configuration, transactional SQL database engine.
endef

# Download informations
MASTER_SITES = http://sqlite.org/
DISTNAME = sqlite-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz 
DISTFILES += COPYING

PATCHFILES = gar-base.diff
PATCHFILES += shell.c.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = sqlite-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWsqlite3 CSWsqlite3rt CSWsqlite3devel

CATALOGNAME_CSWsqlite3 = sqlite3
CATALOGNAME_CSWsqlite3rt = sqlite3_rt
CATALOGNAME_CSWsqlite3devel = sqlite3_devel

SPKG_DESC_CSWsqlite3 = $(DESCRIPTION)
SPKG_DESC_CSWsqlite3rt = $(SPKG_DESC_CSWsqlite3) runtime
SPKG_DESC_CSWsqlite3devel = $(SPKG_DESC_CSWsqlite3) development package

PKGFILES_CSWsqlite3 = $(bindir)/.*
PKGFILES_CSWsqlite3devel = $(PKGFILES_DEVEL)

REQUIRED_PKGS_CSWsqlite3 = CSWsqlite3rt
REQUIRED_PKGS_CSWsqlite3devel = CSWsqlite3

BUILD64 = 1
NO_ISAEXEC = 1

# Make configure options
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threadsafe --disable-debug 

TEST_SCRIPTS =

include gar/category.mk

