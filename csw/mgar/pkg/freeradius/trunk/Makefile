NAME = freeradius
VERSION = 2.1.12
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A free RADIUS server implementation

MASTER_SITES = ftp://ftp.freeradius.org:/pub/freeradius/
DISTFILES += $(NAME)-server-$(VERSION).tar.gz
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswfreeradius
EXPANDVARS += cswfreeradius
DISTFILES += server.pem
DISTFILES += ca.pem
DISTNAME = $(NAME)-server-$(VERSION)

VENDOR_URL = http://freeradius.org/

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibgdbm-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWlibreadline-dev

PACKAGES += CSWfreeradius
SPKG_DESC_CSWfreeradius = A free RADIUS server implementation
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWfreeradius += CSWlibreadline6

# These may be problematic, override for now
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/etc/opt/csw/freeradius/radiusd.conf.CSW
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/dictionary.5
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeradius/Simultaneous-Use
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeradius/ldap_howto.rst
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeradius/rlm_sqlcounter
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeradius/supervise-radiusd.rst
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeradius/performance-testing
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/sbin/radiusd
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/sbin/checkrad
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/local|root/opt/csw/bin/radwho
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/dictionary.5
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/share|root/opt/csw/share/doc/freeradius/mssql
CHECKPKG_OVERRIDES_CSWfreeradius += file-with-bad-content|/usr/share|root/opt/csw/share/doc/freeradius/ldap_howto.rst


PACKAGES += CSWfreeradius-krb5
SPKG_DESC_CSWfreeradius-krb5 = Kerberos 5 Module rlm_krb5 for FreeRADIUS
PKGFILES_CSWfreeradius-krb5 += $(raddbdir)/modules/krb5.CSW
PKGFILES_CSWfreeradius-krb5 += $(docdir)/rlm_krb5
PKGFILES_CSWfreeradius-krb5 += /opt/csw/lib/freeradius/rlm_krb5\.so
PKGFILES_CSWfreeradius-krb5 += /opt/csw/lib/freeradius/rlm_krb5-2\.1\.[0-9]+\.so
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWfreeradius-krb5 += CSWfreeradius

PACKAGES += CSWfreeradius-ldap
SPKG_DESC_CSWfreeradius-ldap = LDAP Module rlm_ldap for FreeRADIUS
PKGFILES_CSWfreeradius-ldap += $(raddbdir)/ldap\.attrmap\.CSW
PKGFILES_CSWfreeradius-ldap += $(raddbdir)/modules/ldap\.CSW
PKGFILES_CSWfreeradius-ldap += $(docdir)/ldap_howto\.rst
PKGFILES_CSWfreeradius-ldap += $(docdir)/RADIUS-LDAP-eDirectory
PKGFILES_CSWfreeradius-ldap += $(docdir)/rlm_ldap
PKGFILES_CSWfreeradius-ldap += $(docdir)/examples/openldap.schema
PKGFILES_CSWfreeradius-ldap += /opt/csw/lib/freeradius/rlm_ldap\.so
PKGFILES_CSWfreeradius-ldap += /opt/csw/lib/freeradius/rlm_ldap-2\.1\.[0-9]+\.so
RUNTIME_DEP_PKGS_CSWfreeradius-ldap += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWfreeradius-ldap += CSWfreeradius

## Disabling Perl due to linker issues and weird makefiles
#PACKAGES += CSWfreeradius-perl
SPKG_DESC_CSWfreeradius-perl = Perl Module rlm_perl for FreeRADIUS
RUNTIME_DEP_PKGS_CSWfreeradius-perl += CSWperl
RUNTIME_DEP_PKGS_CSWfreeradius-perl += CSWfreeradius
PKGFILES_CSWfreeradius-perl += $(raddbdir)/example.pl
rlm_perl_inc = $(shell /opt/csw/bin/perl -e 'use Config; print "$$Config{archlib}\n"')/CORE
# CONFIGURE_ARGS += --with-rlm_perl_include_dir=$(rlm_perl_inc)
CONFIGURE_ARGS += --without-rlm_perl
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/example.pl
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/modules/perl

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

radius_user = radius
radius_group = radius

CSWfreeradius_usergroup = $(radius_user):$(radius_group):FreeRADIUS:/var/opt/csw/freeradius:/bin/false::

# Some of the RLM Submodules don't seem to pick up the include paths from CPPFLAGS
EXTRA_CFLAGS  = $(CPPFLAGS)

# Put libraries (including all of the modules) in /opt/csw/lib/freeradius
libdir = $(abspath $(libdir_install)/freeradius/$(MM_LIBDIR))

raddbdir = $(sysconfdir)/freeradius

radius_rundir = $(localstatedir)/run/radiusd
radius_rundir_perms = 0755

radius_logdir = $(localstatedir)/log/radius
radius_logdir_perms = 2770

# Configuration directory
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
PRESERVECONF += $(raddbdir)/sites-available/buffered-sql
PRESERVECONF += $(raddbdir)/sites-available/coa
PRESERVECONF += $(raddbdir)/sites-available/control-socket
PRESERVECONF += $(raddbdir)/sites-available/copy-acct-to-home-server
PRESERVECONF += $(raddbdir)/sites-available/decoupled-accounting
PRESERVECONF += $(raddbdir)/sites-available/default
PRESERVECONF += $(raddbdir)/sites-available/dhcp
PRESERVECONF += $(raddbdir)/sites-available/dynamic-clients
PRESERVECONF += $(raddbdir)/sites-available/example
PRESERVECONF += $(raddbdir)/sites-available/inner-tunnel
PRESERVECONF += $(raddbdir)/sites-available/originate-coa
PRESERVECONF += $(raddbdir)/sites-available/proxy-inner-tunnel
PRESERVECONF += $(raddbdir)/sites-available/robust-proxy-accounting
PRESERVECONF += $(raddbdir)/sites-available/soh
PRESERVECONF += $(raddbdir)/sites-available/status
PRESERVECONF += $(raddbdir)/sites-available/virtual.example.com
PRESERVECONF += $(raddbdir)/sites-available/vmps

## Additional Config cleanups
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sites-enabled/control-socket
EXTRA_MERGE_EXCLUDE_FILES += $(raddbdir)/sites-enabled/inner-tunnel

CONFIGURE_ARGS += $(DIRPATHS)
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

# There is no testsuite
TEST_SCRIPTS =

INSTALL_ARGS += R=$(DESTDIR)

# We add the radius user and radius group, enable them in the configuration also
REINPLACEMENTS += radiususer
REINPLACE_MATCH_radiususer = ^\#(user|group)
REINPLACE_WITH_radiususer = \$$1
REINPLACE_FILES_radiususer = $(sysconfdir)/freeradius/radiusd.conf
REINPLACE_WHEN_radiususer = postinstall

INITSMF = /etc/opt/csw/init.d/cswfreeradius

# Fix permissions on the radiusd rundir (disabled for now)
PROTOTYPE_MODIFIERS += rundir
PROTOTYPE_FILES_rundir = $(radius_rundir)
PROTOTYPE_USER_rundir = $(radius_user)
PROTOTYPE_GROUP_rundir = $(radius_group)
PROTOTYPE_PERMS_rundir = $(radius_rundir_perms)
PROTOTYPE_CLASS_rundir = ugfiles

PROTOTYPE_MODIFIERS += logdir
PROTOTYPE_FILES_logdir = $(radius_logdir)
PROTOTYPE_USER_logdir = $(radius_user)
PROTOTYPE_GROUP_logdir = $(radius_user)
PROTOTYPE_PERMS_logdir = $(radius_logdir_perms)
PROTOTYPE_CLASS_logdir = ugfiles

# Fix permissions on the configuration directory
PROTOTYPE_MODIFIERS += raddb
PROTOTYPE_FILES_raddb = $(raddbdir)
PROTOTYPE_FILES_raddb += $(raddbdir)/.*
PROTOTYPE_USER_raddb = radius
PROTOTYPE_GROUP_raddb = radius
PROTOTYPE_CLASS_raddb = ugfiles

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	@echo "Installing init script..."
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswfreeradius $(DESTDIR)/etc/opt/csw/init.d/cswfreeradius
	@echo "Installing sample certificate files..."
	ginstall -m 640 $(FILEDIR)/ca.pem $(DESTDIR)/$(raddbdir)/certs/
	ginstall -m 640 $(FILEDIR)/server.pem $(DESTDIR)/$(raddbdir)/certs/
	@echo "Creating PID file directory"
	ginstall -d $(DESTDIR)$(radius_rundir)
	@echo "Relaxing permissions on dictionary file"
	chmod 644 $(DESTDIR)$(raddbdir)/dictionary
	@echo "Commenting out experimental modules"
	perl -npi -e 'print "#" if( !/^\s*(#.*)?$$/ )' $(DESTDIR)$(raddbdir)/experimental.conf
	@$(MAKECOOKIE)
