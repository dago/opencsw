# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# Upstream bug filed:
# http://bugs.mysql.com/bug.php?id=62567

PROJ_NAME = mysql
NAME = $(PROJ_NAME)5
BASE_VERSION = 5.0
PATCHLEVEL = 92
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server

# PACKAGING_PLATFORMS = solaris9-sparc solaris10-sparc

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

DISTNAME = mysql-$(VERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

# Change prefix to /opt/csw/$(NAME)
prefix = $(BUILD_PREFIX)/$(NAME)
localstatedir = /var$(prefix)
sysconfdir = /etc$(prefix)
libdir_install = $(BUILD_PREFIX)/lib
includedir = $(BUILD_PREFIX)/include

#  --bindir=/opt/csw/mysql5/bin
#  --datadir=/opt/csw/mysql5/share
#  --exec_prefix=/opt/csw/mysql5
#  --infodir=/opt/csw/mysql5/share/info
#  --libexecdir=/opt/csw/mysql5/libexec
#  --mandir=/opt/csw/mysql5/share/man
#  --prefix=/opt/csw/mysql5
#  --sbindir=/opt/csw/mysql5/sbin
#  --sharedstatedir=/opt/csw/mysql5/share

# Where to put the init script
global_sysconfdir = /etc$(BUILD_PREFIX)
# Where to link the binaries
global_bindir = $(BUILD_PREFIX)/bin

INITSMF = $(sysconfdir)/init\.d/csw$(NAME)

MYSQL_LIB_VER = 15

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
PKGFILES_CSWmysql-dev  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSWmysql-dev  += $(prefix)/include.*
PKGFILES_CSWmysql-dev  += /opt/csw/include/mysql
OBSOLETED_BY_CSWmysql-dev = CSWmysql5devel
CHECKPKG_OVERRIDES_CSWmysql-dev += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysql_config.1

PACKAGES += CSWlibmysqlclient$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibz1
OBSOLETED_BY_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSW$(NAME)rt

PACKAGES += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient_r\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient_r.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += CSWlibz1
OBSOLETED_BY_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += CSW$(NAME)rt

PACKAGES += CSW$(NAME)client
SPKG_DESC_CSW$(NAME)client = MySQL $(BASE_VERSION) client binaries
RPKGFILES_CSW$(NAME)client  = $(bindir)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/sbin/$(bin_name))
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibz1
CHECKPKG_OVERRIDES_CSWmysql5client += bad-rpath-entry
# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
CSW$(NAME)client_programs += myisamlog
CSW$(NAME)client_programs += myisampack
CSW$(NAME)client_programs += mysql
CSW$(NAME)client_programs += mysqlaccess
CSW$(NAME)client_programs += mysqladmin
CSW$(NAME)client_programs += mysqlbin
CSW$(NAME)client_programs += mysqlbinlog
CSW$(NAME)client_programs += mysqlcheck
CSW$(NAME)client_programs += mysql_client_test
CSW$(NAME)client_programs += mysqldump
CSW$(NAME)client_programs += mysqlhotcopy
CSW$(NAME)client_programs += mysqlimport
CSW$(NAME)client_programs += mysqlshow
CSW$(NAME)client_programs += mysql_zap
CSW$(NAME)client_programs += perror
CSW$(NAME)client_programs += replace

PACKAGES += CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient$(MYSQL_LIB_VER)
SPKG_DESC_CSW$(NAME) = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME) += CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibwrap1
CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

PACKAGES += CSW$(NAME)bench
PACKAGES += CSW$(NAME)test

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
# PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch
PATCHFILES += 0004-looking-for-ps-use-basename-0.patch

SPKG_DESC_CSW$(NAME)bench  = MySQL $(BASE_VERSION) benchmarking
SPKG_DESC_CSW$(NAME)test   = MySQL $(BASE_VERSION) testing files

CATALOGNAME_CSW$(NAME)bench  = $(NAME)bench
CATALOGNAME_CSW$(NAME)test   = $(NAME)test

EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
ARCHALL_CSW$(NAME)bench = 1
ARCHALL_CSW$(NAME)test  = 1


# Enable 64 bits build
BUILD64 = 1

PKGFILES_CSW$(NAME)bench   = $(prefix)/sql-bench.*

PKGFILES_CSW$(NAME)test    = $(prefix)/mysql-test.*

RUNTIME_DEP_PKGS_CSW$(NAME)bench       = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)bench      += CSWperl
RUNTIME_DEP_PKGS_CSW$(NAME)test        = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)test       += CSWperl

MASTER_SITES = http://ftp.heanet.ie/mirrors/www.mysql.com/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(VERSION).tar.gz
DISTFILES += csw$(NAME) quick_start-csw README.CSW ChangeLog
DISTFILES += CSW$(NAME).preinstall
DISTFILES += CSW$(NAME).postinstall
DISTFILES += cswusergroup

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)


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

CHECKPKG_OVERRIDES_CSW$(NAME)client += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysqlaccess.1
# This could be reviewed.
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

EXECUTABLES += comp_err
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
EXECUTABLES += mysql_explain_log
EXECUTABLES += mysql_find_rows
EXECUTABLES += mysql_fix_extensions
EXECUTABLES += mysql_fix_privilege_tables
EXECUTABLES += mysql_install_db
EXECUTABLES += mysql_secure_installation
EXECUTABLES += mysql_setpermission
EXECUTABLES += mysql_tableinfo
EXECUTABLES += mysql_tzinfo_to_sql
EXECUTABLES += mysql_upgrade
EXECUTABLES += mysql_upgrade_shell
EXECUTABLES += mysql_waitpid
EXECUTABLES += mysql_zap
EXECUTABLES += mysqlaccess
EXECUTABLES += mysqladmin
EXECUTABLES += mysqlbinlog
EXECUTABLES += mysqlbug
EXECUTABLES += mysqlcheck
EXECUTABLES += mysqld_multi
EXECUTABLES += mysqld_safe
EXECUTABLES += mysqldump
EXECUTABLES += mysqldumpslow
EXECUTABLES += mysqlhotcopy
EXECUTABLES += mysqlimport
EXECUTABLES += mysqlshow
EXECUTABLES += mysqltest
EXECUTABLES += mysqltestmanager
EXECUTABLES += mysqltestmanager-pwgen
EXECUTABLES += mysqltestmanagerc
EXECUTABLES += perror
EXECUTABLES += replace
EXECUTABLES += resolve_stack_dump
EXECUTABLES += resolveip

ALTERNATIVES =
ALTERNATIVES_CSW$(NAME) = 

# This list could be generated automatically from $(EXECUTABLES)
# /home/maciej/src/opencsw/.buildsys/v2/gar//gar.pkg.mk:833: *** The variable 'ALTERNATIVE_comp_err' is empty, but must contain an alternative.  Stop.
ALTERNATIVES_CSW$(NAME)client = mysql$(BASE_VERSION)
ALTERNATIVE_mysql$(BASE_VERSION) = $(global_bindir)/$(firstword $(CSW$(NAME)client_programs)) mysql $(bindir)/$(firstword $(CSW$(NAME)client_programs)) 50
ALTERNATIVE_mysql$(BASE_VERSION) += $(foreach C,$(wordlist 2,$(words $(CSW$(NAME)client_programs)),$(CSW$(NAME)client_programs)),\
	$(global_bindir)/$C $C $(bindir)/$C)

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

test-custom:
	alias sh=/usr/bin/bash;                           \
		cd $(WORKSRC)/mysql-test;                       \
		perl mysql-test-run.pl --mem --big-test --force \
		--skip-test=archive-big --skip-test=/gis/

pre-configure-modulated:
	# To work around the following libtool version mismatch problem:
	# libtool: Version mismatch error.  This is libtool 2.2.6, but the
	# libtool: definition of this LT_INIT comes from libtool 2.2.6b.
	# libtool: You should recreate aclocal.m4 with macros from libtool 2.2.6
	# http://lists.opencsw.org/pipermail/maintainers/2009-December/005066.html
	cd $(WORKSRC) && autoreconf --force --install --symlink
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(DESTDIR)$(libdir); gmv -v mysql/* .)
	(cd $(DESTDIR)$(libdir); grmdir -v mysql)
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/$(NAME)/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/$(NAME)/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/$(NAME)/doc
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/$(NAME)/doc
	gln -sf ../../../$(NAME)/share/$(NAME)/doc/README.CSW \
		$(PKGROOT)/opt/csw/share/$(NAME)/doc/README.CSW
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/csw$(NAME) $(PKGROOT)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	# Create symlinks to binaries
	ginstall -m 755 -d $(PKGROOT)$(global_bindir)
	#for f in $(PKGROOT)$(bindir)/*; do \
	#	if echo $$f | grep amd64$$; then continue; fi; \
	#	if echo $$f | grep sparcv9$$; then continue; fi; \
	#	ln -s ../$(NAME)/bin/`basename $$f` \
	#	      $(PKGROOT)$(global_bindir)/`basename $$f`; \
	#done
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)

# We need the GNU userland (nobody knows why)
PATH := /opt/csw/gnu:$(PATH)
