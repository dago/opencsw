# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = mysql5
BASE_VERSION = 5.1
PATCHLEVEL = 40
GARVERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server

# Useful when making a series of builds on the same day
GARFLAVOR = DBG

DISTNAME = mysql-$(GARVERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

bindir_install = $(prefix)/bin/$(GARNAME)/$(BASE_VERSION)
datadir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)
docdir=$(prefix)/share/doc/$(GARNAME)/$(BASE_VERSION)
includedir=$(prefix)/include/$(GARNAME)/$(BASE_VERSION)
infodir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/info
libdir_install =$(prefix)/lib/$(GARNAME)/$(BASE_VERSION)
libexecdir_install =$(prefix)/libexec/$(GARNAME)/$(BASE_VERSION)
lispdir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/emacs/site-lisp
localstatedir = /var$(prefix)/$(GARNAME)/$(BASE_VERSION)
mandir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/man
sbindir_install = $(prefix)/sbin/$(GARNAME)/$(BASE_VERSION)
sharedstatedir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)
sourcedir=$(prefix)/src/$(GARNAME)/$(BASE_VERSION)
sysconfdir = /etc$(prefix)/$(GARNAME)/$(BASE_VERSION)

# Where to put the init script
global_sysconfdir = /etc$(prefix)
# Where to link the binaries
global_bindir = /opt$(prefix)

INITSMF = $(global_sysconfdir)/init\.d/cswmysql-$(BASE_VERSION)

PACKAGES  = CSWmysql5 CSWmysql5bench CSWmysql5client CSWmysql5devel
PACKAGES += CSWmysql5rt CSWmysql5test

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch

SPKG_DESC_CSWmysql5       = Multithreaded SQL database
SPKG_DESC_CSWmysql5bench  = MySQL 5 benchmarking
SPKG_DESC_CSWmysql5client = MySQL 5 client binaries
SPKG_DESC_CSWmysql5devel  = MySQL 5 header files
SPKG_DESC_CSWmysql5rt     = MySQL 5 runtime files
SPKG_DESC_CSWmysql5test   = MySQL 5 testing files


CATALOGNAME_CSWmysql5       = $(GARNAME)
CATALOGNAME_CSWmysql5bench  = $(GARNAME)bench
CATALOGNAME_CSWmysql5client = $(GARNAME)client
CATALOGNAME_CSWmysql5devel  = $(GARNAME)devel
CATALOGNAME_CSWmysql5rt     = $(GARNAME)rt
CATALOGNAME_CSWmysql5test   = $(GARNAME)test

INCOMPATIBLE_PKGS_CSWmysql5bench  = CSWmysql4bench
INCOMPATIBLE_PKGS_CSWmysql5client = CSWmysql4client
INCOMPATIBLE_PKGS_CSWmysql5       = CSWmysql4
INCOMPATIBLE_PKGS_CSWmysql5devel  = CSWmysql4devel
INCOMPATIBLE_PKGS_CSWmysql5test   = CSWmysql4test

# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
CSWmysql5client_programs  = myisamlog
CSWmysql5client_programs += myisampack
CSWmysql5client_programs += mysql
CSWmysql5client_programs += mysqlaccess
CSWmysql5client_programs += mysqladmin
CSWmysql5client_programs += mysqlbin
CSWmysql5client_programs += mysqlbinlog
CSWmysql5client_programs += mysqlcheck
CSWmysql5client_programs += mysql_client_test
CSWmysql5client_programs += mysqldump
CSWmysql5client_programs += mysqlhotcopy
CSWmysql5client_programs += mysqlimport
CSWmysql5client_programs += mysqlshow
CSWmysql5client_programs += mysql_zap
CSWmysql5client_programs += perror
CSWmysql5client_programs += replace

# Without this EXTRA_LD_OPTIONS setting, /opt/csw/bin/mysql fails with a shared
# library not found.  EXTRA_LIB was tried too, but did not work, as the -R path
# ended up with having two $ISALIST tokens.
#
# Without this setting it looks for:
# /opt/csw/mysql5/lib/amd64/libmysqlclient.so.15
# The library is at:
# /opt/csw/mysql5/lib/amd64/mysql/libmysqlclient.so.15
EXTRA_LD_OPTIONS  = -R$(libdir)/\$$ISALIST/mysql

CSWmysql5devel_programs += mysql_config

# Enable 64 bits build
BUILD64 = 1

PKGFILES_CSWmysql5bench   = $(prefix)/sql-bench.*
PKGFILES_CSWmysql5client  = $(bindir)
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSWmysql5devel  += $(foreach bin_name,$(CSWmysql5devel_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSWmysql5devel  += $(foreach bin_name,$(CSWmysql5devel_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSWmysql5devel  += $(foreach bin_name,$(CSWmysql5devel_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSWmysql5devel  += $(foreach bin_name,$(CSWmysql5devel_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSWmysql5devel  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSWmysql5devel  += $(prefix)/include.*
PKGFILES_CSWmysql5devel  += /opt/csw/include/mysql

PKGFILES_CSWmysql5rt      = $(prefix)/lib/.*\.so.*
PKGFILES_CSWmysql5test    = $(prefix)/mysql-test.*

REQUIRED_PKGS_CSWmysql5bench       = CSWmysql5
REQUIRED_PKGS_CSWmysql5client      = CSWmysql5rt
REQUIRED_PKGS_CSWmysql5            = CSWmysql5client CSWmysql5rt
REQUIRED_PKGS_CSWmysql5devel       = CSWmysql5
REQUIRED_PKGS_CSWmysql5test        = CSWmysql5 CSWperl

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(GARVERSION).tar.gz
DISTFILES += cswmysql5 quick_start-csw README.CSW ChangeLog
DISTFILES += CSWmysql5.preinstall
DISTFILES += CSWmysql5.postinstall
DISTFILES += cswusergroup

UFILES_REGEX = mysql-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses CSWzlib
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

# MySQL-5.1.40 doesn't compile without setting EXTRA_INC.
EXTRA_INC = /opt/csw/include
EXTRA_LIB = /opt/csw/lib
EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
# CONFIGURE_ARGS += --without-docs
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-extra-charsets=all
CONFIGURE_ARGS += --with-low-memory
CONFIGURE_ARGS += --with-pthread
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-zlib-dir=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-plugins=max-no-ndb
CONFIGURE_ARGS += --with-comment
CONFIGURE_ARGS_DBG = --with-debug
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# TODO: Make the tests pass. They don't at the moment.
TEST_SCRIPTS =
TEST_TARGETS = check


USERGROUP = /etc/opt/csw/pkg/CSWmysql5/cswusergroup

PROTOTYPE_MODIFIERS = dbdir
PROTOTYPE_FILES_dbdir = $(localstatedir)
PROTOTYPE_USER_dbdir = mysql
PROTOTYPE_GROUP_dbdir = mysql
PROTOTYPE_PERMS_dbdir = 0700
PROTOTYPE_CLASS_dbdir = ugfiles

SPKG_CLASSES = none ugfiles

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/mysql/doc
	# ln -sf ../../../mysql5/share/mysql/doc/README.CSW \
	# 	$(PKGROOT)/opt/csw/share/mysql/doc/README.CSW
	ginstall -m 755 -d $(PKGROOT)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswmysql5 $(PKGROOT)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(global_sysconfdir)/pkg/CSWmysql5
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(global_sysconfdir)/pkg/CSWmysql5
	## A symlink for mysql5 include files
	## ginstall -m 755 -d $(PKGROOT)/opt/csw/include
	## ln -s ../mysql5/include/mysql $(PKGROOT)/opt/csw/include/mysql
	# Create symlinks to binaries
	ginstall -m 755 -d $(PKGROOT)$(global_bindir)
	for f in $(PKGROOT)$(bindir)/*; do \
		ln -s mysql/$(BASE_VERSION)/`basename $$f` $(PKGROOT)$(global_bindir)/`basename $$f`; \
	done
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)
