# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# If you are involved in packaging MySQL, consider subscribing to the
# packagers mailing list:
# http://lists.mysql.com/packagers
#
# About building MySQL with cmake:
# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
#
# !!WARNING!!
# From 5.6.4, stlport is used by default.
# It appears to not be used by libmysql*, so there should not be any binary
# incompatibility there. However, care must be taken that it does not creep
# in, either in the lib*.so or in the mysql_config script.


PROJ_NAME    = mysql
NAME         = $(PROJ_NAME)5
BASE_VERSION = 5.6
PATCHLEVEL   = 12
ALTS_PRIO    = 56
VERSION = $(BASE_VERSION).$(PATCHLEVEL)

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = SOS12U3

# Solaris 10 needs a special map file since we need libnsl Version 1.9.1
# and libc 1.22.5
LINKER_MAPS ?= -M "$(abspath $(WORKDIR)/map.mysql)"

DISTNAME = mysql-$(VERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

# Those options follow those of the official builds
EXTRA_CFLAGS-sparc = -Xa -xstrconst 
EXTRA_CFLAGS-i386  = -fsimple=1 -ftrap=%none -nofstore -xbuiltin=%all -xlibmil -xlibmopt
EXTRA_CXXFLAGS-sparc = -noex 
EXTRA_CXXFLAGS-i386  = -fsimple=1 -ftrap=%none -nofstore -xbuiltin=%all -features=no%except -xlibmil -xlibmopt
EXTRA_CFLAGS   += $(EXTRA_CFLAGS-$(GARCH)) -g -mt -KPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm -xnorunpath
EXTRA_CXXFLAGS += $(EXTRA_CXXFLAGS-$(GARCH)) -g0 -mt -KPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm -norunpath
EXTRA_LDFLAGS += -Bdirect

# The official build used -xO2 on 32 bit x86, -xO3 for 64 bit
# Use that for all builds
OPT_FLAGS_SOS-32 = -xO2
OPT_FLAGS_SOS-64 = -xO3
OPT_FLAGS_SOS = $(OPT_FLAGS_SOS-$(MEMORYMODEL))


INITSMF = $(sysconfdir)/init\.d/csw$(NAME)

# Existing databases are in this location
localstatedir = /var$(BUILD_PREFIX)/$(NAME)
# To avoid file conflicts
# datadir = $(prefix)/share/mysql/$(BASE_VERSION)

MYSQL_LIB_VER = 18

MERGE_DIRS_isa-extra = $(bindir) $(libdir) $(sbindir) $(libexecdir)

PACKAGES += CSWmysql-dev
SPKG_DESC_CSWmysql-dev = MySQL development files
PKGFILES_CSWmysql-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient$(MYSQL_LIB_VER)
CSWmysql-dev_programs += mysql_config
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSWmysql-dev  += $(mandir)/man1/mysql_config.*
PKGFILES_CSWmysql-dev  += $(prefix)/include.*
PKGFILES_CSWmysql-dev  += /opt/csw/include/mysql

PACKAGES += CSWlibmysqlclient$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibssl1-0-0

PACKAGES += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient_r\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient_r.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient-r18 += CSWlibmysqlclient18

# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
client_programs += myisamlog
client_programs += myisampack
client_programs += mysql
client_programs += mysqlaccess
client_programs += mysqladmin
client_programs += mysqlbin
client_programs += mysqlbinlog
client_programs += mysqlcheck
client_programs += mysql_client_test
client_programs += mysqldump
client_programs += mysqlhotcopy
client_programs += mysqlimport
client_programs += mysqlshow
client_programs += mysql_zap
client_programs += perror
client_programs += replace

PACKAGES += CSW$(NAME)client
SPKG_DESC_CSW$(NAME)client = MySQL $(BASE_VERSION) client binaries
PKGFILES_CSW$(NAME)client  = $(bindir)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),/opt/csw/sbin/$(bin_name))
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSW$(NAME)client += bad-rpath-entry

CHECKPKG_OVERRIDES_CSWlibmysqlclient18 += bad-rpath-entry

PACKAGES += CSW$(NAME)
SPKG_DESC_CSW$(NAME) = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME) += CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibstlport1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/sparcv9/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/amd64/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1

# An example:
# s9_preload.so.1|is|needed|by|/opt/csw/bin/innochecksum|but|never|used
#CHECKPKG_OVERRIDES_CSW$(NAME) += soname-unused

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/mysql-test.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/sql-bench.*
EXTRA_MERGE_EXCLUDE_FILES += $(datadir)/mysql-test.*

BUILD64 = 1

MASTER_SITES  = http://ftp.heanet.ie/mirrors/www.mysql.com/Downloads/MySQL-$(BASE_VERSION)/
MASTER_SITES += http://mysql.skynet.be/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(VERSION).tar.gz
DISTFILES += csw$(NAME).tpl
DISTFILES += quick_start-csw
DISTFILES += README.CSW
DISTFILES += ChangeLog
DISTFILES += CSW$(NAME).preinstall
DISTFILES += CSW$(NAME).postinstall
DISTFILES += cswusergroup
DISTFILES += map.mysql

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWcmake
BUILD_DEP_PKGS += CSWbison

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += "-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON"
CMAKE_ARGS += -DINSTALL_LAYOUT=RPM
CMAKE_ARGS += -DMYSQL_DATADIR=$(localstatedir)
CMAKE_ARGS += -DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS += -DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
CMAKE_ARGS += -DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS += -DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/plugin
CMAKE_ARGS += -DWITH_LIBWRAP=1
CMAKE_ARGS += -DWITH_SSL=system
CMAKE_ARGS += -DWITH_ZLIB=system
CMAKE_ARGS += -DDEFAULT_CHARSET=utf8
CMAKE_ARGS += -DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS += -DCOMPILATION_COMMENT='OpenCSW'
CMAKE_ARGS += -DBUILD_CONFIG=mysql_release
CMAKE_ARGS += -DOPENSSL_ROOT_DIR=$(prefix)
CMAKE_ARGS += -DC_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_C_LINK_FLAGS="$(LDFLAGS)"
CMAKE_ARGS += -DCMAKE_CXX_LINK_FLAGS="$(LDFLAGS)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS += -DBISON_EXECUTABLE=/opt/csw/bin/bison

# The line below come from the official MySQL build configuration
CMAKE_ARGS += "-DENABLED_PROFILING:BOOL=ON"
CMAKE_ARGS += "-DENABLE_DEBUG_SYNC:BOOL=ON"
CMAKE_ARGS += "-DENABLE_DOWNLOADS:BOOL=OFF"
CMAKE_ARGS += "-DENABLE_GCOV:BOOL=OFF"
CMAKE_ARGS += "-DENABLE_GPROF:BOOL=OFF"
CMAKE_ARGS += "-DENABLE_MEMCACHED_SASL:BOOL=OFF"
CMAKE_ARGS += "-DENABLE_MEMCACHED_SASL_PWDB:BOOL=OFF"
CMAKE_ARGS += "-DFEATURE_SET:STRING=community"
CMAKE_ARGS += "-DMYSQL_MAINTAINER_MODE:BOOL=OFF"
CMAKE_ARGS += "-DOPTIMIZER_TRACE:BOOL=ON"
CMAKE_ARGS += "-DWITH_ARCHIVE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_BLACKHOLE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_DEBUG:BOOL=OFF"
CMAKE_ARGS += "-DWITH_DEFAULT_COMPILER_OPTIONS:BOOL=ON"
CMAKE_ARGS += "-DWITH_DEFAULT_FEATURE_SET:BOOL=ON"
CMAKE_ARGS += "-DWITH_EDITLINE:STRING=bundled"
CMAKE_ARGS += "-DWITH_EMBEDDED_SERVER:BOOL=ON"
CMAKE_ARGS += "-DWITH_EXAMPLE_STORAGE_ENGINE:BOOL=OFF"
CMAKE_ARGS += "-DWITH_EXTRA_CHARSETS:STRING=all"
CMAKE_ARGS += "-DWITH_FEDERATED_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_INNOBASE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_INNODB_MEMCACHED:BOOL=1"
CMAKE_ARGS += "-DWITH_LIBEVENT:STRING=bundled"
CMAKE_ARGS += "-DWITH_LIBWRAP:BOOL=OFF"
CMAKE_ARGS += "-DWITH_PARTITION_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_PERFSCHEMA_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_PIC:BOOL=ON"
CMAKE_ARGS += "-DWITH_READLINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_UNIT_TESTS:BOOL=ON"
CMAKE_ARGS += "-DWITH_VALGRIND:BOOL=OFF"
CMAKE_ARGS += "-DENABLE_DTRACE:BOOL=ON"

USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS = dbdir
PROTOTYPE_FILES_dbdir = $(localstatedir)
PROTOTYPE_USER_dbdir = mysql
PROTOTYPE_GROUP_dbdir = mysql
PROTOTYPE_PERMS_dbdir = 0700
PROTOTYPE_CLASS_dbdir = ugfiles

CHECKPKG_OVERRIDES_CSW$(NAME) += surplus-dependency|CSW$(NAME)client
CHECKPKG_OVERRIDES_CSW$(NAME)bench += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME)bench += surplus-dependency|CSW$(NAME)
CHECKPKG_OVERRIDES_CSW$(NAME)test += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME)test += surplus-dependency|CSW$(NAME)

# This could be reviewed.
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

EXECUTABLES += innochecksum
EXECUTABLES += msql2mysql
EXECUTABLES += my_print_defaults
EXECUTABLES += myisam_ftdump
EXECUTABLES += myisamchk
EXECUTABLES += myisamlog
EXECUTABLES += myisampack
EXECUTABLES += mysql
EXECUTABLES += mysql_client_test
EXECUTABLES += mysql_config
EXECUTABLES += mysql_convert_table_format
EXECUTABLES += mysql_find_rows
EXECUTABLES += mysql_fix_extensions
EXECUTABLES += mysql_plugin
EXECUTABLES += mysql_secure_installation
EXECUTABLES += mysql_setpermission
EXECUTABLES += mysql_tzinfo_to_sql
EXECUTABLES += mysql_upgrade
EXECUTABLES += mysql_waitpid
EXECUTABLES += mysql_zap
EXECUTABLES += mysqlaccess
EXECUTABLES += mysqlaccess.conf
EXECUTABLES += mysqladmin
EXECUTABLES += mysqlbinlog
EXECUTABLES += mysqlbug
EXECUTABLES += mysqlcheck
EXECUTABLES += mysqld
EXECUTABLES += mysqld_multi
EXECUTABLES += mysqld_safe
EXECUTABLES += mysqldump
EXECUTABLES += mysqldumpslow
EXECUTABLES += mysqlhotcopy
EXECUTABLES += mysqlimport
EXECUTABLES += mysqlshow
EXECUTABLES += mysqlslap
EXECUTABLES += mysqltest
EXECUTABLES += perror
EXECUTABLES += replace
EXECUTABLES += resolve_stack_dump
EXECUTABLES += resolveip

CONFIGURE_SCRIPTS = custom

TEST_TARGET = test

include gar/category.mk

configure-custom:
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)

post-configure-modulated:
	gsed \
		-e 's+@prefix@+$(prefix)+g' \
		-e 's+@localstatedir@+$(localstatedir)+g' \
		-e 's+@sysconfdir@+$(sysconfdir)+g' \
		-e 's+@bindir@+$(bindir)+g' \
		-e 's+@BASE_VERSION@+$(BASE_VERSION)+g' \
		< $(WORKDIR)/csw$(NAME).tpl \
		> $(WORKDIR)/csw$(NAME)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/csw$(NAME) $(DESTDIR)$(sysconfdir)/init.d
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18; \
		ln -s libmysqlclient.so.18 libmysqlclient_r.so.18)
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18.0.0; \
		ln -s libmysqlclient.so.18.0.0 libmysqlclient_r.so.18.0.0)
	# Do not distribute libstlport with MySQL, use a separate one
	(cd $(DESTDIR)$(libdir); rm libstlport.*)
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/$(NAME)/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/$(NAME)/doc/ChangeLog-$(BASE_VERSION)
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/$(NAME)/doc/README-$(BASE_VERSION).CSW
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/$(NAME)/doc
	gln -sf ../../../$(NAME)/share/$(NAME)/doc/README-$(BASE_VERSION).CSW \
		$(PKGROOT)/opt/csw/share/$(NAME)/doc/README-$(BASE_VERSION).CSW
	# The quick_start-csw file is almost the same as postinstall.
	# [ -d $(PKGROOT)$(datadir)/mysql ]
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)
