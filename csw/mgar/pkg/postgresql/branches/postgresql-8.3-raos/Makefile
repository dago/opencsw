# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Note 1
# ------
#
# A word of caution: PostgreSQL does use autoconf, but it does *not* use
# automake. That said, it `misses' many features found in pure
# autoconf/automake builds, e.g. --program-suffix is not available. This also
# explains some quirks of this recipe.
#
#
# Note 2
# ------
#
# The idea is to make it possible to install different major/minor versions of
# PostgreSQL at the same time but without installing them to distinct --prefix
# directories, which in turn makes linking against PostgreSQL easier. This has
# been achieved as follows:
#
#  * libraries go into $(libdir)
#
#  * binaries go into $(libexec)/postgres/XY/ and alternatives are used to
#    bring the binaries into $(prefix)/bin
#
# Generally, putting libraries in $(libdir) should not pose a problem, but in
# the case of PostgresSQL, there is also a directory $(libdir)/postgres which
# is unversioned and cannot be changed by passing arguments to configure. This
# shortcoming can be lifted by adjusting $(pkglibdir) in
# $(WORKSRC)/src/Makefile.global.in which is what we do.


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
BASE_VERSION = 8.3
VERSION_NODOT = $(subst .,_,$(BASE_VERSION))
BASE_VERSION_G = $(subst .,,$(BASE_VERSION))
PATCHLEVEL = 16
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

VENDOR_URL = http://www.postgresql.org/

define BLURB
endef

MIGRATE_FILES_CSWpostgresql-$(BASE_VERSION_G)    = postgresql.conf
MIGRATE_DEST_DIR_CSWpostgresql-$(BASE_VERSION_G) = $(sysconfdir)

MASTER_SITES = http://ftp.postgresql.org/pub/source/v$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += cswpostgres.tmpl
DISTFILES += cswusergroup.tmpl
DISTFILES += postgresql.conf.tmpl
DISTFILES += README-CSW.txt
DISTFILES += CSWpostgresql-$(BASE_VERSION_G).postinstall

# ARCHALL_CSWpostgresql                       = 1
# ARCHALL_CSWpostgresql-$(BASE_VERSION_G)-doc = 1

LICENSE = COPYRIGHT

BUILD_DEP_PKGS  = CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWgsed # gsed is used in this recipe
BUILD_DEP_PKGS += CSWlibz-dev

# Why's that? --raos
#
# EXTRA_INC = $(BUILD_PREFIX)/include
# EXTRA_LIB = $(BUILD_PREFIX)/lib

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
ISAEXEC = 0

#
# Postgres specific variables
#
PGBINDIR		= $(libexecdir)/$(NAME)/$(BASE_VERSION_G)
PGSBINDIR       	= $(libexecdir)/$(NAME)/$(BASE_VERSION_G)
PGDATADIR		= $(datadir)/$(NAME)/$(BASE_VERSION_G)
PGDOCDIR		= $(datadir)/doc/$(NAME)/$(BASE_VERSION_G)
PGLOCALSTATEDIR_BASE	= $(localstatedir)/$(NAME)
PGDATA          	= $(PGLOCALSTATEDIR_BASE)/$(BASE_VERSION_G)

USERGROUPDIR		= $(sysconfdir)/pkg/$(NAME)


CONFIGURE_ARGS  = $(DIRPATHS)

# This is one of the quirks mentioned at the beginning: --program-suffix is not
# supported, so IMHO, binaries should go to --libexecdir
CONFIGURE_ARGS += --bindir=$(PGBINDIR)
CONFIGURE_ARGS += --sbindir=$(PGSBINDIR)

CONFIGURE_ARGS += --datadir=$(PGDATADIR)
CONFIGURE_ARGS += --localstatedir=$(PGDATA)
CONFIGURE_ARGS += --with-includes=/opt/csw/include
CONFIGURE_ARGS += --with-libraries=$(abspath /opt/csw/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-docdir=$(PGDOCDIR)
# configure complains that we are not thread-safe, wtf? --raos
#CONFIGURE_ARGS += --enable-thread-safety

CONFIGURE_ARGS += --with-gssapi
# CONFIGURE_ARGS += --with-krb5
CONFIGURE_ARGS += --with-pam
# CONFIGURE_ARGS += --with-bonjour
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-libxml
CONFIGURE_ARGS += --with-libxslt
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))

# Skipping tests to save time during packaging, and to enable x86 builds.
#
# IMHO, tests are essential, especially on Solaris, and I do not experience
# build troubles on x86 having them enabled --raos
SKIPTEST ?= 1
TEST_TARGET = check

# PKGFILES_CSWpostgresql                        = NOFILES
# PKGFILES_CSWpostgresql-$(BASE_VERSION_G)-doc  = $(PKGFILES_DOC)


# initscript_base_name = cswpostgres_$(subst .,_,$(BASE_VERSION))
#initscript_base_name = cswpostgres_$(VERSION_NODOT)
#INITSMF = /etc$(prefix)/init\.d/$(initscript_base_name)

USERGROUP = $(USERGROUPDIR)/cswusergroup-$(BASE_VERSION)

#PRESERVECONF = $(sysconfdir)/postgresql\.conf

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
#
# Since we are not using isaexec, this line is not needed, right? --raos
#PROTOTYPE_FILTER = perl -npe 's,=/opt/csw/bin/isaexec,-isaexec=/opt/csw/bin/isaexec,'

# Here come the alternatives we use to let the user choose between 32/64bit
# variants of the binaries
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

# Bad voodoo coming up...
ALTERNATIVES = $(BUILD_ISAS)
$(foreach alt,$(ALTERNATIVES), $(eval ALTERNATIVE_$(alt) = $(subst /$(DEFAULT_ISA)/,/,$(foreach n,$(BIN_NAMES),$(bindir)/$(n)-$(BASE_VERSION_G) $(NAME)-$(BASE_VERSION_G) $(libexecdir)/$(alt)/$(NAME)/$(BASE_VERSION_G)/$(n) 20))))


# ISAEXEC_FILES = $(addsuffix -isaexec,$(foreach B,$(BIN_NAMES),$(bindir_install)/$B))
# ALTERNATIVES_CSWpostgresql-$(BASE_VERSION_G) = $(NAME)$(BASE_VERSION_G)-32 $(NAME)$(BASE_VERSION_G)-64 $(NAME)$(BASE_VERSION_G)-auto
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT)/$(firstword $(BIN_NAMES)) 100
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-32 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT)/$B)
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(ISA_DEFAULT64)/$(firstword $(BIN_NAMES)) 200
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-64 += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$(ISA_DEFAULT64)/$B)
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto = $(bindir_install)/$(firstword $(BIN_NAMES)) $(firstword $(BIN_NAMES)) $(bindir_install)/$(firstword $(BIN_NAMES))-isaexec 300
# ALTERNATIVE_$(NAME)$(BASE_VERSION_G)-auto += $(foreach B,$(wordlist 2,$(words $(BIN_NAMES)),$(BIN_NAMES)),$(bindir_install)/$B $B $(bindir_install)/$B-isaexec)

# # checkpkg does not detect this dependency automatically
# CHECKPKG_OVERRIDES_CSWpostgresql-$(BASE_VERSION_G) += surplus-dependency|CSWalternatives

# PACKAGES += CSWlibpq5
# CATALOGNAME_CSWlibpq5 = libpq5
# PKGFILES_CSWlibpq5 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.5(\.\d+)*)
# SPKG_DESC_CSWlibpq5 += PostgreSQL C client library (built from $(BASE_VERSION).x sources), libpq.so.5
# RUNTIME_DEP_PKGS_CSWlibpq5 += CSWlibgssapi-krb5-2
# RUNTIME_DEP_PKGS_CSWlibpq5 += CSWosslrt

# PACKAGES += CSWlibecpg6
# CATALOGNAME_CSWlibecpg6 = libecpg6
# PKGFILES_CSWlibecpg6 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.6(\.\d+)*)
# SPKG_DESC_CSWlibecpg6 += Embedded PostgreSQL for C library (built from $(BASE_VERSION).x sources), libecpg.so.6
# RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpgtypes3
# RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpq5

# PACKAGES += CSWlibecpg-compat3
# CATALOGNAME_CSWlibecpg-compat3 = libecpg_compat3
# PKGFILES_CSWlibecpg-compat3 += $(call baseisadirs,$(prefix)/lib,libecpg_compat\.so\.3(\.\d+)*)
# SPKG_DESC_CSWlibecpg-compat3 += Older version of run-time library for ECPG programs (built from $(BASE_VERSION).x sources), libecpg_compat.so.3
# RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibecpg6
# RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpgtypes3
# RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpq5

# PACKAGES += CSWlibpgtypes3
# CATALOGNAME_CSWlibpgtypes3 = libpgtypes3
# PKGFILES_CSWlibpgtypes3 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.3\.0)
# PKGFILES_CSWlibpgtypes3 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.3(\.\d+)*)
# SPKG_DESC_CSWlibpgtypes3 += Used by programs built with ecpg (Embedded PostgreSQL for C, from $(BASE_VERSION).x sources), libpgtypes.so.3

# PACKAGES += CSWlibpq-dev
# CATALOGNAME_CSWlibpq-dev = libpq_dev
# SPKG_DESC_CSWlibpq-dev = PostgreSQL C client headers (built from $(BASE_VERSION).x sources)
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibgnugetopt0
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibgssapi-krb5-2
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibreadline6
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibxml2-2
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibxslt1
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibz1
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWosslrt
# PKGFILES_CSWlibpq-dev += $(prefix)/include/postgresql.*
# PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libpq.so
# PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libecpg.so
# PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libecpg_compat.so
# PKGFILES_CSWlibpq-dev += $(prefix)/lib/.*libpgtypes.so
# PKGFILES_CSWlibpq-dev += $(prefix)/bin/.*pg_config.*
# PKGFILES_CSWlibpq-dev += $(prefix)/share/postgresql/8.4/man/man1/pg_config.1
# PKGFILES_CSWlibpq-dev += $(prefix)/share/locale/*/LC_MESSAGES/pg_config.*\.mo
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibpq5
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibecpg6
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibecpg-compat3
# RUNTIME_DEP_PKGS_CSWlibpq-dev += CSWlibpgtypes3

# PACKAGES += CSWpostgresql-$(BASE_VERSION_G)
# CATALOGNAME_CSWpostgresql-$(BASE_VERSION_G) = postgresql_$(BASE_VERSION_G)
# SPKG_DESC_CSWpostgresql-$(BASE_VERSION_G) = PostgreSQL, version $(BASE_VERSION).x

# # Private shared libraries have sonames, which triggers this error.
# CHECKPKG_OVERRIDES_CSWpostgresql-$(BASE_VERSION_G) += soname-not-part-of-filename

# # Legacy libraries
# PACKAGES += CSWlibpq3
# CATALOGNAME_CSWlibpq3 = libpq3
# PKGFILES_CSWlibpq3 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.3(\.\d+)*)
# SPKG_DESC_CSWlibpq3 += PostgreSQL C client library, libpq.so.3
# RUNTIME_DEP_PKGS_CSWlibpq3 += CSWosslrt

# PACKAGES += CSWlibpq4
# CATALOGNAME_CSWlibpq4 = libpq4
# PKGFILES_CSWlibpq4 += $(call baseisadirs,$(prefix)/lib,libpq\.so\.4(\.\d+)*)
# SPKG_DESC_CSWlibpq4 += PostgreSQL C client library, libpq.so.4
# RUNTIME_DEP_PKGS_CSWlibpq4 += CSWosslrt

# PACKAGES += CSWlibpgtypes1
# CATALOGNAME_CSWlibpgtypes1 = libpgtypes1
# PKGFILES_CSWlibpgtypes1 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.1(\.\d+)*)
# SPKG_DESC_CSWlibpgtypes1 += Used by programs built with ecpg (Embedded PostgreSQL for C), libpgtypes.so.1

# PACKAGES += CSWlibpgtypes2
# CATALOGNAME_CSWlibpgtypes2 = libpgtypes2
# PKGFILES_CSWlibpgtypes2 += $(call baseisadirs,$(prefix)/lib,libpgtypes\.so\.2(\.\d+)*)
# SPKG_DESC_CSWlibpgtypes2 += Used by programs built with ecpg (Embedded PostgreSQL for C), libpgtypes.so.2

# PACKAGES += CSWlibecpg4
# CATALOGNAME_CSWlibecpg4 = libecpg4
# PKGFILES_CSWlibecpg4 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.4(\.\d+)*)
# SPKG_DESC_CSWlibecpg4 += Embedded PostgreSQL for C library, libecpg.so.4
# RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWlibpgtypes1
# RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWosslrt
# RUNTIME_DEP_PKGS_CSWlibecpg4 += CSWlibpq3

# PACKAGES += CSWlibecpg5
# CATALOGNAME_CSWlibecpg5 = libecpg5
# PKGFILES_CSWlibecpg5 += $(call baseisadirs,$(prefix)/lib,libecpg\.so\.5(\.\d+)*)
# SPKG_DESC_CSWlibecpg5 += Embedded PostgreSQL for C library, libecpg.so.5
# RUNTIME_DEP_PKGS_CSWlibecpg5 += CSWlibpgtypes2
# RUNTIME_DEP_PKGS_CSWlibecpg5 += CSWlibpq5

# PACKAGES += CSWlibecpg-compat2
# CATALOGNAME_CSWlibecpg-compat2 = libecpg_compat2
# PKGFILES_CSWlibecpg-compat2 += $(call baseisadirs,$(prefix)/lib,libecpg_compat\.so\.2(\.\d+)*)
# SPKG_DESC_CSWlibecpg-compat2 += Older version of run-time library for ECPG programs, libecpg_compat.so.2
# RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibpgtypes2
# RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibecpg5
# RUNTIME_DEP_PKGS_CSWlibecpg-compat2 += CSWlibpq5

# # The horrible transitional package
# PACKAGES += CSWlibpq
# PKGFILES_CSWlibpq += $(prefix)/postgresql.*
# SPKG_DESC_CSWlibpq = Transitional package for PostgreSQL shared libraries
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibecpg-compat2
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibecpg-compat3
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibecpg4
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibecpg5
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibecpg6
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpgtypes1
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpgtypes2
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpgtypes3
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpq3
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpq4
# RUNTIME_DEP_PKGS_CSWlibpq += CSWlibpq5

include gar/category.mk

# what's that good for? --raos
#
#CFLAGS := $(filter-out -I%,$(CFLAGS))

# We adjust the $(pkglibdir) found in $(WORKSRC)/src/Makefile.global.in, so
# that it should be possible to install 8.x and 8.y concurrently
pre-configure-modulated:
	if [ -r $(WORKSRC)/src/Makefile.global.in ] ; then \
		gsed -i -r -e 's|^(pkglibdir[[:space:]]*=[[:space:]]*)\$$\(libdir\).*$$|\1$$(libdir)/postgresql/$(BASE_VERSION_G)|' $(WORKSRC)/src/Makefile.global.in ; \
	fi
	@$(MAKECOOKIE)

post-build-modulated:
	$(BUILD_ENV) gmake -C $(WORKSRC)/contrib all
	@$(MAKECOOKIE)

post-install-modulated:
	$(INSTALL_ENV) gmake -C $(WORKSRC)/contrib DESTDIR=$(DESTDIR) install
	ginstall -d -m 755 $(DESTDIR)$(prefix)/bin
	[ -r $(DESTDIR)$(bindir)/pg_config ] && \
	gmv -v $(DESTDIR)$(bindir)/pg_config $(DESTDIR)$(prefix)/bin || true
	@$(MAKECOOKIE)

post-merge:
# Create the PGDATA directory
	ginstall -d $(PKGROOT)$(PGDATA)
# Create the directory for the user group file
	ginstall -d $(PKGROOT)$(USERGROUPDIR)
# PGLOCALSTATEDIR_BASE has been chosen, because this should be stable, i.e
# unversioned, across different PostgreSQL installation
	gsed -e 's+@PGLOCALSTATEDIR_BASE@+$(PGLOCALSTATEDIR_BASE)+g' $(FILEDIR)/cswusergroup.tmpl > $(PKGROOT)$(USERGROUP)
# 	ginstall -d $(PKGROOT)/etc$(prefix)/init.d
# 	ginstall \
# 		$(WORKDIR)/cswpostgres.tmpl \
# 		$(PKGROOT)/etc$(prefix)/init.d/$(initscript_base_name)
# 	ginstall -d $(PKGROOT)/etc$(prefix)/pkg/$(NAME)
# 	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
# 		< $(FILEDIR)/cswusergroup.tmpl \
# 		> $(WORKDIR)/cswusergroup
# 	ginstall $(WORKDIR)/cswusergroup \
# 		$(PKGROOT)/etc$(prefix)/pkg/$(NAME)/cswusergroup_$(VERSION_NODOT)
# 	ginstall -d $(PKGROOT)$(sysconfdir)
# 	gsed -e 's+@PGDATA@+$(PGDATA)+g' \
# 		< $(FILEDIR)/postgresql.conf.tmpl \
# 		> $(WORKDIR)/postgresql.conf
# 	ginstall $(WORKDIR)/postgresql.conf \
# 		$(PKGROOT)$(sysconfdir)
# 	ginstall -d $(PKGROOT)$(docdir)
# 	# ginstall $(WORKDIR)/README-CSW.txt $(PKGROOT)$(docdir)
# 	ginstall -m 755 -d $(PKGROOT)$(prefix)/bin
# 	# for b in $(BIN_NAMES); do \
# 	#   gln -s ..$(version_dependent)/bin/$${b} $(PKGROOT)$(prefix)/bin/$${b}; \
# 	# done
# 	ginstall -d $(PKGROOT)$(PGDATA)
# 	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
# 	mkdir -p $(PKGROOT)$(prefix)/lib
# 	mkdir -p $(PKGROOT)$(prefix)/lib/$(ISA_DEFAULT64)
# 	for libname in libpq libecpg libecpg_compat libpgtypes; do \
# 		mv $(PKGROOT)$(libdir)/$${libname}.so $(PKGROOT)$(prefix)/lib; \
# 		mv $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/$${libname}.so $(PKGROOT)$(prefix)/lib/$(ISA_DEFAULT64); \
# 		mv $(PKGROOT)$(libdir)/$${libname}.so.* $(PKGROOT)$(prefix)/lib; \
# 		mv $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/$${libname}.so.* $(PKGROOT)$(prefix)/lib/$(ISA_DEFAULT64); \
# 	done
# 	$(FILEDIR)/merge_legacy_libs.sh $(GARCH) $(FILEDIR) $(PKGROOT)/$(prefix)/lib

# 	# Backward compatibility provided by CSWlibpq
# 	mkdir -p $(PKGROOT)$(prefix)/postgresql/lib
# 	mkdir -p $(PKGROOT)$(prefix)/postgresql/lib/$(ISA_DEFAULT64)
# 	gln -s . $(PKGROOT)$(prefix)/postgresql/lib/$(ISA_DEFAULT)
# 	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(prefix)/postgresql/lib/64
# 	gln -s $(ISA_DEFAULT) $(PKGROOT)$(prefix)/postgresql/lib/32
# 	for f in $(PKGROOT)$(prefix)/lib/*.so.*; do \
# 		ln -s \
# 			../../lib/`basename $${f}` \
# 			$(PKGROOT)$(prefix)/postgresql/lib; \
# 	done
# 	for f in $(PKGROOT)$(prefix)/lib/$(ISA_DEFAULT64)/lib*.so.*; do \
# 		ln -s \
# 			../../lib/$(ISA_DEFAULT64)/`basename $${f}` \
# 			$(PKGROOT)$(prefix)/postgresql/lib/$(ISA_DEFAULT64); \
# 	done
# 	@$(MAKECOOKIE)
