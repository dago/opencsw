GARNAME = freeradius
GARVERSION = 2.1.10
CATEGORIES = server

DESCRIPTION = A free RADIUS server implementation
define BLURB
  A free RADIUS server implementation
endef

MASTER_SITES = ftp://ftp.freeradius.org:/pub/freeradius/
DISTFILES  = $(GARNAME)-server-$(GARVERSION).tar.gz
DISTNAME = $(GARNAME)-server-$(GARVERSION)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://freeradius.org/

LICENSE = LICENSE
GARCOMPILER = GCC4


# Stripping libtool breaks the build in versions <=2.1.7
#STRIP_LIBTOOL = 1

## Some of the RLM Submodules don't seem to pick up the include paths without 
## setting CFLAGS
EXTRA_CFLAGS  = -I/opt/csw/include
#EXTRA_CFLAGS += -DIE_LIBTOOL_DIE
#CONFIGURE_ENV = CFLAGS="$(CFLAGS)"

#EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/lib/libltdl.so.*
#EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/lib/sparcv9/libltdl.so.*
#EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/lib/amd64/libltdl.so.*
#EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/include/ltdl.h

RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpcap
RUNTIME_DEP_PKGS_CSWfreeradius += CSWoldaprt
RUNTIME_DEP_PKGS_CSWfreeradius += CSWosslrt
RUNTIME_DEP_PKGS_CSWfreeradius += CSWgdbm
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWfreeradius += CSWreadline
RUNTIME_DEP_PKGS_CSWfreeradius += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWfreeradius += CSWgcc4corert

## Can't get perl to link cleanly
## Still get noise about a missing dependency due to an included example 
## script in raddb
#RUNTIME_DEP_PKGS_CSWfreeradius += CSWperl
CHECKPKG_OVERRIDES_CSWfreeradius += missing-dependency|CSWperl

# Put libraries (including all of the modules) in /opt/csw/lib/freeradius
libdir     = $(abspath $(libdir_install)/$(GARNAME)/$(MM_LIBDIR))

# Put the config in the recommended /etc/opt/csw tree
sysconfdir = /etc$(prefix)
raddbdir   = $(sysconfdir)/raddb
# move all of the var stuff to /var/opt/csw
localstatedir = /var$(prefix)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += CC=$(CC) CXX=$(CXX) F77=$(F77) FC=$(FC)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)" CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)" FCFLAGS="$(FCFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"
#CONFIGURE_ARGS += MYSQL_CONFIG=/opt/csw/mysql5/bin/$(ISA)/mysql_config 
CONFIGURE_ARGS += --with-system-libtool
CONFIGURE_ARGS += --with-system-libltld
CONFIGURE_ARGS += --with-raddbdir=$(raddbdir)
CONFIGURE_ARGS += --enable-ltdl-install=no
CONFIGURE_ARGS += --enable-strict-dependencies
CONFIGURE_ARGS += --enable-developer
CONFIGURE_ARGS += --with-large-files --with-updfromto --with-edir
CONFIGURE_ARGS += --without-rlm_sql_firebird
CONFIGURE_ARGS += --without-rlm_sql_freetds
CONFIGURE_ARGS += --without-rlm_sql_iodbc
CONFIGURE_ARGS += --without-rlm_sql_oracle
CONFIGURE_ARGS += --without-rlm_sql_sybase
CONFIGURE_ARGS += --without-rlm_sql_db2
CONFIGURE_ARGS += --without-rlm_eap_ikev2
CONFIGURE_ARGS += --without-rlm_sql_unixodbc
CONFIGURE_ARGS += --without-rlm_eap_tnc

## Disabling Postgresql because it's going to take a bunch of weird
## Makefile hackery of these non-automake Makefiles to get the RPATH right
#BUILD_DEP_PKGS += CSWpostgresql
#rlm_pgsql_lib = $(shell /opt/csw/postgresql/bin/$(ISA)/pg_config --libdir)
#rlm_pgsql_inc = $(shell /opt/csw/postgresql/bin/$(ISA)/pg_config --includedir)
#CONFIGURE_ARGS += --with-rlm_sql_postgresql_lib_dir=$(rlm_pgsql_lib)
#CONFIGURE_ARGS += --with-rlm_sql_postgresql_include_dir=$(rlm_pgsql_inc)
CONFIGURE_ARGS += --without-rlm_sql_postgresql

## Disabling MySQL because it's going to take a bunch of weird
## Makefile hackery of these non-automake Makefiles to get the RPATH right
#BUILD_DEP_PKGS += CSWmysql5devel
#CONFIGURE_ARGS += --with-mysql-lib-dir=/opt/csw/mysql5/lib/$(ISA)/mysql
#CONFIGURE_ARGS += --with-mysql-include-dir=/opt/csw/mysql5/include
CONFIGURE_ARGS += --without-rlm_sql_mysql

## Disabling Perl due to linker issues and weird makefiles
#rlm_perl_inc = $(shell /opt/csw/bin/perl -e 'use Config; print "$$Config{archlib}\n"')/CORE
#CONFIGURE_ARGS += --with-rlm_perl_include_dir=$(rlm_perl_inc)
CONFIGURE_ARGS += --without-rlm_perl

# No tests available
TEST_TARGET =

INSTALL_ARGS += R=$(DESTDIR)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
