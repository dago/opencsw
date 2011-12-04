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
#
#
# Note 3: Alternatives
# ------
#
# I was unable to get the alternatives system to work with using
#
#  ALTERNATIVES_CSWpostgresql83-server = server_amd64 server_pentium_pro
#
# and then defining those alternatives. /opt/csw/sbin/alternatives choked on
# the one file generated for server containing two distinct alternatives. So I
# cooked my own soup:
#
#  1. Create for server, client, contrib, devel separate files containing the
#     alternatives for the ISAs
#
#  2. Adjust the prototype to add include the class 'cswalternatives' for the
#     files in question.
#
# The problem appeared to be having two lines in the same file. So my approach
# is to generate one file per line of alternatives.
#
#
# Note 4:  New upstream releases
# ------
#
# 1. Adjust BASE_VERSION and/or PATCHLEVEL.
#
# 2. Make sure the SONAME patch for
#    $(WORKDIR)/postgresql-x.y.z/src/Makefile.shlib still works
#
# 3. Comment out 'post-install-modulated:'. So we can identify changes in the
#    server/client environment.
#
# 4. `mgar package`
#
# 5. If step 4 succeeded, check the prototype of
#    CSW$(NAME)$(BASE_VERSION_NODOT) for files that have slipped by and put
#    them in the proper place.
#
# 6. Uncomment 'post-install-modulated:'. This will shed light on changes in
#    the contrib environment.
#
# 7. `mgar spotless package`
#
# 8. If step 6 succeeded, check the prototype of
#    CSW$(NAME)$(BASE_VERSION_NODOT) for files that have slipped by and put
#    them in the proper place.
#
# 9. Make sure the proper version numbers are used for the library packages.


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
BASE_VERSION_NODOT = $(subst .,,$(BASE_VERSION))
PATCHLEVEL = 16
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

VENDOR_URL = http://www.postgresql.org/

define BLURB
endef

# Here we will fetch various variables that are used in this recipe. I decided
# to place those in a separate file for the sake of uncluttering this recipe.
#
# Many of the varibles defined in pgconf.mk depend on the various $(VERSION*)
# variables.
include pgconf.mk

MASTER_SITES = http://ftp.postgresql.org/pub/source/v$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += README-CSW.txt
DISTFILES += CSWpostgresql-server.postinstall.tmpl
DISTFILES += $(INITSCRIPTFILETMPL)
DISTFILES += $(USERGROUPFILETMPL)
DISTFILES += $(CSWPGSQLCONFFILETMPL)

# This patch will make the SONAME of the libraries to contain the major and
# minor version. This is important when having multiple installations of
# PostgreSQL where the library versions differ only in the minor part, such as
# with PostgreSQL 8.3 and PostgreSQL 8.4.
#
PATCHFILES += 0000-SONAME-including-major-and-minor-version.patch

INITSMF = $(sysconfdir)/init\.d/$(INITSCRIPTFILE_VERSIONED)
USERGROUP = $(USERGROUPDIR)/$(USERGROUPFILE_VERSIONED)
PRESERVECONF = $(sysconfdir)/$(CSWPGSQLCONFFILE_VERSIONED)

LICENSE = COPYRIGHT

PROTOTYPE_MODIFIERS = pgdata alternatives
PROTOTYPE_FILES_pgdata = $(PGLOCALSTATEDIR_BASE).*
PROTOTYPE_USER_pgdata = postgres
PROTOTYPE_GROUP_pgdata = sys
PROTOTYPE_PERMS_pgdata = 0700
PROTOTYPE_CLASS_pgdata = ugfiles

PROTOTYPE_FILES_alternatives = .*/alternatives/$(NAME)$(BASE_VERSION_NODOT).*
PROTOTYPE_CLASS_alternatives = cswalternatives

# This is the catchall package. It should not contain any files from
# $(PKGROOT). After building all the packages, I check the prototype of this
# package to make sure there are no files slipped by.
PACKAGES = CSW$(NAME)$(BASE_VERSION_NODOT)
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT) = PostgreSQL $(VERSION), Meta Package
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)  = CSW$(NAME)$(BASE_VERSION_NODOT)-server
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT) += CSW$(NAME)$(BASE_VERSION_NODOT)-client
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT) += CSW$(NAME)$(BASE_VERSION_NODOT)-contrib
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT) += CSW$(NAME)$(BASE_VERSION_NODOT)-devel

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-server
CATALOGNAME_CSW$(NAME)$(BASE_VERSION_NODOT)-server = $(NAME)$(BASE_VERSION_NODOT)_server
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-server = PostgreSQL $(VERSION), Server
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server  = $(foreach n,$(BIN_NAMES_SERVER),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += $(foreach n,$(BIN_NAMES_SERVER),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += $(foreach n,$(SO_NAMES_SERVER),.*/$(NAME)/$(BASE_VERSION_NODOT)/*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += $(MISC_NAMES_SERVER)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*/$(NAME)/$(BASE_VERSION_NODOT)/timezone(sets|)/.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*/$(NAME)/$(BASE_VERSION_NODOT)/tsearch_.*/.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += $(PGLOCALSTATEDIR_BASE).*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*$(USERGROUP)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*$(sysconfdir)/init\.d/.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*$(sysconfdir)/$(CSWPGSQLCONFFILE_VERSIONED).CSW
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_server.*
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server  = CSWlibiconv2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibncurses5
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibreadline6
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibxml2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibxslt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWalternatives
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibpq5-1
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-server = $(foreach i,$(BUILD_ISAS), server_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-client
CATALOGNAME_CSW$(NAME)$(BASE_VERSION_NODOT)-client = $(NAME)$(BASE_VERSION_NODOT)_client
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-client = PostgreSQL $(VERSION), Client
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client = $(foreach n,$(BIN_NAMES_CLIENT),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += $(foreach n,$(BIN_NAMES_CLIENT),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += $(MISC_NAMES_CLIENT)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_client.*
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client  = CSWlibiconv2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibncurses5
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibreadline6
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibxml2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibxslt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibpq5-1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWalternatives
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-client = $(foreach i,$(BUILD_ISAS), client_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-contrib
CATALOGNAME_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(NAME)$(BASE_VERSION_NODOT)_contrib
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = PostgreSQL $(VERSION), Contrib
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(foreach n,$(BIN_NAMES_CONTRIB),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += $(foreach n,$(BIN_NAMES_CONTRIB),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += $(foreach n,$(SO_NAMES_CONTRIB),.*/$(NAME)/$(BASE_VERSION_NODOT)/*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*/$(NAME)/$(BASE_VERSION_NODOT)/contrib.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_contrib.*
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib  = CSWlibiconv2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibxml2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibxslt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibpq5-1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWalternatives
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(foreach i,$(BUILD_ISAS), contrib_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-devel
CATALOGNAME_CSW$(NAME)$(BASE_VERSION_NODOT)-devel = $(NAME)$(BASE_VERSION_NODOT)_devel
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-devel = PostgreSQL $(VERSION), Development Files
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel  = .*/pgxs/.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += $(PKGFILES_DEVEL)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += $(foreach n,$(BIN_NAMES_DEVEL),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += $(foreach n,$(BIN_NAMES_DEVEL),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += .*/man5/.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_devel.*
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-devel += CSWalternatives
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-devel = $(foreach i,$(BUILD_ISAS), devel_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-doc
ARCHALL_CSW$(NAME)$(BASE_VERSION_NODOT)-doc = 1
CATALOGNAME_CSW$(NAME)$(BASE_VERSION_NODOT)-doc = $(NAME)$(BASE_VERSION_NODOT)_doc
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-doc = PostgreSQL $(VERSION), Documentation Files
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-doc  =  .*/doc/$(NAME)/$(BASE_VERSION_NODOT)/.*

PACKAGES += CSWlibecpg_compat3-0
CATALOGNAME_CSWlibecpg_compat3-0 = libecpg_compat3_0
SPKG_DESC_CSWlibecpg_compat3-0 = PostgreSQL $(VERSION), libecpg_compat
PKGFILES_CSWlibecpg_compat3-0  = $(call pkgfiles_lib,libecpg_compat.so.3)
RUNTIME_DEP_PKGS_CSWlibecpg_compat3-0  = CSWlibecpg6-0
RUNTIME_DEP_PKGS_CSWlibecpg_compat3-0 += CSWlibpgtypes3-0
RUNTIME_DEP_PKGS_CSWlibecpg_compat3-0 += CSWlibpq5-1

PACKAGES += CSWlibecpg6-0
CATALOGNAME_CSWlibecpg6-0 = libecpg6_0
SPKG_DESC_CSWlibecpg6-0 = PostgreSQL $(VERSION), libecpg
PKGFILES_CSWlibecpg6-0  = $(call pkgfiles_lib,libecpg.so.6)
RUNTIME_DEP_PKGS_CSWlibecpg6-0 += CSWlibpgtypes3-0
RUNTIME_DEP_PKGS_CSWlibecpg6-0 += CSWlibpq5-1

PACKAGES += CSWlibpgtypes3-0
CATALOGNAME_CSWlibpgtypes3-0 = libpgtypes3_0
SPKG_DESC_CSWlibpgtypes3-0 = PostgreSQL $(VERSION), libpgtypes
PKGFILES_CSWlibpgtypes3-0  = $(call pkgfiles_lib,libpgtypes.so.3)

PACKAGES += CSWlibpq5-1
CATALOGNAME_CSWlibpq5-1 = libpq5_1
SPKG_DESC_CSWlibpq5-1 = PostgreSQL $(VERSION), libpq
PKGFILES_CSWlibpq5-1  = $(call pkgfiles_lib,libpq.so.5)
RUNTIME_DEP_PKGS_CSWlibpq5-1  = CSWosslrt

BUILD_DEP_PKGS  = CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWgsed # gsed is used in this recipe
BUILD_DEP_PKGS += CSWlibz-dev

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
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-libxml
CONFIGURE_ARGS += --with-libxslt
CONFIGURE_ARGS += --without-krb5
CONFIGURE_ARGS += --without-bonjour
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))

# Skipping tests to save time during packaging, and to enable x86 builds.
#
# IMHO, tests are essential, especially on Solaris, and I do not experience
# build troubles on x86 having them enabled --raos
SKIPTEST ?= 1
TEST_TARGET = check

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
# This variable will be increased in the course of the following foreach loops
alt_priority = 20
# This will generate the ALTERNATIVEs for the binaries in $(libexecdir)/postgresql/XY.
# I consider this bad voodoo.
## Server
$(foreach alt,$(BUILD_ISAS), $(eval alt_priority=$(shell expr $(alt_priority) + 10)) $(eval ALTERNATIVE_server_$(alt) = $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(firstword $(BIN_NAMES_SERVER)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-server $(libexecdir)/$(subst server_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n))) $(alt_priority)) $(eval ALTERNATIVE_server_$(alt) += $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(wordlist 2,$(words $(BIN_NAMES_SERVER)),$(BIN_NAMES_SERVER)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT) $(libexecdir)/$(subst server_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n)))) )
## Client
# reset priority
alt_priority = 20
$(foreach alt,$(BUILD_ISAS), $(eval alt_priority=$(shell expr $(alt_priority) + 10)) $(eval ALTERNATIVE_client_$(alt) = $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(firstword $(BIN_NAMES_CLIENT)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-client $(libexecdir)/$(subst client_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n))) $(alt_priority)) $(eval ALTERNATIVE_client_$(alt) += $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(wordlist 2,$(words $(BIN_NAMES_CLIENT)),$(BIN_NAMES_CLIENT)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT) $(libexecdir)/$(subst client_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n)))) )
## Contrib
# reset priority
alt_priority = 20
$(foreach alt,$(BUILD_ISAS), $(eval alt_priority=$(shell expr $(alt_priority) + 10)) $(eval ALTERNATIVE_contrib_$(alt) = $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(firstword $(BIN_NAMES_CONTRIB)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-contrib $(libexecdir)/$(subst contrib_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n))) $(alt_priority)) $(eval ALTERNATIVE_contrib_$(alt) += $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(wordlist 2,$(words $(BIN_NAMES_CONTRIB)),$(BIN_NAMES_CONTRIB)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT) $(libexecdir)/$(subst contrib_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n)))) )
## Devel
# reset priority
alt_priority = 20
$(foreach alt,$(BUILD_ISAS), $(eval alt_priority=$(shell expr $(alt_priority) + 10)) $(eval ALTERNATIVE_devel_$(alt) = $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(firstword $(BIN_NAMES_DEVEL)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-devel $(libexecdir)/$(subst devel_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n))) $(alt_priority)) $(eval ALTERNATIVE_devel_$(alt) += $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(wordlist 2,$(words $(BIN_NAMES_DEVEL)),$(BIN_NAMES_DEVEL)),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT) $(libexecdir)/$(subst devel_,,$(alt))/$(NAME)/$(BASE_VERSION_NODOT)/$(n)))) )

# We adjust the $(pkglibdir) found in $(WORKSRC)/src/Makefile.global.in, so
# that it should be possible to install 8.x and 8.y concurrently
pre-configure-modulated:
	if [ -r $(WORKSRC)/src/Makefile.global.in ] ; then \
		gsed -i -r -e 's|^(pkglibdir[[:space:]]*=[[:space:]]*)\$$\(libdir\).*$$|\1$$(libdir)/postgresql/$(BASE_VERSION_NODOT)|' $(WORKSRC)/src/Makefile.global.in ; \
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
# Create my alternatives files
	$(foreach a,$(myALTERNATIVES), $(foreach i,$(BUILD_ISAS), $(shell ginstall -d $(PKGROOT)$(sharedstatedir)/alternatives ; echo "$(ALTERNATIVE_$(a)_$(i))" > $(PKGROOT)$(sharedstatedir)/alternatives/$(NAME)$(BASE_VERSION_NODOT)_$(a)_$(i))))
# Create the PGDATA directory
	ginstall -d $(PKGROOT)$(PGDATA)
# The usergroup file
	ginstall -d $(PKGROOT)$(USERGROUPDIR)
	$(mySED) $(FILEDIR)/$(USERGROUPFILETMPL) > $(PKGROOT)$(USERGROUPDIR)/$(USERGROUPFILE_VERSIONED)
# The init script
	ginstall -d $(PKGROOT)$(sysconfdir)/init.d
	$(mySED) $(FILEDIR)/$(INITSCRIPTFILETMPL) > $(PKGROOT)$(sysconfdir)/init.d/$(INITSCRIPTFILE_VERSIONED)
	chmod 0755 $(PKGROOT)$(sysconfdir)/init.d/$(INITSCRIPTFILE_VERSIONED)
# The init script config
	$(mySED) $(FILEDIR)/$(CSWPGSQLCONFFILETMPL) > $(PKGROOT)$(sysconfdir)/$(CSWPGSQLCONFFILE_VERSIONED).CSW
# Adjust the man page names for man1
	for f in $(PKGROOT)$(datadir)/man/man1/* ; do \
		f_no_suffix="`echo $$f | sed -e 's/.1$$//'`" ; \
		mv $$f $${f_no_suffix}-$(BASE_VERSION_NODOT).1 ; \
	done
	@$(MAKECOOKIE)

pre-package:
	$(mySED) $(FILEDIR)/CSWpostgresql-server.postinstall.tmpl > $(WORKDIR)/CSW$(NAME)$(BASE_VERSION_NODOT)-server.postinstall
