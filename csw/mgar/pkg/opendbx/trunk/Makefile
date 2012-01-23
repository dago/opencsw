NAME = opendbx
VERSION = 1.4.5
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWopendbx CSWopendbxdevel CSWopendbxmysql CSWopendbxsqlite3 CSWopendbxoracle
CATALOGNAME_CSWopendbx = opendbx
CATALOGNAME_CSWopendbxdevel = opendbx_devel
CATALOGNAME_CSWopendbxmysql = opendbx_mysql
CATALOGNAME_CSWopendbxsqlite3 = opendbx_sqlite3
CATALOGNAME_CSWopendbxoracle = opendbx_oracle

SPKG_DESC_CSWopendbx = $(DESCRIPTION)
SPKG_DESC_CSWopendbxdevel = $(DESCRIPTION), development package
SPKG_DESC_CSWopendbxmysql = $(DESCRIPTION), mysql backend package
SPKG_DESC_CSWopendbxsqlite3 = $(DESCRIPTION), sqlite3 backend package
SPKG_DESC_CSWopendbxsoracle = $(DESCRIPTION), oracle backend package

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GCC3
BUILD64_LIBS_ONLY = 1

EXTRA_BUILD_ISAS_i386 = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv8plus

PACKAGING_PLATFORMS +=  solaris9-sparc solaris9-i386

EXTRA_INC =  $(prefix)/mysql5/include/mysql $(prefix)/instantclient_10_2/sdk/include
EXTRA_LINKER_DIRS_MYSQL_32 = $(prefix)/mysql5/lib/mysql
EXTRA_LINKER_DIRS_ORACLE_32 += $(prefix)/instantclient_10_2
EXTRA_LINKER_DIRS_MYSQL_64 = $(prefix)/mysql5/lib/64/mysql
EXTRA_LINKER_DIRS_ORACLE_64 += $(prefix)/instantclient_10_2/64
EXTRA_LINKER_FLAGS = -L$(EXTRA_LINKER_DIRS_MYSQL_$(MEMORYMODEL)) -L$(EXTRA_LINKER_DIRS_ORACLE_$(MEMORYMODEL))
EXTRA_RUNPATH_LINKER_FLAGS = -R$(EXTRA_LINKER_DIRS_MYSQL_$(MEMORYMODEL)) -R$(EXTRA_LINKER_DIRS_ORACLE_$(MEMORYMODEL))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-utils
CONFIGURE_ARGS += --with-backends="mysql sqlite3 oracle"

PKGFILES_CSWopendbxdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWopendbxmysql = $(call baseisadirs,$(libdir),opendbx/libmysqlbackend.*) 
PKGFILES_CSWopendbxsqlite3 = $(call baseisadirs,$(libdir),opendbx/libsqlite3backend.*) 
PKGFILES_CSWopendbxoracle = $(call baseisadirs,$(libdir),opendbx/liboraclebackend.*) 

CHECKPKG_OVERRIDES_CSWopendbxdevel += surplus-dependency|CSWopendbx
CHECKPKG_OVERRIDES_CSWopendbxmysql += surplus-dependency|CSWopendbx
CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += surplus-dependency|CSWopendbx
CHECKPKG_OVERRIDES_CSWopendbxoracle += surplus-dependency|CSWopendbx

CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/amd64/opendbx/libsqlite3backend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/opendbx/libsqlite3backend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/opendbx/libsqlite3backend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxsqlite3 += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/sparcv8plus/opendbx/libsqlite3backend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/amd64/libopendbx.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/amd64/libopendbxplus.so.1.0.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/libopendbx.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/libopendbxplus.so.1.0.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/libopendbx.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/libopendbxplus.so.1.0.
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/libopendbxplus.so.1.0.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/sparcv8plus/libopendbx.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbx += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/sparcv8plus/libopendbxplus.so.1.0.0
CHECKPKG_OVERRIDES_CSWopendbxmysql += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/amd64/opendbx/libmysqlbackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxmysql += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/opendbx/libmysqlbackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxmysql += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/opendbx/libmysqlbackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxmysql += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/sparcv8plus/opendbx/libmysqlbackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxoracle += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/amd64/opendbx/liboraclebackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxoracle += bad-rpath-entry|/opt/csw/instantclient_10_2/64|opt/csw/lib/sparcv9/opendbx/liboraclebackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxoracle += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/opendbx/liboraclebackend.so.1.2.0
CHECKPKG_OVERRIDES_CSWopendbxoracle += missing-dependency|CSWorainstclient102
CHECKPKG_OVERRIDES_CSWopendbxoracle += bad-rpath-entry|/opt/csw/instantclient_10_2|opt/csw/lib/sparcv8plus/opendbx/liboraclebackend.so.1.2.0

RUNTIME_DEP_PKGS_CSWopendbx += CSWgcc3corert
RUNTIME_DEP_PKGS_CSWopendbx += CSWgcc3g++rt
RUNTIME_DEP_PKGS_CSWopendbx += CSWggettextrt
RUNTIME_DEP_PKGS_CSWopendbxdevel += CSWopendbx
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWgcc3corert
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWzlib
RUNTIME_DEP_PKGS_CSWopendbxmysql += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWopendbxsqlite3 += CSWgcc3corert
RUNTIME_DEP_PKGS_CSWopendbxsqlite3 += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWopendbxoracle += CSWgcc3corert
RUNTIME_DEP_PKGS_CSWopendbxoracle += CSWopendbx
RUNTIME_DEP_PKGS_CSWopendbxoracle += CSWorainstclient102

include gar/category.mk
