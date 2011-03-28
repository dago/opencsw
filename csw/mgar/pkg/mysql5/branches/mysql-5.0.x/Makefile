# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# 5.0.90 doesn't build:
# http://bugs.mysql.com/bug.php?id=50409
# Let's wait for 5.0.91.

PROJ_NAME = mysql
NAME = $(PROJ_NAME)5
BASE_VERSION = 5.0
PATCHLEVEL = 87
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server

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
prefix = /opt/csw/$(NAME)
localstatedir = /var$(prefix)
sysconfdir = /etc/opt/csw
libdir = /opt/csw/lib
includedir = /opt/csw/include

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
global_sysconfdir = /etc/opt/csw
# Where to link the binaries
global_bindir = /opt/csw/bin

INITSMF = $(global_sysconfdir)/init\.d/csw$(NAME)

PACKAGES += CSWlibmysqlclient15
PKGFILES_CSWlibmysqlclient15 += $(call baseisadirs,$(libdir),libmysqlclient\.so\.15(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient15 += MySQL $(BASE_VERSION) client library, libmysqlclient.so.15
RUNTIME_DEP_PKGS_CSWlibmysqlclient15 += CSWzlib
OBSOLETED_BY_CSWlibmysqlclient15 += CSWmysql5rt

PACKAGES += CSWlibmysqlclient-r15
PKGFILES_CSWlibmysqlclient-r15 += $(call baseisadirs,$(libdir),libmysqlclient_r\.so\.15(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient-r15 += MySQL $(BASE_VERSION) client library, libmysqlclient_r.so.15
RUNTIME_DEP_PKGS_CSWlibmysqlclient-r15 += CSWzlib
OBSOLETED_BY_CSWlibmysqlclient-r15 += CSWmysql5rt

PACKAGES += CSW$(NAME)client
SPKG_DESC_CSW$(NAME)client = MySQL $(BASE_VERSION) client binaries
RPKGFILES_CSW$(NAME)client  = $(bindir)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/sbin/$(bin_name))
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWncurses
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWzlib
# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
CSW$(NAME)client_programs  = myisamlog
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
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient-r15
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibmysqlclient15
SPKG_DESC_CSW$(NAME)       = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME)           += CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME)           += CSWzlib

PACKAGES += CSW$(NAME)bench
PACKAGES += CSW$(NAME)devel
PACKAGES += CSW$(NAME)test

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch

SPKG_DESC_CSW$(NAME)bench  = MySQL $(BASE_VERSION) benchmarking
SPKG_DESC_CSW$(NAME)devel  = MySQL $(BASE_VERSION) header files
SPKG_DESC_CSW$(NAME)test   = MySQL $(BASE_VERSION) testing files

CATALOGNAME_CSW$(NAME)bench  = $(NAME)bench
CATALOGNAME_CSW$(NAME)devel  = $(NAME)devel
CATALOGNAME_CSW$(NAME)test   = $(NAME)test

ARCHALL_CSW$(NAME)bench = 1
ARCHALL_CSW$(NAME)test  = 1

CSW$(NAME)devel_programs += mysql_config

# Enable 64 bits build
BUILD64 = 1

PKGFILES_CSW$(NAME)bench   = $(prefix)/sql-bench.*
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSW$(NAME)devel  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSW$(NAME)devel  += $(prefix)/include.*
PKGFILES_CSW$(NAME)devel  += /opt/csw/include/mysql

PKGFILES_CSW$(NAME)test    = $(prefix)/mysql-test.*

RUNTIME_DEP_PKGS_CSW$(NAME)bench       = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)bench      += CSWperl
RUNTIME_DEP_PKGS_CSW$(NAME)test        = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)test       += CSWperl

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(VERSION).tar.gz
DISTFILES += csw$(NAME) quick_start-csw README.CSW ChangeLog
DISTFILES += CSW$(NAME).preinstall
DISTFILES += CSW$(NAME).postinstall
DISTFILES += cswusergroup

UFILES_REGEX = mysql-(\d+(?:\.\d+)*).tar.gz

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__

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
CONFIGURE_ARGS += --with-zlib-dir=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-plugins=max-no-ndb
CONFIGURE_ARGS += --with-comment
CONFIGURE_ARGS += --with-mysqld-libs=-lmtmalloc
CONFIGURE_ARGS += --with-big-tables
CONFIGURE_ARGS += --enable-thread-safe-client
CONFIGURE_ARGS_DBG = --with-debug
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# TODO: Make the tests pass. They don't at the moment.
TEST_SCRIPTS =


USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS = dbdir
PROTOTYPE_FILES_dbdir = $(localstatedir)
PROTOTYPE_USER_dbdir = mysql
PROTOTYPE_GROUP_dbdir = mysql
PROTOTYPE_PERMS_dbdir = 0700
PROTOTYPE_CLASS_dbdir = ugfiles

CHECKPKG_OVERRIDES_CSWmysql5 += surplus-dependency|CSWmysql5client
CHECKPKG_OVERRIDES_CSWmysql5bench += file-with-bad-content
CHECKPKG_OVERRIDES_CSWmysql5bench += surplus-dependency|CSWmysql5
CHECKPKG_OVERRIDES_CSWmysql5test += file-with-bad-content
CHECKPKG_OVERRIDES_CSWmysql5test += surplus-dependency|CSWmysql5

CHECKPKG_OVERRIDES_CSWmysql5client += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysqlaccess.1
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/info/mysql.info
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/myisam_ftdump.1
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysqld_multi.1
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysqld_safe.1
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysqldumpslow.1
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man8/mysqlmanager.8
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/mysql/mysqld_multi.server
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/bin/sparcv8/mysqlbug
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/bin/sparcv9/mysqlbug
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/export/home|root/opt/csw/mysql5/share/info/mysql.info
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/share|root/opt/csw/mysql5/share/info/mysql.info
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/share|root/opt/csw/mysql5/share/man/man1/mysql_tzinfo_to_sql.1
CHECKPKG_OVERRIDES_CSWmysql5devel += file-with-bad-content|/usr/local|root/opt/csw/mysql5/share/man/man1/mysql_config.1

CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/bin/i386/mysqlbug
CHECKPKG_OVERRIDES_CSWmysql5 += file-with-bad-content|/usr/local|root/opt/csw/mysql5/bin/amd64/mysqlbug

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
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/mysql/doc
	gln -sf ../../../$(NAME)/share/mysql/doc/README.CSW \
		$(PKGROOT)/opt/csw/share/mysql/doc/README.CSW
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/csw$(NAME) $(PKGROOT)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	# Create symlinks to binaries
	ginstall -m 755 -d $(PKGROOT)$(global_bindir)
	for f in $(PKGROOT)$(bindir)/*; do \
		if echo $$f | grep amd64$$; then continue; fi; \
		if echo $$f | grep sparcv9$$; then continue; fi; \
		ln -s ../$(NAME)/bin/`basename $$f` \
		      $(PKGROOT)$(global_bindir)/`basename $$f`; \
	done
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)

show-dirpaths:
	echo $(DIRPATHS)
