# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# This BUILD is NOT READY!  It needs work before it's usable.

# TODO: Initialize the database cluster during installation if not already
# there.
#
# TODO: Migration plan from 8.3: Installing 8.3 and 8.4 at the same time, and
# migrating
#
# TODO: The isaexec part in GAR doesn't work very well.  Let's write a minimal
# example of it.   (gmake repackage may produce the right output)

NAME = postgresql
BASE_VERSION = 8.4
# How to make one automatically?
VERSION_NODOT = 8_4
BASE_VERSION_G = 84
PATCHLEVEL = 4
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

DESCRIPTION = An advanced open source database
SPKG_SOURCEURL = http://www.postgresql.org/

define BLURB
endef

pgsubdir = $(NAME)$(BASE_VERSION_G)
bindir_install = $(exec_prefix)/bin/$(pgsubdir)
sbindir_install = $(exec_prefix)/sbin/$(pgsubdir)
libdir_install = $(exec_prefix)/lib/$(pgsubdir)
# libdir = $(prefix)$(version_dependent)/lib
# Otherwise initdb can't find the right libraries, see:
# http://archives.postgresql.org/pgsql-general/2010-01/msg00422.php
localstatedir = /var$(prefix)/$(pgsubdir)
sysconfdir = /etc$(prefix)/$(pgsubdir)
datadir = $(prefix)/share/$(pgsubdir)
docdir = $(prefix)/share/doc/$(NAME)-$(BASE_VERSION)
includedir = $(prefix)/include/$(pgsubdir)
infodir = $(datadir)/info
libexecdir_install = $(exec_prefix)/libexec/$(pgsubdir)
lispdir = $(datadir)/emacs/site-lisp
mandir = $(datadir)/man
sharedstatedir = $(prefix)/share/$(pgsubdir)
sourcedir = $(prefix)/src/$(pgsubdir)

MIGRATE_FILES_CSWpostgresql-$(BASE_VERSION_G)    = postgresql.conf
MIGRATE_DEST_DIR_CSWpostgresql-$(BASE_VERSION_G) = $(sysconfdir)

MASTER_SITES = http://wwwmaster.postgresql.org/redir/53/h/source/v$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += cswpostgres.tmpl
DISTFILES += cswusergroup.tmpl
DISTFILES += postgresql.conf.tmpl
DISTFILES += README-CSW.txt
# DISTFILES += CSWpostgresql-$(BASE_VERSION_G).postinstall
include files/CSWpostgresql-$(BASE_VERSION_G).postinstall

PACKAGES += CSWpostgresql
PACKAGES += CSWlibpq-$(BASE_VERSION_G)
PACKAGES += CSWpostgresql-$(BASE_VERSION_G)
PACKAGES += CSWpostgresql-$(BASE_VERSION_G)-dev
PACKAGES += CSWpostgresql-$(BASE_VERSION_G)-doc

CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G)      = postgresql_$(BASE_VERSION_G)
CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G)-doc  = postgresql_$(BASE_VERSION_G)_doc
CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G)-dev  = postgresql_$(BASE_VERSION_G)_devel
CATALOGNAME_CSWlibpq-$(BASE_VERSION_G)           = libpq$(BASE_VERSION_G)
CATALOGNAME_CSWpostgresql                        = postgresql

SPKG_DEST_CSWpostgresql                       = An advanced open source database, a metapackage
SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G)     = An advanced open source database, version $(BASE_VERSION).x
SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G)-doc = PostgreSQL $(BASE_VERSION).x Documentation
SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G)-dev = PostgreSQL $(BASE_VERSION).x Developer Files
SPKG_DESC_CSWlibpq-$(BASE_VERSION_G)          = PostgreSQL $(BASE_VERSION).x Libraries

RUNTIME_DEP_PKGS_CSWpostgresql                        = CSWpostgresql-$(BASE_VERSION_G)
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWlibgnugetopt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWlibpq-$(BASE_VERSION_G)
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWlibxml2
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWlibxslt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWosslrt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWreadline
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)     += CSWzlib
RUNTIME_DEP_PKGS_CSWlibpq-$(BASE_VERSION_G)          += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWlibpq-$(BASE_VERSION_G)          += CSWosslrt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G)-dev  = CSWpostgresql-$(BASE_VERSION_G)

CHECKPKG_OVERRIDES_CSWpostgresql += surplus-dependency|CSWpostgresql-84
CHECKPKG_OVERRIDES_CSWpostgresql-84-dev += surplus-dependency|CSWpostgresql-84

ARCHALL_CSWpostgresql                       = 1
ARCHALL_CSWpostgresql-$(BASE_VERSION_G)-doc = 1
ARCHALL_CSWpostgresql-$(BASE_VERSION_G)-doc = 1

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
# NOISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-includes=/opt/csw/include

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

# CSWpostgresql is a generic wrapper always pointing to the latest release
PKGFILES_CSWpostgresql                        = NOFILES
PKGFILES_CSWpostgresql-$(BASE_VERSION_G)-doc  = $(PKGFILES_DOC)
PKGFILES_CSWpostgresql-$(BASE_VERSION_G)-dev  = $(PKGFILES_DEVEL)

PKGFILES_CSWlibpq-$(BASE_VERSION_G)           = $(call baseisadirs,$(libdir),libpq\.so(\.\d+)*)
PKGFILES_CSWlibpq-$(BASE_VERSION_G)          += $(call baseisadirs,$(libpath_install),libpq\.so(\.\d+)*)
PKGFILES_CSWlibpq-$(BASE_VERSION_G)          += $(libdir)/64

# initscript_base_name = cswpostgres_$(subst .,_,$(BASE_VERSION))
initscript_base_name = cswpostgres_$(VERSION_NODOT)
INITSMF = /etc$(prefix)/init\.d/$(initscript_base_name)
USERGROUP = /etc/opt/csw/pkg/postgresql/cswusergroup_$(VERSION_NODOT)
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
PROTOTYPE_FILES_pgdata = $(PGDATA)
PROTOTYPE_USER_pgdata = postgres
PROTOTYPE_GROUP_pgdata = sys
PROTOTYPE_PERMS_pgdata = 0700
PROTOTYPE_CLASS_pgdata = ugfiles

# This is one of the rare cases where a protoype filter is needed.
# Do not copy this for other Makefiles unless you understand exactly what it does!!
# (explanation: It adds -isaexec to the isaexec-name of the binaries to be isaexec'ed)
PROTOTYPE_FILTER = perl -npe 's,=/opt/csw/bin/isaexec,-isaexec=/opt/csw/bin/isaexec,'

# ISAEXEC_FILES = $(addsuffix -isaexec,$(foreach B,$(BIN_NAMES),$(bindir_install)/$B))
ALTERNATIVES_CSWpostgresql-$(BASE_VERSION_G) = $(NAME)$(BASE_VERSION_G)-32 $(NAME)$(BASE_VERSION_G)-64 $(NAME)$(BASE_VERSION_G)-auto
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT)/$(firstword $(BIN_NAMES)) 100
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT)/$B)
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT64)/$(firstword $(BIN_NAMES)) 200
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT64)/$B)
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(firstword $(BIN_NAMES))-isaexec 300
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$B-isaexec)

# checkpkg does not detect this dependency automatically
CHECKPKG_OVERRIDES_CSWpostgresql-84 += surplus-dependency|CSWalternatives

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
	gsed \
		-e 's+@PGDATA@+$(PGDATA)+g' \
		-e 's+@sysconfdir@+$(sysconfdir)+g' \
		-e 's+@bindir@+$(bindir)+g' \
		< $(FILEDIR)/cswpostgres.tmpl \
		> $(WORKDIR)/$(initscript_base_name)
	ginstall \
		$(WORKDIR)/$(initscript_base_name) \
		$(PKGROOT)/etc$(prefix)/init.d/$(initscript_base_name)
	ginstall -d $(PKGROOT)/etc$(prefix)/pkg/$(NAME)
	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
		< $(FILEDIR)/cswusergroup.tmpl \
		> $(WORKDIR)/cswusergroup
	ginstall $(WORKDIR)/cswusergroup \
		$(PKGROOT)/etc$(prefix)/pkg/$(NAME)/cswusergroup_$(VERSION_NODOT)
	ginstall -d $(PKGROOT)$(sysconfdir)
	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
		< $(FILEDIR)/postgresql.conf.tmpl \
		> $(WORKDIR)/postgresql.conf
	ginstall $(WORKDIR)/postgresql.conf \
		$(PKGROOT)$(sysconfdir)
	ginstall -d $(PKGROOT)$(docdir)
	# ginstall $(WORKDIR)/README-CSW.txt $(PKGROOT)$(docdir)
	ginstall -m 755 -d $(PKGROOT)$(prefix)/bin
	ginstall -d $(PKGROOT)$(PGDATA)
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	for L in $(notdir $(wildcard $(PKGROOT)$(libdir)/libpq.*)); do \
		gln -s $(pgsubdir)/$$L $(PKGROOT)$(libpath_install)/$$L; \
	done
	mkdir -p $(PKGROOT)$(libpath_install)/$(ISA_DEFAULT64)
	for L in $(notdir $(wildcard $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libpq.*)); do \
		gln -s ../$(pgsubdir)/$(ISA_DEFAULT64)/$$L $(PKGROOT)$(libpath_install)/$(ISA_DEFAULT64)/$$L; \
	done
	@$(MAKECOOKIE)
