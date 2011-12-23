# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# If you are involved in packaging MySQL, consider subscribing to the
# packagers mailing list:
# http://lists.mysql.com/packagers

PROJ_NAME = mysql
NAME = $(PROJ_NAME)55
BASE_VERSION = 5.5
PATCHLEVEL = 19
ALTS_PRIO = 55
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

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

# There are problems with the build using Sun Studio.
GARCOMPILER = GNU

INITSMF = $(sysconfdir)/init\.d/csw$(NAME)

# Existing databases are in this location
localstatedir = /var$(BUILD_PREFIX)/$(NAME)
# To avoid file conflicts
datadir = $(prefix)/share/mysql/$(BASE_VERSION)

MYSQL_LIB_VER = 18

PACKAGES += CSWmysql-dev
SPKG_DESC_CSWmysql-dev = MySQL development files
PKGFILES_CSWmysql-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient$(MYSQL_LIB_VER)
CSWmysql-dev_programs += mysql_config
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(call baseisadirs,$(bindir),$(bin_name)$(PROGRAM_SUFFIX)))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(mandir)/man1/$(bin_name)\.1$(PROGRAM_SUFFIX))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),/opt/csw/bin/$(bin_name)$(PROGRAM_SUFFIX))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),/opt/csw/sbin/$(bin_name)$(PROGRAM_SUFFIX))
PKGFILES_CSWmysql-dev  += $(mandir)/man1/mysql_config.*
PKGFILES_CSWmysql-dev  += $(prefix)/include.*
PKGFILES_CSWmysql-dev  += /opt/csw/include/mysql
CHECKPKG_OVERRIDES_CSWmysql-dev += file-with-bad-content|/usr/local|root$(mandir)/man1/mysql_config$(PROGRAM_SUFFIX).1
ALTERNATIVES_CSWmysql-dev = mysql_dev
ALTERNATIVE_mysql_dev = $(bindir)/$(firstword $(CSWmysql-dev_programs)) mysql_dev $(bindir)/$(firstword $(CSWmysql-dev_programs)) $(ALTS_PRIO)
ALTERNATIVE_mysql_dev += $(foreach C,$(wordlist 2,$(words $(CSWmysql-dev_programs)),$(CSWmysql-dev_programs)),\
	$(bindir)/$C $C $(bindir)/$C$(PROGRAM_SUFFIX))
ALTERNATIVE_mysql_dev += $(foreach C,$(wordlist 2,$(words $(CSWmysql-dev_programs)),$(CSWmysql-dev_programs)),\
	$(mandir)/man1/$(C).1 $C $(mandir)/man1/$(C)$(PROGRAM_SUFFIX).1)

PATCHFILES += 0003-I-HATE-CMAKE.patch
PATCHFILES += 0003-WHY-IS-CMAKE-TRYING-TO-BE-SMARTER-THAN-ME.patch

PACKAGES += CSWlibmysqlclient$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibmysqlclient18 += CSWlibgcc-s1

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
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(call baseisadirs,$(bindir),$(bin_name)$(PROGRAM_SUFFIX)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(mandir)/man1/$(bin_name)$(PROGRAM_SUFFIX)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),/opt/csw/bin/$(bin_name)$(PROGRAM_SUFFIX))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),/opt/csw/sbin/$(bin_name)$(PROGRAM_SUFFIX))
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWosslrt
CHECKPKG_OVERRIDES_CSW$(NAME)client += bad-rpath-entry
# It's intentional. There's a sparcv8-incompatible assembler code there.
CHECKPKG_OVERRIDES_CSW$(NAME)client_isa-sparcv8plus += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSW$(NAME)client += CHECKPKG_OVERRIDES_CSW$(NAME)client_$(ISA)

PACKAGES += CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient$(MYSQL_LIB_VER)
SPKG_DESC_CSW$(NAME) = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME) += CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibwrap1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWosslrt
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/mysql-test.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/sql-bench.*

PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch

# Enable 64 bits build
BUILD64 = 1

MASTER_SITES = http://ftp.heanet.ie/mirrors/www.mysql.com/Downloads/MySQL-$(BASE_VERSION)/
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

PROGRAM_SUFFIX = -$(BASE_VERSION)
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
CONFIGURE_ARGS += --program-suffix=$(PROGRAM_SUFFIX)

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DMYSQL_DATADIR=$(localstatedir)
CMAKE_ARGS += -DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS += -DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
CMAKE_ARGS += -DINSTALL_MANDIR=$(subst $(prefix)/,,$(mandir))
CMAKE_ARGS += -DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS += -DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/$(MM_LIBDIR)/plugin
CMAKE_ARGS += -DWITH_READLINE=1
CMAKE_ARGS += -DWITH_SSL=system
CMAKE_ARGS += -DWITH_ZLIB=system
CMAKE_ARGS += -DDEFAULT_CHARSET=utf8
CMAKE_ARGS += -DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS += -DWITH_COMMENT='OpenCSW'
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)" -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DBUILD_CONFIG=mysql_release
# CMAKE_ARGS += -DOPENSSL_INCLUDE_DIR="$(includedir)"
# CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
# CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DOPENSSL_ROOT_DIR=$(prefix)
# CMAKE_ARGS += -DOPENSSL_SSL_LIBRARIES=$(libdir)/$(MM_LIBDIR)/libssl.so
# CMAKE_ARGS += -DOPENSSL_CRYPTO_LIBRARIES=$(libdir)/$(MM_LIBDIR)/libcrypto.so
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"

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

CHECKPKG_OVERRIDES_CSW$(NAME)client += file-with-bad-content|/usr/local|root$(prefix)/share/man/man1/mysqlaccess$(PROGRAM_SUFFIX).1
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

ALTERNATIVES_CSW$(NAME) = mysql$(BASE_VERSION)_main
ALTERNATIVE_mysql$(BASE_VERSION)_main = $(bindir)/$(firstword $(EXECUTABLES)) mysql_main $(bindir)/$(firstword $(EXECUTABLES))$(PROGRAM_SUFFIX) $(ALTS_PRIO)
ALTERNATIVE_mysql$(BASE_VERSION)_main += $(foreach C,$(wordlist 2,$(words $(EXECUTABLES)),$(EXECUTABLES)),\
	$(bindir)/$C $C $(bindir)/$C$(PROGRAM_SUFFIX))

ALTERNATIVES_CSW$(NAME)client = mysql$(BASE_VERSION)_client
ALTERNATIVE_mysql$(BASE_VERSION)_client = $(bindir)/$(firstword $(client_programs)) mysql_client $(bindir)/$(firstword $(client_programs)) $(ALTS_PRIO)
ALTERNATIVE_mysql$(BASE_VERSION)_client += $(foreach C,$(wordlist 2,$(words $(client_programs)),$(client_programs)),\
	$(bindir)/$C $C $(bindir)/$C$(PROGRAM_SUFFIX))
ALTERNATIVE_mysql$(BASE_VERSION)_client += $(foreach C,$(wordlist 2,$(words $(client_programs)),$(client_programs)),\
	$(mandir)/man1/$(C).1 $C $(mandir)/man1/$(C)$(PROGRAM_SUFFIX).1)

# These are harmless, although it would be nice to clean them up eventually.
# Help appreciated?
CHECKPKG_OVERRIDES_CSWmysql51 += file-collision|/opt/csw/share/doc/mysql5devel_stub/README.CSW|CSWmysql5|CSWmysql51
CHECKPKG_OVERRIDES_CSWmysql51 += file-collision|/opt/csw/share/doc/mysql_dev/README.CSW|CSWmysql5|CSWmysql51
CHECKPKG_OVERRIDES_CSWmysql51 += file-collision|/opt/csw/share/info/mysql.info|CSWmysql5|CSWmysql51

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
	# (cd $(DESTDIR)$(libdir); gmv -v mysql/* .)
	# (cd $(DESTDIR)$(libdir); grmdir -v mysql)
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/csw$(NAME) $(DESTDIR)$(sysconfdir)/init.d
	# Add versions to binary names
	for f in $(EXECUTABLES); do \
		gmv -v "$(DESTDIR)$(bindir)/$${f}" \
		       "$(DESTDIR)$(bindir)/$${f}$(PROGRAM_SUFFIX)"; \
	done
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18; \
		ln -s libmysqlclient.so.18 libmysqlclient_r.so.18)
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18.0.0; \
		ln -s libmysqlclient.so.18.0.0 libmysqlclient_r.so.18.0.0)
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/$(NAME)/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/$(NAME)/doc/ChangeLog-$(BASE_VERSION)
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/$(NAME)/doc/README-$(BASE_VERSION).CSW
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/$(NAME)/doc
	gln -sf ../../../$(NAME)/share/$(NAME)/doc/README.CSW \
		$(PKGROOT)/opt/csw/share/$(NAME)/doc/README.CSW
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)

# We need the GNU userland (nobody knows why)
PATH := /opt/csw/gnu:$(PATH)
