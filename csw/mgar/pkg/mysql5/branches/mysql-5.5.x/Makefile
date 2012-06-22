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


PROJ_NAME = mysql
NAME = $(PROJ_NAME)5
BASE_VERSION = 5.5
PATCHLEVEL = 25
ALTS_PRIO = 55
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# There is some assembler code, which doesn't work on sparcv8, and I don't see
# an easy way to switch it off.
ISA_DEFAULT_sparc-5.9 = sparcv8plus

DISTNAME = mysql-$(VERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

EXTRA_CFLAGS += -mt -D__EXTENSIONS__
EXTRA_CXXFLAGS += -mt -D__EXTENSIONS__

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
CHECKPKG_OVERRIDES_CSWmysql-dev += file-with-bad-content|/usr/local|root$(mandir)/man1/mysql_config.1
CHECKPKG_OVERRIDES_CSWmysql-dev += file-with-bad-content|/usr/local|root$(mandir)/man1/mysql_config.1
PATCHFILES += 0003-I-HATE-CMAKE.patch
PATCHFILES += 0003-WHY-IS-CMAKE-TRYING-TO-BE-SMARTER-THAN-ME.patch

PACKAGES += CSWlibmysqlclient$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_5.9 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_$(GAROSREL))

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
# RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient$(MYSQL_LIB_VER)
# RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
# RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)client_5.9 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSW$(NAME)client_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)client += $(RUNTIME_DEP_PKGS_CSW$(NAME)client_$(GAROSREL))
CHECKPKG_OVERRIDES_CSW$(NAME)client += bad-rpath-entry

# It's intentional. There's a sparcv8-incompatible assembler code there, so we
# must build for sparcv8+ on Solaris 9.
CHECKPKG_OVERRIDES_CSW$(NAME)client += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSW$(NAME) += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWlibmysqlclient18 += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWlibmysqlclient18 += bad-rpath-entry

PACKAGES += CSW$(NAME)
# RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
# RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient$(MYSQL_LIB_VER)
SPKG_DESC_CSW$(NAME) = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME) += CSW$(NAME)client
# RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibwrap1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)_5.9 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSW$(NAME)_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME) += $(RUNTIME_DEP_PKGS_CSW$(NAME)_$(GAROSREL))
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/mysql-test.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/sql-bench.*
EXTRA_MERGE_EXCLUDE_FILES += $(datadir)/mysql-test.*


# Enable 64 bits build
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

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWcmake
BUILD_DEP_PKGS += CSWbison

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
# Why not have a docs package?
# CONFIGURE_ARGS += --without-docs
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-charset=utf8
CONFIGURE_ARGS += --with-extra-charsets=all
CONFIGURE_ARGS += --with-low-memory
CONFIGURE_ARGS += --with-pthread
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-zlib-dir=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-ssl=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-plugins=max-no-ndb
CONFIGURE_ARGS += --with-comment="(OpenCSW)"
CONFIGURE_ARGS += --with-mysqld-user=mysql
CONFIGURE_ARGS += --with-fast-mutexes
CONFIGURE_ARGS += --with-libwrap
CONFIGURE_ARGS += --with-mysqld-libs=-lmtmalloc
CONFIGURE_ARGS += --with-big-tables
CONFIGURE_ARGS += --enable-thread-safe-client
CONFIGURE_ARGS_DBG = --with-debug
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DINSTALL_LAYOUT=RPM
CMAKE_ARGS += -DMYSQL_DATADIR=$(localstatedir)
CMAKE_ARGS += -DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS += -DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
# CMAKE_ARGS += -DINSTALL_MANDIR=$(subst $(prefix)/,,$(mandir))
CMAKE_ARGS += -DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS += -DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/plugin
CMAKE_ARGS += -DWITH_READLINE=1
CMAKE_ARGS += -DWITH_LIBWRAP=1
CMAKE_ARGS += -DWITH_SSL=system
CMAKE_ARGS += -DWITH_ZLIB=system
CMAKE_ARGS += -DDEFAULT_CHARSET=utf8
CMAKE_ARGS += -DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS += -DWITH_COMMENT='OpenCSW'
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DBUILD_CONFIG=mysql_release
# CMAKE_ARGS += -DOPENSSL_INCLUDE_DIR="$(includedir)"
# CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
# CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DOPENSSL_ROOT_DIR=$(prefix)
# CMAKE_ARGS += -DOPENSSL_SSL_LIBRARIES=$(libdir)/libssl.so
# CMAKE_ARGS += -DOPENSSL_CRYPTO_LIBRARIES=$(libdir)/libcrypto.so
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += "-DCMAKE_C_FLAGS=$(CFLAGS)"
CMAKE_ARGS += "-DCMAKE_CXX_FLAGS=$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON

# TODO: Make the tests pass. They don't at the moment.
SKIPTEST ?= 1
TEST_SCRIPTS = custom
TEST_TARGETS = check

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

CHECKPKG_OVERRIDES_CSW$(NAME)client += file-with-bad-content|/usr/local|root$(prefix)/share/man/man1/mysqlaccess.1
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

include gar/category.mk

test-custom:
	alias sh=/usr/bin/bash;                           \
		cd $(WORKSRC)/mysql-test;                       \
		perl mysql-test-run.pl --mem --big-test --force \
		--skip-test=archive-big --skip-test=/gis/

configure-custom:
	#		--debug-output \
	#		--debug-trycompile \
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)

post-configure-modulated:
	gsed \
		-e 's+@prefix@+$(prefix)+' \
		-e 's+@localstatedir@+$(localstatedir)+' \
		-e 's+@sysconfdir@+$(sysconfdir)+' \
		-e 's+@bindir@+$(bindir)+' \
		-e 's+@BASE_VERSION@+$(BASE_VERSION)+' \
		< $(WORKDIR)/csw$(NAME).tpl \
		> $(WORKDIR)/csw$(NAME)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/csw$(NAME) $(DESTDIR)$(sysconfdir)/init.d
	# # Add versions to binary names
	# for f in $(EXECUTABLES); do \
	# 	gmv -v "$(DESTDIR)$(bindir)/$${f}" \
	# 	       "$(DESTDIR)$(bindir)/$${f}"; \
	# done
	(cd $(DESTDIR)$(libdir_install); rm libmysqlclient_r.so.18; \
		ln -s libmysqlclient.so.18 libmysqlclient_r.so.18)
	(cd $(DESTDIR)$(libdir_install); rm libmysqlclient_r.so.18.0.0; \
		ln -s libmysqlclient.so.18.0.0 libmysqlclient_r.so.18.0.0)
	# gmv -vf $(DESTDIR)$(mandir)/man1/mysql_config.1
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
	# ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)
