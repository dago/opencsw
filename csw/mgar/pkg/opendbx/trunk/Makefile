GARNAME = opendbx
GARVERSION = 1.4.5
CATEGORIES = lib

DESCRIPTION = A C library for accessing databases with a single API
define BLURB
  OpenDBX is an extremely lightweight but extensible C library for
  accessing databases with a single API. It provides a clean and simple
  interface across all supported databases that leads to an elegant
  code design automatically. Currently MySQL, PostgreSQL, SQLite
  (v2 & 3), MSSQL and Sybase are supported and backends for more native
  database APIs can be written easily. If you want your application to
  support different databases with little effort, this is definitively
  the right thing for you!
endef

MASTER_SITES = http://www.linuxnetworks.de/opendbx/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWopendbx CSWopendbxdevel CSWopendbxmysql CSWopendbxsqlite3
CATALOGNAME_CSWopendbx = opendbx
CATALOGNAME_CSWopendbxdevel = opendbx_devel
CATALOGNAME_CSWopendbxmysql = opendbx_mysql
CATALOGNAME_CSWopendbxsqlite3 = opendbx_sqlite3

SPKG_DESC_CSWopendbx = $(DESCRIPTION)
SPKG_DESC_CSWopendbxdevel = $(DESCRIPTION), development package
SPKG_DESC_CSWopendbxmysql = $(DESCRIPTION), mysql backend package
SPKG_DESC_CSWopendbxsqlite3 = $(DESCRIPTION), sqlite3 backend package

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GCC4
BUILD64 = 1
#EXTRA_BUILD_ISAS_i386 = pentium_pro
#EXTRA_BUILD_ISAS_sparc = sparcv8plus

EXTRA_INC = /opt/csw/mysql5/include/mysql
EXTRA_LINKER_DIRS_32 = $(prefix)/mysql5/lib/mysql
EXTRA_LINKER_DIRS_64 = $(prefix)/mysql5/lib/64/mysql
EXTRA_LINKER_FLAGS = -L$(EXTRA_LINKER_DIRS_$(MEMORYMODEL))
EXTRA_RUNPATH_LINKER_FLAGS = -R$(EXTRA_LINKER_DIRS_$(MEMORYMODEL))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-utils
CONFIGURE_ARGS += --with-backends="mysql sqlite3"

PKGFILES_CSWopendbxdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWopendbxmysql = $(call baseisadirs,$(libdir),opendbx/libmysqlbackend.*) 
PKGFILES_CSWopendbxsqlite3 = $(call baseisadirs,$(libdir),opendbx/libsqlite3backend.*) 

#CONFIGURE_ARGS += --with-backends=oracle
#EXTRA_LIB = /opt/csw/instantclient_10_2
#EXTRA_INC = /opt/csw/instantclient_10_2/sdk/include
#RUNTIME_DEP_PKGS_CSWopendbx += CSWorainstclient102
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/libopendbx.so.1.2.0
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/$ISALIST|opt/csw/lib/libopendbx.so.1.2.0
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/libopendbxplus.so.1.0.0
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/$ISALIST|opt/csw/lib/libopendbxplus.so.1.0.0
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/opendbx/liboraclebackend.so.1.2.0
#CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/$ISALIST|opt/csw/lib/opendbx/liboraclebackend.so.1.2.0

CHECKPKG_OVERRIDES_CSWopendbxdevel += surplus-dependency|CSWopendbx
CHECKPKG_OVERRIDES_CSWopendbxmysql += surplus-dependency|CSWopendbx
CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += surplus-dependency|CSWopendbx

RUNTIME_DEP_PKGS_CSWopendbx += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWopendbx += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWopendbx += CSWggettextrt
RUNTIME_DEP_PKGS_CSWopendbxdevel += CSWopendbx
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWzlib
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWopendbxsqlite3 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWopendbxsqlite3 += CSWsqlite3rt

include gar/category.mk
