GARNAME = freeradius
GARVERSION = 2.1.10
CATEGORIES = server

DESCRIPTION = A free RADIUS server implementation
define BLURB
  A free RADIUS server implementation
endef

MASTER_SITES = ftp://ftp.freeradius.org:/pub/freeradius/
DISTFILES  = $(GARNAME)-server-$(GARVERSION).tar.gz
DISTFILES += cswfreeradius
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

# Put libraries (including all of the modules) in /opt/csw/lib/freeradius
libdir     = $(abspath $(libdir_install)/$(GARNAME)/$(MM_LIBDIR))

# Put the config in the recommended /etc/opt/csw tree
sysconfdir = /etc$(prefix)
raddbdir   = $(sysconfdir)/raddb
# move all of the var stuff to /var/opt/csw
localstatedir = /var$(prefix)

PRESERVECONF += $(raddbdir)/.*\.conf
PRESERVECONF += $(raddbdir)/acct_users
PRESERVECONF += $(raddbdir)/attrs.*
PRESERVECONF += $(raddbdir)/dictionary
PRESERVECONF += $(raddbdir)/certs/.*.cnf
PRESERVECONF += $(raddbdir)/hints
PRESERVECONF += $(raddbdir)/huntgroups
PRESERVECONF += $(raddbdir)/ldap.attrmap
PRESERVECONF += $(raddbdir)/modules/.*
PRESERVECONF += $(raddbdir)/policy.txt
PRESERVECONF += $(raddbdir)/preproxy_users
PRESERVECONF += $(raddbdir)/sql/.*/.*\.conf
PRESERVECONF += $(raddbdir)/users

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
CONFIGURE_ARGS += --without-rlm_eap_ikev2
CONFIGURE_ARGS += --without-rlm_sql_unixodbc
CONFIGURE_ARGS += --without-rlm_eap_tnc

# We probably won't ever build these database bindings
CONFIGURE_ARGS += --without-rlm_sql_firebird
CONFIGURE_ARGS += --without-rlm_sql_freetds
CONFIGURE_ARGS += --without-rlm_sql_iodbc
CONFIGURE_ARGS += --without-rlm_sql_sybase
CONFIGURE_ARGS += --without-rlm_sql_db2
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/mssql
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/mssql/.*
CONFIGURE_ARGS += --without-rlm_sql_oracle
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/oracle
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/oracle/.*

## Individual Package definitions start here

PACKAGES += CSWfreeradius
CATALOGNAME_CSWfreeradius = $(GARNAME)
SPKG_DESC_CSWfreeradius = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpcap
RUNTIME_DEP_PKGS_CSWfreeradius += CSWosslrt
RUNTIME_DEP_PKGS_CSWfreeradius += CSWgdbm
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWfreeradius += CSWreadline
RUNTIME_DEP_PKGS_CSWfreeradius += CSWgcc4corert

## Kerberos
PACKAGES += CSWfreeradius-krb5
CATALOGNAME_CSWfreeradius-krb5 = freeradius_krb5
SPKG_DESC_CSWfreeradius-krb5 = Kerberos 5 Module rlm_krb5 for FreeRADIUS
PKGFILES_CSWfreeradius-krb5 += $(raddbdir)/modules/krb5.CSW
PKGFILES_CSWfreeradius-krb5 += $(docdir)/rlm_krb5
PKGFILES_CSWfreeradius-krb5 += /opt/csw/lib/freeradius/rlm_krb5\.so
PKGFILES_CSWfreeradius-krb5 += /opt/csw/lib/freeradius/rlm_krb5-2\.1\.[0-9]+\.so
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWfreeradius
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWgcc4corert

## LDAP
PACKAGES += CSWfreeradius-ldap
CATALOGNAME_CSWfreeradius-ldap = freeradius_ldap
SPKG_DESC_CSWfreeradius-ldap = LDAP Module rlm_ldap for FreeRADIUS
PKGFILES_CSWfreeradius-ldap += $(raddbdir)/ldap\.attrmap\.CSW
PKGFILES_CSWfreeradius-ldap += $(raddbdir)/modules/ldap\.CSW
PKGFILES_CSWfreeradius-ldap += $(docdir)/ldap_howto\.rst
PKGFILES_CSWfreeradius-ldap += $(docdir)/RADIUS-LDAP-eDirectory
PKGFILES_CSWfreeradius-ldap += $(docdir)/rlm_ldap
PKGFILES_CSWfreeradius-ldap += $(docdir)/examples/openldap.schema
PKGFILES_CSWfreeradius-ldap += /opt/csw/lib/freeradius/rlm_ldap\.so
PKGFILES_CSWfreeradius-ldap += /opt/csw/lib/freeradius/rlm_ldap-2\.1\.[0-9]+\.so
RUNTIME_DEP_PKGS_CSWfreeradius-ldap += CSWoldaprt
RUNTIME_DEP_PKGS_CSWfreeradius-ldap += CSWfreeradius
RUNTIME_DEP_PKGS_CSWfreeradius-ldap += CSWgcc4corert

## Perl support
## Disabling Perl due to linker issues and weird makefiles
#PACKAGES += CSWfreeradius-perl
#CATALOGNAME_CSWfreeradius-perl = freeradius-perl
#SPKG_DESC_CSWfreeradius-perl = Perl Module rlm_perl for FreeRADIUS
#RUNTIME_DEP_PKGS_CSWfreeradius-perl += CSWperl
#RUNTIME_DEP_PKGS_CSWfreeradius-perl += CSWfreeradius
#PKGFILES_CSWfreeradius-perl += $(raddbdir)/example.pl
#rlm_perl_inc = $(shell /opt/csw/bin/perl -e 'use Config; print "$$Config{archlib}\n"')/CORE
#CONFIGURE_ARGS += --with-rlm_perl_include_dir=$(rlm_perl_inc)
## Comment out the following lines when building Perl
CONFIGURE_ARGS += --without-rlm_perl
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/example.pl
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/modules/perl
## End perl exclusion lines

## PostgreSQL support
## Disabling Postgresql because it's going to take a bunch of weird
## Makefile hackery of these non-automake Makefiles to get the RPATH right
#BUILD_DEP_PKGS += CSWpostgresql
#rlm_pgsql_lib = $(shell /opt/csw/postgresql/bin/$(ISA)/pg_config --libdir)
#rlm_pgsql_inc = $(shell /opt/csw/postgresql/bin/$(ISA)/pg_config --includedir)
#CONFIGURE_ARGS += --with-rlm_sql_postgresql_lib_dir=$(rlm_pgsql_lib)
#CONFIGURE_ARGS += --with-rlm_sql_postgresql_include_dir=$(rlm_pgsql_inc)
## Comment out the following lines when building PostgreSQL support
CONFIGURE_ARGS += --without-rlm_sql_postgresql
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/postgresql
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/postgresql/.*
## End pgsql exclusion lines

## Disabling MySQL because it's going to take a bunch of weird
## Makefile hackery of these non-automake Makefiles to get the RPATH right
#BUILD_DEP_PKGS += CSWmysql5devel
#CONFIGURE_ARGS += --with-mysql-lib-dir=/opt/csw/mysql5/lib/$(ISA)/mysql
#CONFIGURE_ARGS += --with-mysql-include-dir=/opt/csw/mysql5/include
## Comment out the following lines when building mysql support
CONFIGURE_ARGS += --without-rlm_sql_mysql
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/mysql
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sql/mysql/.*
## End mysql exclusion lines


# No tests available
TEST_TARGET =

INSTALL_ARGS += R=$(DESTDIR)

INITSMF = /etc/opt/csw/init.d/cswfreeradius

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-install-modulated: copy-local-files

# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/cswfreeradius $(DESTDIR)/etc/opt/csw/init.d/cswfreeradius
	@$(MAKECOOKIE)
