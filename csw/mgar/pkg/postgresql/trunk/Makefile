# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = postgresql
BASE_VERSION = 8.4
PATCHLEVEL = 1
GARVERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
GARFLAVOR ?= DBG

DESCRIPTION = An advanced open source database
SPKG_SOURCEURL = http://www.postgresql.org/

define BLURB
endef

version_dependent = /lib/$(GARNAME)/$(BASE_VERSION)
bindir_install = $(prefix)$(version_dependent)/bin
sbindir_install = $(prefix)$(version_dependent)/sbin
libdir_install = $(prefix)$(version_dependent)/lib
localstatedir = /var$(prefix)/$(GARNAME)/$(BASE_VERSION)
sysconfdir = /etc$(prefix)/$(GARNAME)/$(BASE_VERSION)
datadir = $(prefix)/share/$(GARNAME)/$(BASE_VERSION)
docdir = $(prefix)/share/doc/$(GARNAME)-$(BASE_VERSION)
includedir = $(prefix)/include/$(GARNAME)/$(BASE_VERSION)
infodir = $(datadir)/info
libexecdir_install = $(prefix)/libexec/$(GARNAME)/$(BASE_VERSION)
lispdir = $(datadir)/emacs/site-lisp
mandir = $(datadir)/man
sharedstatedir = $(prefix)/share/$(GARNAME)/$(BASE_VERSION)
sourcedir = $(prefix)/src/$(GARNAME)/$(BASE_VERSION)

MIGRATE_FILES_CSWpostgresql-8.4    = postgresql.conf
MIGRATE_DEST_DIR_CSWpostgresql-8.4 = $(sysconfdir)

MASTER_SITES = http://wwwmaster.postgresql.org/redir/53/h/source/v$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += cswpostgres.tmpl
DISTFILES += cswusergroup.tmpl
DISTFILES += postgresql.conf.tmpl
DISTFILES += README-CSW.txt

PACKAGES  = CSWpostgresql-84 CSWpostgresql-84-doc CSWpostgresql-84-dev CSWlibpq-84
PACKAGES += CSWpostgresql

CATALOGNAME_CSWpostgresql-84      = postgresql_84
CATALOGNAME_CSWpostgresql-84-doc  = postgresql_84_doc
CATALOGNAME_CSWpostgresql-84-dev  = postgresql_84_devel
CATALOGNAME_CSWlibpq-84           = libpq84
CATALOGNAME_CSWpostgresql         = postgresql

SPKG_DEST_CSWpostgresql        = An advanced open source database, a metapackage
SPKG_DESC_CSWpostgresql-84     = An advanced open source database, version 8.4.x
SPKG_DESC_CSWpostgresql-84-doc = PostgreSQL Documentation
SPKG_DESC_CSWpostgresql-84-dev = PostgreSQL Developer Files
SPKG_DESC_CSWlibpq-84          = PostgreSQL Libraries

REQUIRED_PKGS_CSWpostgresql        = CSWpostgresql-84
REQUIRED_PKGS_CSWpostgresql-84     = CSWreadline CSWzlib CSWlibpq-84
REQUIRED_PKGS_CSWpostgresql-84    += CSWlibxml2 CSWlibxslt CSWosslrt CSWkrb5lib
REQUIRED_PKGS_CSWpostgresql-84-dev = CSWpostgresql-84
REQUIRED_PKGS_CSWlibpq-84          = CSWkrb5lib CSWlibxml2 CSWlibxslt CSWosslrt
REQUIRED_PKGS_CSWlibpq-84         += CSWzlib

ARCHALL_CSWpostgresql        = 1
ARCHALL_CSWpostgresql-84-doc = 1
ARCHALL_CSWpostgresql-84-doc = 1

LICENSE = COPYRIGHT

EXTRA_INC = $(BUILD_PREFIX)/include
EXTRA_LIB = $(BUILD_PREFIX)/lib

EXTRA_LD_OPTIONS  = -R$(prefix)/lib/\$$ISALIST

BUILD64 = 1

# There was a discussion about whether to use ISAEXEC by default.  The argument
# is that enabling 64-bit by default where possible (using isaexec) is a waste.
# I'm not completely convinced.  Leaving this line commented out for future
# consideration.
#
# References:
# - http://lists.opencsw.org/pipermail/maintainers/2009-November/004903.html
#
# I'd like to get some hard data though.  What is the difference in the memory
# footprint, and what is the difference in execution speed between 32 and
# 64-bit versions?
#
# NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-includes=/opt/csw/include
CONFIGURE_ARGS += --with-library=$(abspath /opt/csw/lib/$(MM_LIBDIR))

# # Perl support only in the 32-bit version
# CONFIGURE_ARGS_isa-sparcv8 += --with-perl
# CONFIGURE_ARGS_isa-i386 += --with-perl

# # Python support in 32-bit only
# CONFIGURE_ARGS_isa-sparcv8 += --with-python
# CONFIGURE_ARGS_isa-i386 += --with-python

CONFIGURE_ARGS += --with-gssapi
# CONFIGURE_ARGS += --with-krb5
CONFIGURE_ARGS += --with-pam
# CONFIGURE_ARGS += --with-bonjour
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-libxml
CONFIGURE_ARGS += --with-libxslt
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))

# Skipping tests to save time during packaging, and to enable x86 builds.
SKIPTEST ?= 1
TEST_TARGET = check

PKGFILES_CSWpostgresql        = $(prefix)/bin/.*
PKGFILES_CSWpostgresql-84-doc = $(PKGFILES_DOC)
PKGFILES_CSWpostgresql-84-doc += $(prefix)/share/doc/postgresql/html.*
PKGFILES_CSWpostgresql-84-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibpq-84  = $(PKGFILES_RT)
PKGFILES_CSWlibpq-84 += $(libdir)/64

INITSMF = /etc$(prefix)/init\.d/cswpostgres_$(BASE_VERSION)
USERGROUP = /etc$(prefix)/pkg/postgresql-$(BASE_VERSION)
PRESERVECONF = $(sysconfdir)/postgresql\.conf

BIN_NAMES  = clusterdb
BIN_NAMES += createdb
BIN_NAMES += createlang
BIN_NAMES += createuser
BIN_NAMES += dropdb
BIN_NAMES += droplang
BIN_NAMES += dropuser
BIN_NAMES += ecpg
BIN_NAMES += initdb
BIN_NAMES += oid2name
BIN_NAMES += pg_config
BIN_NAMES += pg_controldata
BIN_NAMES += pg_ctl
BIN_NAMES += pg_dump
BIN_NAMES += pg_dumpall
BIN_NAMES += pg_resetxlog
BIN_NAMES += pg_restore
BIN_NAMES += pg_standby
BIN_NAMES += pgbench
BIN_NAMES += postgres
BIN_NAMES += postmaster
BIN_NAMES += psql
BIN_NAMES += reindexdb
BIN_NAMES += vacuumdb
BIN_NAMES += vacuumlo

PGDATA = $(localstatedir)/pgdata

PROTOTYPE_MODIFIERS = pgdata
PROTOTYPE_FILES_pgdata = $(localstatedir) $(PGDATA)
PROTOTYPE_USER_pgdata = postgres
PROTOTYPE_GROUP_pgdata = postgres
PROTOTYPE_PERMS_pgdata = 0700
PROTOTYPE_CLASS_pgdata = ugfiles

SPKG_CLASSES = none ugfiles

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-build-modulated:
	$(BUILD_ENV) gmake -C $(WORKSRC)/contrib all
	@$(MAKECOOKIE)

post-install-modulated:
	$(INSTALL_ENV) gmake -C $(WORKSRC)/contrib DESTDIR=$(DESTDIR) install
	@$(MAKECOOKIE)

post-merge:
	ginstall -d $(PKGROOT)/etc$(prefix)/init.d
	sed -e 's+@PGDATA@+$(PGDATA)+' \
		-e 's+@sysconfdir@+$(sysconfdir)+' \
		-e 's+@bindir@+$(bindir)+' \
		< $(FILEDIR)/cswpostgres.tmpl \
		> $(WORKDIR)/cswpostgres_$(BASE_VERSION)
	ginstall \
		$(WORKDIR)/cswpostgres_$(BASE_VERSION) \
		$(PKGROOT)/etc$(prefix)/init.d/cswpostgres_$(BASE_VERSION)
	ginstall -d $(PKGROOT)/etc$(prefix)/pkg/$(GARNAME)
	sed -e 's+@PGDATA@+$(PGDATA)+' \
		< $(FILEDIR)/cswusergroup.tmpl \
		> $(WORKDIR)/cswusergroup
	ginstall $(WORKDIR)/cswusergroup \
		$(PKGROOT)/etc$(prefix)/pkg/$(GARNAME)/cswusergroup-$(BASE_VERSION)
	ginstall -d $(PKGROOT)$(sysconfdir)
	sed -e 's+@PGDATA@+$(PGDATA)+' \
		< $(FILEDIR)/postgresql.conf.tmpl \
		> $(WORKDIR)/postgresql.conf
	ginstall $(WORKDIR)/postgresql.conf \
		$(PKGROOT)$(sysconfdir)
	ginstall -d $(PKGROOT)$(docdir)
	ginstall $(WORKDIR)/README-CSW.txt $(PKGROOT)$(docdir)
	ginstall -m 755 -d $(PKGROOT)$(prefix)/bin
	for b in $(BIN_NAMES); do \
	  gln -s ..$(version_dependent)/bin/$${b} $(PKGROOT)$(prefix)/bin/$${b}; \
	done
	ginstall -d $(PKGROOT)$(PGDATA)
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)
