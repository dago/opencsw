NAME = opendbx
VERSION = 1.4.6
CATEGORIES = lib
GARTYPE = v2

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
DISTFILES  = $(NAME)-$(VERSION). = CSWlibopendbx1
PACKAGES +=CSWlibopendbxdevel
PACKAGES += CSWlibopendbxmysql
PACKAGES += CSWlibopendbxsqlite3

CATALOGNAME_CSWlibopendbx1 = libopendbx1
CATALOGNAME_CSWlibopendbxdevel = libopendbxdevel
CATALOGNAME_CSWlibopendbxmysql = libopendbxmysql
CATALOGNAME_CSWlibopendbxsqlite3 = libopendbxsqlite3

SPKG_DESC_CSWlibopendbx1 += $(DESCRIPTION), libopendbx.so.1
SPKG_DESC_CSWlibopendbxdevel = $(DESCRIPTION), development package
SPKG_DESC_CSWlibopendbxmysql = $(DESCRIPTION), mysql backend package
SPKG_DESC_CSWlibopendbxsqlite3 = $(DESCRIPTION), sqlite3CRIPTION), oracle backend package

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

4ARCOMPILER = GCC3
BUILD64_LIBS_ONLY = 1

EXTRA_BUILD_ISAS_i386 = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv8plus

PACKAGING_PLAT10-sparc solaris10-i386

EXTRA_INC =  $(prefix)/include/mysqlE_$(MEMORYMODEL))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-utils
CONFIGURE_ARGS += --with-backen"
CONFIGURE_ARGS += --enable-maintainer-mode

PKGFILES_CSWlibopendbxdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibopendbxmysql = $(call baseisadirs,$(libdir),opendbx/libmysqlbackend.*) 
PKGFILES_CSWlibopendbxsqlite3 = $(call baseisadirs,$(libdir),opendbx/libsqlite3backend.*) 
PKGFILES_CSWlibopendbx1 = $(PKGFILES_RT)

RUNTIME_DEP_PKGS_CSWlibopendbxmysql += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibopendbxmysql += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWlibopendbxdevel += CSWlibopendbx1
RUNTIME_DEP_PKGS_CSWlibopendbxsqlite3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibopendbxsqlite3 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibopendbx1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibopendbx1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibopendbx1 += CSWlibstdc++6

CHECKPKG_OVERRIDES_CSWlibopendbx1 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libopendbxplus.so.1.0.0|soname=libopendbxplus.so.1|pkgname=CSWlibopendbx1|expected=CSWlibopendbxplus1
CHECKPKG_OVERRIDES_CSWlibopendbx1 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libopendbxplus.so.1.0.0|soname=libopendbxplus.so.1|pkgname=CSWlibopendbx1|expected=CSWlibopendbxplus1
CHECKPKG_OVERRIDES_CSWlibopendbx1 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libopendbxplus.so.1.0.0|soname=libopendbxplus.so.1|pkgname=CSWlibopendbx1|expected=CSWlibopendbxplus1

include gar/category.mk
