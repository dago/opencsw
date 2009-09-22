# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = mysql5
GARVERSION = 5.0.84
CATEGORIES = server

DISTNAME = mysql-$(GARVERSION)

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

# Change prefix to /opt/csw/mysql5
prefix = /opt/csw/mysql5
sysconfdir = /etc/opt/csw/mysql5
localstatedir = /var/opt/csw/mysql5
global_sysconfdir = /etc/opt/csw
global_bindir = /opt/csw/bin

INITSMF = $(global_sysconfdir)/init\.d/cswmysql5

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch

PACKAGES  = CSWmysql5 CSWmysql5bench CSWmysql5client CSWmysql5devel
PACKAGES += CSWmysql5rt CSWmysql5test

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
INCOMPATIBLE_PKGS_CSWmysql5rt     = CSWmysql4rt
INCOMPATIBLE_PKGS_CSWmysql5test   = CSWmysql4test

SPKG_DESC_CSWmysql5       = Multithreaded SQL database
SPKG_DESC_CSWmysql5bench  = MySQL 5 benchmarking
SPKG_DESC_CSWmysql5client = MySQL 5 client binaries
SPKG_DESC_CSWmysql5devel  = MySQL 5 header files
SPKG_DESC_CSWmysql5rt     = MySQL 5 runtime files
SPKG_DESC_CSWmysql5test   = MySQL 5 testing files

support64 = (/(amd64|i386))?

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


PKGFILES_CSWmysql5bench   = $(prefix)/sql-bench.*
PKGFILES_CSWmysql5client  = $(bindir)
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),$(bindir)$(support64)/$(bin_name))
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSWmysql5client += $(foreach bin_name,$(CSWmysql5client_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSWmysql5devel  += $(bindir)$(support64)/mysql_config
PKGFILES_CSWmysql5devel  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSWmysql5devel   = $(prefix)/include.*
PKGFILES_CSWmysql5rt      = $(prefix)/lib/.*\.so.*
PKGFILES_CSWmysql5test    = $(prefix)/mysql-test.*

REQUIRED_PKGS_CSWmysql5bench       = CSWmysql5
REQUIRED_PKGS_CSWmysql5client      = CSWmysql5rt
REQUIRED_PKGS_CSWmysql5            = CSWmysql5client CSWmysql5rt
REQUIRED_PKGS_CSWmysql5devel       = CSWmysql5
REQUIRED_PKGS_CSWmysql5test        = CSWmysql5

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-5.0/
DISTFILES  = mysql-$(GARVERSION).tar.gz
DISTFILES += cswmysql5 quick_start-csw README.CSW
DISTFILES += CSWmysql5.preinstall

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses CSWzlib
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

# because we alter the prefix.  this gets us proper linking as well as
# LD_OPTIONS (RPATH)
EXTRA_LIB = /opt/csw/lib
EXTRA_INC = /opt/csw/include
EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
CONFIGURE_ARGS += --without-docs
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-extra-charsets=all
CONFIGURE_ARGS += --with-low-memory
CONFIGURE_ARGS += --with-pthread
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-zlib-dir=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-plugins=max-no-ndb

TEST_SCRIPTS =

# Enable 64 bits build
BUILD64 = 1

USERGROUP = /opt/csw/etc/pkg/CSWmysql5/cswusergroup
PROTOTYPE_FILTER = awk ' \
    $$$$3 ~ /\/var\/opt\/csw\/mysql5$$$$/ { $$$$2 = "ugfiles"; \
                                            $$$$4 = "0700"; \
                                            $$$$5 = "mysql"; \
                                            $$$$6 = "mysql" } \
    { print }'
SPKG_CLASSES = none ugfiles

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)
	ginstall -m 755 -d $(DESTDIR)$(datadir)/mysql5/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(datadir)/mysql5/doc
	ginstall -m 755 -d $(DESTDIR)/opt/csw/share/mysql5/doc
	ln -sf ../../../mysql5/share/mysql5/doc/README.CSW \
		$(DESTDIR)/opt/csw/share/mysql5/doc/README.CSW
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswmysql5 $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(DESTDIR)$(datadir)/mysql5
	ginstall -m 755 -d $(DESTDIR)$(global_sysconfdir)/pkg/CSWmysql5
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(DESTDIR)$(global_sysconfdir)/pkg/CSWmysql5

	# Create symlinks
	ginstall -m 755 -d $(DESTDIR)$(global_bindir)
	for f in $(DESTDIR)$(bindir)/*; do \
		ln -s ../mysql5/bin/`basename $$f` $(DESTDIR)$(global_bindir)/`basename $$f`; \
	done
	@$(MAKECOOKIE)
