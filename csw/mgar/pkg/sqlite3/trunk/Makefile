GARNAME      = sqlite3
GARVERSION   = 3.7.2
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
DISTFILES += copyright-release.html

LICENSE = copyright-release.html

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

RUNTIME_DEP_PKGS_CSWsqlite3  = CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWreadline
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWncurses

BUILD_DEP_PKGS = CSWreadline CSWncurses

BUILD64 = 1
NOISAEXEC = 1

# Make configure options
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threadsafe --disable-debug --disable-tcl  
CONFIGURE_ARGS += --with-readline-inc="-I/opt/csw/include/readline"

TEST_SCRIPTS =

include gar/category.mk

