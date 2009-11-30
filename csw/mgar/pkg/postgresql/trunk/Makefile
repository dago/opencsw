# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = postgresql
BASE_VERSION = 8.4
PATCHLEVEL = 1
GARVERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
GARFLAVOR = DBG

DESCRIPTION = An advanced open source database
SPKG_SOURCEURL = http://www.postgresql.org/

define BLURB
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

MIGRATE_FILES = postgresql.conf
MIGRATE_DEST_DIR = $(sysconfdir)

MASTER_SITES = http://wwwmaster.postgresql.org/redir/53/h/source/v$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += cswpostgres.tmpl
DISTFILES += cswusergroup.tmpl
DISTFILES += postgresql.conf.tmpl
DISTFILES += README-CSW.txt

PACKAGES = CSWpostgresql CSWpostgresqldoc CSWpostgresqldevel CSWlibpq

CATALOGNAME_CSWpostgresql      = postgresql
CATALOGNAME_CSWpostgresqldoc   = postgresql_doc
CATALOGNAME_CSWpostgresqldevel = postgresql_devel
CATALOGNAME_CSWlibpq           = libpq

SPKG_DESC_CSWpostgresql = An advanced open source database
SPKG_DESC_CSWpostgresqldoc = PostgreSQL Documentation
SPKG_DESC_CSWpostgresqldevel = PostgreSQL Developer Files
SPKG_DESC_CSWlibpq = PostgreSQL Libraries

REQUIRED_PKGS_CSWpostgresql = CSWreadline CSWzlib CSWlibpq
REQUIRED_PKGS_CSWpostgresqldevel = CSWpostgresql

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

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_PAX_ARGS = -s ",^\./opt/csw/postgresql/share/doc,./opt/csw/share/doc/postgresql,p"

PKGFILES_CSWpostgresqldoc = $(PKGFILES_DOC)
PKGFILES_CSWpostgresqldevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpostgresqldevel += $(prefix)/share/doc/postgresql/html.*
PKGFILES_CSWlibpq  = $(PKGFILES_RT)
PKGFILES_CSWlibpq += $(libdir)/64

# -> TODO: start in rc3.d S10, Stop everywhere else in K90
INITSMF = /etc$(prefix)/init\.d/cswpostgres-$(BASE_VERSION)

# -> TODO: Migrate $(prefix)/var/pgdata to /var$(prefix)/postgresql/pgdata
USERGROUP = /etc$(prefix)/pkg/postgresql-$(BASE_VERSION)

# -> TODO: Migrate $(prefix)/etc/postgresql.conf to /etc$(prefix)/postgresql.conf
PRESERVECONF = $(sysconfdir)/postgresql\.conf

BIN_NAMES  = clusterdb createdb createlang createuser dropdb droplang dropuser
BIN_NAMES += ecpg initdb pg_config pg_controldata pg_ctl pg_dump pg_dumpall
BIN_NAMES += pg_resetxlog pg_restore postgres postmaster psql reindexdb

PGDATA = $(localstatedir)/pgdata

PROTOTYPE_MODIFIERS = pgdata
PROTOTYPE_FILES_pgdata = $(PGDATA)
PROTOTYPE_USER_pgdata = postgres
PROTOTYPE_GROUP_pgdata = postgres
PROTOTYPE_PERMS_pgdata = 0700
PROTOTYPE_CLASS_pgdata = ugfiles

SPKG_CLASSES = none ugfiles

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-merge:
	ginstall -d $(PKGROOT)/etc$(prefix)/init.d
	sed -e 's+@PGDATA@+$(PGDATA)+' \
		-e 's+@sysconfdir@+$(sysconfdir)+' \
		-e 's+@bindir@+$(bindir)+' \
		< $(FILEDIR)/cswpostgres.tmpl \
		> $(WORKDIR)/cswpostgres
	ginstall \
		$(WORKDIR)/cswpostgres \
		$(PKGROOT)/etc$(prefix)/init.d/cswpostgres-$(BASE_VERSION)
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
	for b in $(BIN_NAMES); do \
	  gln -s $(GARNAME)/$(BASE_VERSION)/$${b} $(PKGROOT)$(prefix)/bin/$${b}; \
	done
	ginstall -d $(PKGROOT)$(PGDATA)
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)
