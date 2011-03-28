# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# The idea is based on the Ubuntu PostgreSQL package.

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
BASE_VERSION = 9.0
# How to make one automatically?
VERSION_NODOT = 9_0
BASE_VERSION_G = 90
PATCHLEVEL = 0
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

SPKG_SOURCEURL = http://www.postgresql.org/

define BLURB
endef

version_dependent = /lib/$(NAME)/$(BASE_VERSION)
bindir_install = $(prefix)$(version_dependent)/bin
bindir = $(prefix)$(version_dependent)/bin
sbindir_install = $(prefix)$(version_dependent)/sbin
sbindir = $(prefix)$(version_dependent)/sbin
# libdir = $(prefix)$(version_dependent)/lib
# Otherwise initdb can't find the right libraries, see:
# http://archives.postgresql.org/pgsql-general/2010-01/msg00422.php
# libdir = $(abspath $(prefix)$(version_dependent)/lib/$(MM_LIBDIR))
# libdir_install = $(prefix)$(version_dependent)/lib
localstatedir = /var$(prefix)/$(NAME)/$(BASE_VERSION)
sysconfdir = /etc$(prefix)/postgresql-common
datadir = $(prefix)/share/$(NAME)/$(BASE_VERSION)
docdir = $(prefix)/share/doc/$(NAME)-doc-$(BASE_VERSION)
includedir = $(prefix)/include/postgresql/
infodir = $(datadir)/info
libexecdir_install = $(prefix)/libexec/$(NAME)/$(BASE_VERSION)
lispdir = $(datadir)/emacs/site-lisp
mandir = $(datadir)/man
sharedstatedir = $(prefix)/share/$(NAME)/$(BASE_VERSION)
sourcedir = $(prefix)/src/$(NAME)/$(BASE_VERSION)

MIGRATE_FILES_CSWpostgresql-$(BASE_VERSION_G)    = postgresql.conf
MIGRATE_DEST_DIR_CSWpostgresql-$(BASE_VERSION_G) = $(sysconfdir)

MASTER_SITES = http://wwwmaster.postgresql.org/redir/53/h/source/v$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += cswpostgres.tmpl
DISTFILES += cswusergroup.tmpl
DISTFILES += postgresql.conf.tmpl
DISTFILES += README-CSW.txt
DISTFILES += CSWpostgresql-$(BASE_VERSION_G).postinstall

PATCHFILES += 0001-postgresql-Removed-two-usr-local-occurrences.patch
PATCHFILES += 0003-postgresql-Removed-usr-local-from-ecpg.c.patch

PACKAGES += CSWpostgresql
CATALOGNAME_CSWpostgresql = postgresql
SPKG_DESC_CSWpostgresql = An advanced open source database

PACKAGES += CSWpostgresql-$(BASE_VERSION_G)-doc
CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G)-doc  = postgresql_$(BASE_VERSION_G)_doc
SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G)-doc = PostgreSQL $(BASE_VERSION).x Documentation

RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWlibgnugetopt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWlibpq5
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWlibxml2
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWlibxslt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWosslrt
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWreadline
RUNTIME_DEP_PKGS_CSWpostgresql-$(BASE_VERSION_G) += CSWzlib

ARCHALL_CSWpostgresql                       = 1
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

PKGFILES_CSWpostgresql                        = NOFILES
PKGFILES_CSWpostgresql-$(BASE_VERSION_G)-doc  = $(PKGFILES_DOC)


# initscript_base_name = cswpostgres_$(subst .,_,$(BASE_VERSION))
initscript_base_name = cswpostgres_$(VERSION_NODOT)
INITSMF = /etc$(prefix)/init\.d/$(initscript_base_name)
USERGROUP = /etc$(prefix)/pkg/postgresql/cswusergroup_$(VERSION_NODOT)
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

EXPANDVARS  = CSWpostgresql-$(BASE_VERSION_G).postinstall
EXPANDVARS += cswpostgres.tmpl
# This is one of the rare cases where a protoype filter is needed.
# Do not copy this for other Makefiles unless you understand exactly what it does!!
# (explanation: It adds -isaexec to the isaexec-name of the binaries to be isaexec'ed)
PROTOTYPE_FILTER = perl -npe 's,=$(bindir)/isaexec,-isaexec=/opt/csw/bin/isaexec,'

ISAEXEC_FILES = $(addsuffix -isaexec,$(foreach B,$(BIN_NAMES),$(bindir_install)/$B))

ALTERNATIVES_CSWpostgresql-$(BASE_VERSION_G) = $(NAME)$(BASE_VERSION_G)-32 $(NAME)$(BASE_VERSION_G)-64 $(NAME)$(BASE_VERSION_G)-auto
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT)/$(firstword $(BIN_NAMES)) 100
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT)/$B)
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT64)/$(firstword $(BIN_NAMES)) 200
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT64)/$B)
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(firstword $(BIN_NAMES))-isaexec 300
ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$B-isaexec)

# checkpkg does not detect this dependency automatically
CHECKPKG_OVERRIDES_CSWpostgresql-$(BASE_VERSION_G) += surplus-dependency|CSWalternatives

PACKAGES += CSWlibpq5
CATALOGNAME_CSWlibpq5 = libpq5
PKGFILES_CSWlibpq5 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibpq5 += PostgreSQL C client library (built from $(BASE_VERSION).x sources), libpq.so.5
RUNTIME_DEP_PKGS_CSWlibpq5 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibpq5 += CSWkrb5lib
OBSOLETED_BY_CSWlibpq5 += CSWlibpq

PACKAGES += CSWlibecpg6
CATALOGNAME_CSWlibecpg6 = libecpg6
PKGFILES_CSWlibecpg6 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibecpg6 += Embedded PostgreSQL for C library (built from $(BASE_VERSION).x sources), libecpg.so.6
RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpgtypes3
RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpq5
OBSOLETED_BY_CSWlibecpg6 += CSWlibpq

PACKAGES += CSWlibecpg-compat3
CATALOGNAME_CSWlibecpg-compat3 = libecpg_compat3
PKGFILES_CSWlibecpg-compat3 += $(call baseisadirs,$(prefix)/lib,libecpg_compat\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibecpg-compat3 += Older version of run-time library for ECPG programs (built from $(BASE_VERSION).x sources), libecpg_compat.so.3
RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibecpg6
RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpgtypes3
RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpq5
OBSOLETED_BY_CSWlibecpg-compat3 = CSWlibpq

PACKAGES += CSWlibpgtypes3
CATALOGNAME_CSWlibpgtypes3 = libpgtypes3
PKGFILES_CSWlibpgtypes3 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.3\.0)
PKGFILES_CSWlibpgtypes3 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibpgtypes3 += Used by programs built with ecpg (Embedded PostgreSQL for C, from $(BASE_VERSION).x sources), libpgtypes.so.3
OBSOLETED_BY_CSWlibpgtypes3 = CSWlibpq

PACKAGES += CSWlibpq-dev
CATALOGNAME_CSWlibpq-dev = libpq_dev
SPKG_DESC_CSWlibpq-dev = PostgreSQL C client headers (built from $(BASE_VERSION).x sources)
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibxslt
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWreadline
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibgnugetopt
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWzlib
PKGFILES_CSWlibpq-dev += $(prefix)/include/postgresql.*
PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libpq.so
PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libecpg.so
PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libecpg_compat.so
PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libpgtypes.so
PKGFILES_CSWlibpq-dev += $(prefix)/bin/.*pg_config.*
PKGFILES_CSWlibpq-dev += $(prefix)/share/postgresql/8.4/man/man1/pg_config.1
PKGFILES_CSWlibpq-dev += $(prefix)/share/locale/*/LC_MESSAGES/pg_config.*\.mo
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibpq5
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibecpg6
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibecpg-compat3
RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibpgtypes3

PACKAGES += CSWpostgresql-$(BASE_VERSION_G)
CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G) = postgresql_$(BASE_VERSION_G)
SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G) = PostgreSQL, version $(BASE_VERSION).x

# Legacy libraries
PACKAGES += CSWlibpq3
CATALOGNAME_CSWlibpq3 = libpq3
PKGFILES_CSWlibpq3 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibpq3 += PostgreSQL C client library, libpq.so.3
RUNTIME_DEP_PKGS_CSWlibpq3 += CSWosslrt
OBSOLETED_BY_CSWlibpq3 = CSWlibpq

PACKAGES += CSWlibpq4
CATALOGNAME_CSWlibpq4 = libpq4
PKGFILES_CSWlibpq4 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibpq4 += PostgreSQL C client library, libpq.so.4
RUNTIME_DEP_PKGS_CSWlibpq4 += CSWosslrt
OBSOLETED_BY_CSWlibpq4 = CSWlibpq

PACKAGES += CSWlibpgtypes1
CATALOGNAME_CSWlibpgtypes1 = libpgtypes1
PKGFILES_CSWlibpgtypes1 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibpgtypes1 += Used by programs built with ecpg (Embedded PostgreSQL for C), libpgtypes.so.1
OBSOLETED_BY_CSWlibpgtypes1 = CSWlibpq

PACKAGES += CSWlibpgtypes2
CATALOGNAME_CSWlibpgtypes2 = libpgtypes2
PKGFILES_CSWlibpgtypes2 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibpgtypes2 += Used by programs built with ecpg (Embedded PostgreSQL for C), libpgtypes.so.2
OBSOLETED_BY_CSWlibpgtypes2 = CSWlibpq

PACKAGES += CSWlibecpg4
CATALOGNAME_CSWlibecpg4 = libecpg4
PKGFILES_CSWlibecpg4 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibecpg4 += Embedded PostgreSQL for C library, libecpg.so.4
RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWlibpgtypes1
RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWlibpq3
OBSOLETED_BY_CSWlibecpg4 += CSWlibpq

PACKAGES += CSWlibecpg5
CATALOGNAME_CSWlibecpg5 = libecpg5
PKGFILES_CSWlibecpg5 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibecpg5 += Embedded PostgreSQL for C library, libecpg.so.5
RUNTIME_DEP_PKGS_CSWlibecpg5 += CSWlibpgtypes2
RUNTIME_DEP_PKGS_CSWlibecpg5 += CSWlibpq5
OBSOLETED_BY_CSWlibecpg5 += CSWlibpq

PACKAGES += CSWlibecpg-compat2
CATALOGNAME_CSWlibecpg-compat2 = libecpg_compat2
PKGFILES_CSWlibecpg-compat2 += $(call baseisadirs,$(prefix)/lib,libecpg_compat\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibecpg-compat2 += Older version of run-time library for ECPG programs, libecpg_compat.so.2
RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibpgtypes2
RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibecpg5
RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibpq5
OBSOLETED_BY_CSWlibecpg-compat2 = CSWlibpq


# This occurrence is okay.
#    # On HPUX platforms, gcc is usually configured to search for libraries
#    # in /usr/local/lib, but ld won't do so.  Add an explicit -L switch so
#    # ld can find the same libraries gcc does.  Make sure it goes after any
#    # -L switches provided explicitly.
#    ifeq ($(GCC), yes)
#      SHLIB_LINK  += -L/usr/local/lib
#    endif
#
CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/postgresql/pgxs/src/Makefile.shlib
CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/postgresql/pgxs/src/Makefile.shlib
CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/postgresql/pgxs/src/Makefile.shlib
CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/postgresql/pgxs/src/Makefile.global
CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/postgresql/pgxs/src/Makefile.shlib

# CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/postgresql/9.0/bin/ecpg
# CHECKPKG_OVERRIDES_CSWpostgresql-90 += file-with-bad-content|/usr/local|root/opt/csw/lib/postgresql/9.0/bin/sparcv9/ecpg

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-build-modulated:
	$(BUILD_ENV) gmake -C $(WORKSRC)/contrib all
	@$(MAKECOOKIE)

post-install-modulated:
	$(INSTALL_ENV) gmake -C $(WORKSRC)/contrib DESTDIR=$(DESTDIR) install
	ginstall -d -m 755 $(DESTDIR)$(prefix)/bin
	[ -r $(DESTDIR)$(bindir)/pg_config ] && \
	gmv -v $(DESTDIR)$(bindir)/pg_config $(DESTDIR)$(prefix)/bin || true
	ginstall -d $(DESTDIR)/etc$(prefix)/init.d
	ginstall \
		$(WORKDIR)/cswpostgres.tmpl \
		$(DESTDIR)/etc$(prefix)/init.d/$(initscript_base_name)
	ginstall -d $(DESTDIR)/etc$(prefix)/pkg/$(NAME)
	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
		< $(FILEDIR)/cswusergroup.tmpl \
		> $(WORKDIR)/cswusergroup
	ginstall $(WORKDIR)/cswusergroup \
		$(DESTDIR)/etc$(prefix)/pkg/$(NAME)/cswusergroup_$(VERSION_NODOT)
	ginstall -d $(DESTDIR)$(sysconfdir)
	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
		< $(FILEDIR)/postgresql.conf.tmpl \
		> $(WORKDIR)/postgresql.conf
	ginstall $(WORKDIR)/postgresql.conf \
		$(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(docdir)
	# ginstall $(WORKDIR)/README-CSW.txt $(DESTDIR)$(docdir)
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(prefix)/bin
	ginstall -d $(PKGROOT)$(PGDATA)
	$(FILEDIR)/merge_legacy_libs.sh $(GARCH) $(FILEDIR) $(PKGROOT)/$(prefix)/lib
	# Checks whether the pkgroot contents is OK.
	$(FILEDIR)/check_pkgroot.sh "$(PKGROOT)"
	@$(MAKECOOKIE)
