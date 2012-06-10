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
# I was unable to get the alternatives system to work with using, for
# instance,
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
# 2. Comment out 'post-install-modulated:'. So we can identify changes in the
#    server/client environment.
#
# 3. `mgar package`
#
# 4. If step 3 succeeded, check the prototype of
#    CSW$(NAME)$(BASE_VERSION_NODOT) for files that have slipped by and put
#    them in the proper place.
#
# 5. Uncomment 'post-install-modulated:'. This will shed light on changes in
#    the contrib environment.
#
# 6. `mgar spotless package`
#
# 7. If step 6 succeeded, check the prototype of
#    CSW$(NAME)$(BASE_VERSION_NODOT) for files that have slipped by and put
#    them in the proper place.
#
#
# Note 5: Development package
# ------
#
# The development package is not versioned, i.e. named CSW$(NAME)-dev,
# since we can only support one set of header files with a reasonable
# amount of effort.
#
# Further, it does not use alternatives and puts binaries in $(bindir)
# (see 'post-merge-modulated:'). This will make it easier for
# maintainers to use `pg_config'.

NAME = postgresql
BASE_VERSION = 8.3
VERSION_NODOT = $(subst .,_,$(BASE_VERSION))
BASE_VERSION_NODOT = $(subst .,,$(BASE_VERSION))
PATCHLEVEL = 19
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

VENDOR_URL = http://www.postgresql.org/

define BLURB
	PostgreSQL is a powerful, open source object-relational database system.
	It has more than 15 years of active development and a proven architecture
	that has earned it a strong reputation for reliability, data integrity,
	and correctness.
endef

#
# These variables control many aspects of the build
#
sysconfdir-suffix-64	= /64
sysconfdir		= /etc/opt/csw$(sysconfdir-suffix-$(MEMORYMODEL))
PGSYSCONFDIR		= $(sysconfdir)/$(NAME)/$(BASE_VERSION_NODOT)
PGBINDIR		= $(libexecdir)/$(NAME)/$(BASE_VERSION_NODOT)
PGSBINDIR		= $(libexecdir)/$(NAME)/$(BASE_VERSION_NODOT)
PGDATADIR		= $(datadir)/$(NAME)/$(BASE_VERSION_NODOT)
PGDOCDIR		= $(datadir)/doc/$(NAME)/$(BASE_VERSION_NODOT)
PGLOCALSTATEDIR_BASE	= $(localstatedir)/$(NAME)
PGDATA			= $(PGLOCALSTATEDIR_BASE)/$(BASE_VERSION_NODOT)
# This variable has been introduced for using in EXPANDVARS files
PGNAMEVERSIONED		= $(NAME)$(BASE_VERSION_NODOT)
# This variable has been introduced for using in EXPANDVARS files
PGNAME_VERSIONED	= $(NAME)-$(BASE_VERSION_NODOT)
# Those BIN_NAMES_* are used both, for package creation and alternatives
BIN_NAMES_SERVER	= initdb ipcclean pg_controldata pg_ctl pg_resetxlog postmaster postgres
BIN_NAMES_DEVEL		= ecpg pg_config
BIN_NAMES_CLIENT	= clusterdb createdb createlang createuser dropdb droplang dropuser pg_dump pg_dumpall pg_restore psql reindexdb vacuumdb
BIN_NAMES_CONTRIB	= oid2name pgbench pg_standby vacuumlo
# These are shared objects used by the server. Please note, contrib installs
# also shared object in the same place, so make sure you don't mix up things
SO_NAMES_SERVER		 = ascii_and_mic.so cyrillic_and_mic.so dict_snowball.so euc_cn_and_mic.so
SO_NAMES_SERVER 	+= euc_jis_2004_and_shift_jis_2004.so euc_jp_and_sjis.so euc_kr_and_mic.so
SO_NAMES_SERVER		+= euc_tw_and_big5.so latin2_and_win1250.so latin_and_mic.so plpgsql.so
SO_NAMES_SERVER		+= utf8_and_ascii.so utf8_and_big5.so utf8_and_cyrillic.so utf8_and_euc_cn.so
SO_NAMES_SERVER		+= utf8_and_euc_jis_2004.so utf8_and_euc_jp.so utf8_and_euc_kr.so utf8_and_euc_tw.so
SO_NAMES_SERVER		+= utf8_and_gb18030.so utf8_and_gbk.so utf8_and_iso8859.so utf8_and_iso8859_1.so
SO_NAMES_SERVER		+= utf8_and_johab.so utf8_and_shift_jis_2004.so utf8_and_sjis.so utf8_and_uhc.so utf8_and_win.so
# These are shared object used by contrib. Please note, the server installs
# also shared object in the same place, so make sure you don't mix up things
SO_NAMES_CONTRIB 	 = _int.so adminpack.so autoinc.so btree_gist.so chkpass.so
SO_NAMES_CONTRIB	+= cube.so dblink.so dict_int.so dict_xsyn.so earthdistance.so
SO_NAMES_CONTRIB	+= fuzzystrmatch.so hstore.so insert_username.so int_aggregate.so
SO_NAMES_CONTRIB	+= isn.so lo.so ltree.so moddatetime.so pageinspect.so pg_buffercache.so
SO_NAMES_CONTRIB	+= pg_freespacemap.so pg_trgm.so pgcrypto.so pgrowlocks.so pgstattuple.so
SO_NAMES_CONTRIB	+= pgxml.so refint.so seg.so sslinfo.so tablefunc.so test_parser.so timetravel.so tsearch2.so
# Miscellaneous files
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/conversion_create.sql
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/information_schema.sql
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/pg_hba.conf.sample
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/pg_ident.conf.sample
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/pg_service.conf.sample
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/postgres.bki
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/postgres.description
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/postgres.shdescription
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/postgresql.conf.sample
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/recovery.conf.sample
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/snowball_create.sql
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/sql_features.txt
MISC_NAMES_SERVER	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/system_views.sql
MISC_NAMES_CLIENT	+= .*/share/$(NAME)/$(BASE_VERSION_NODOT)/psqlrc.sample

# Used for the PostgreSQL user. Please note, although the file does not feature
# a version number here, it will be installed with $(BASE_VERSION_NODOT)
# appended.
USERGROUPDIR		= $(sysconfdir)/pkg/$(NAME)
USERGROUPFILE		= cswusergroup
USERGROUPFILETMPL	= $(USERGROUPFILE).tmpl
USERGROUPFILE_VERSIONED = $(USERGROUPFILE)-$(BASE_VERSION_NODOT)

# The configuration file for the init.d script. Please note, although the file
# does not feature a version number here, it will be installed with
# $(BASE_VERSION_NODOT) inserted.
CSWPGSQLCONFFILE	= postgresql.conf
CSWPGSQLCONFFILETMPL    = $(CSWPGSQLCONFFILE).tmpl
CSWPGSQLCONFFILE_VERSIONED = $(subst $(suffix $(CSWPGSQLCONFFILE)),,$(CSWPGSQLCONFFILE))-$(BASE_VERSION_NODOT).conf

# The initscript. Please note, although the file does not feature a version
# number here, it will be installed with $(BASE_VERSION_NODOT) appended
INITSCRIPTFILE		= cswpostgresql
INITSCRIPTFILETMPL	= $(INITSCRIPTFILE).tmpl
INITSCRIPTFILE_VERSIONED = $(INITSCRIPTFILE)-$(BASE_VERSION_NODOT)

# The postinstall script for the postgreSQL server
SERVERPOSTINSTTMPL  = CSWpostgresql-server.postinstall.tmpl
SERVERPOSTINST_VERSIONED = CSW$(NAME)$(BASE_VERSION_NODOT)-server.postinstall


# These are the alternatives provided for the packages.  I use them in the
# recipe to iterate over all possible alternatives (see 'post-merge:')
#
# Please note that these should correspond to the package suffixes.
myALTERNATIVES = server client contrib

POSTMSG = $(foreach n,$(myALTERNATIVES),\
	$(docdir)/$(NAME)$(BASE_VERSION_NODOT)_$(n)/CSW$(NAME)$(BASE_VERSION_NODOT)-$(n).postmsg\
)

MASTER_SITES = http://ftp.postgresql.org/pub/source/v$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += README.CSW
DISTFILES += changelog.CSW
DISTFILES += $(SERVERPOSTINSTTMPL)
DISTFILES += $(INITSCRIPTFILETMPL)
DISTFILES += $(USERGROUPFILETMPL)
DISTFILES += $(CSWPGSQLCONFFILETMPL)
DISTFILES += $(notdir $(POSTMSG))
NOCHECKSUM = $(notdir $(POSTMSG))

EXPANDVARS  = $(CSWPGSQLCONFFILETMPL)
EXPANDVARS += $(INITSCRIPTFILETMPL)
EXPANDVARS += $(CSWPGSQLCONFFILETMPL)
EXPANDVARS += $(SERVERPOSTINSTTMPL)
EXPANDVARS += $(USERGROUPFILETMPL)
EXPANDVARS += README.CSW

# This patch will replace /usr/local/include by /opt/csw/include in
# ecpg.c and thus silence a checkpkg error.
PATCHFILES += 0001-ecpg-usr-local-include-replacement.patch
# Test running on a NFS may fail. Thus we let the test run in
# /var/tmp/pgsql/tmp_check
PATCHFILES += 0002-Run-tests-in-var-tmp-pgsql-tmp_check.patch
# By default, src/makefiles/Makefile.solaris uses -Wl,-R'$(rpathdir)'
# which isn't properly digested by Sun's ld
PATCHFILES += 0000-Use-plain-rpath.patch

INITSMF = $(sysconfdir)/init\.d/$(INITSCRIPTFILE_VERSIONED)
USERGROUP = $(USERGROUPDIR)/$(USERGROUPFILE_VERSIONED)
PRESERVECONF = $(sysconfdir)/$(CSWPGSQLCONFFILE_VERSIONED)

LICENSE = COPYRIGHT

# The alternatives modifier should stay in place, until I figured out
# how to properly employ the ALTERNATIVES system in this build.
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
ARCHALL_CSW$(NAME)$(BASE_VERSION_NODOT) = 1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)  = CSW$(NAME)$(BASE_VERSION_NODOT)-server
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT) += CSW$(NAME)$(BASE_VERSION_NODOT)-client
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT) += CSW$(NAME)$(BASE_VERSION_NODOT)-contrib
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT) += surplus-dependency|CSW$(NAME)$(BASE_VERSION_NODOT)-client
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT) += surplus-dependency|CSW$(NAME)$(BASE_VERSION_NODOT)-server
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT) += surplus-dependency|CSW$(NAME)$(BASE_VERSION_NODOT)-contrib

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-server
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
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*/CSW$(NAME)$(BASE_VERSION_NODOT)-server.postmsg
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += .*$(docdir)/$(NAME)$(BASE_VERSION_NODOT)_server/README.CSW
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibreadline6
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibpq5
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibxslt1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-server += CSWlibgssapi-krb5-2
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT)-server = $(foreach n,$(SO_NAMES_SERVER), soname-not-part-of-filename|soname=lib$(n).0|filename=$(n) )
# This one isn't covered by the above.
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT)-server += soname-not-part-of-filename|soname=libplpgsql.so.1|filename=plpgsql.so
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-server = $(foreach i,$(NEEDED_ISAS), server_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-client
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-client = PostgreSQL $(VERSION), Client
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client = $(foreach n,$(BIN_NAMES_CLIENT),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += $(foreach n,$(BIN_NAMES_CLIENT),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += $(MISC_NAMES_CLIENT)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_client.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += .*/CSW$(NAME)$(BASE_VERSION_NODOT)-client.postmsg
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-client += .*$(docdir)/$(NAME)$(BASE_VERSION_NODOT)_client/README.CSW
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibreadline6
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibpq5
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibxslt1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-client += CSWlibgssapi-krb5-2
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-client = $(foreach i,$(NEEDED_ISAS), client_$(i))

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-contrib
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = PostgreSQL $(VERSION), Contrib
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(foreach n,$(BIN_NAMES_CONTRIB),.*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += $(foreach n,$(BIN_NAMES_CONTRIB),.*/man1/$(n)-$(BASE_VERSION_NODOT)\.1$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += $(foreach n,$(SO_NAMES_CONTRIB),.*/$(NAME)/$(BASE_VERSION_NODOT)/*$(n)$$)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*/$(NAME)/$(BASE_VERSION_NODOT)/contrib.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*/alternatives/$(NAME)$(BASE_VERSION_NODOT)_contrib.*
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*/CSW$(NAME)$(BASE_VERSION_NODOT)-contrib.postmsg
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += .*$(docdir)/$(NAME)$(BASE_VERSION_NODOT)_contrib/README.CSW
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibpq5
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibxslt1
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib += CSWlibreadline6
# This will produce some 'unused overrides'.
CHECKPKG_OVERRIDES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(foreach n,$(SO_NAMES_CONTRIB), soname-not-part-of-filename|soname=lib$(n).0|filename=$(n) )
#ALTERNATIVES_CSW$(NAME)$(BASE_VERSION_NODOT)-contrib = $(foreach i,$(NEEDED_ISAS), contrib_$(i))

PACKAGES += CSW$(NAME)-dev
SPKG_DESC_CSW$(NAME)-dev = PostgreSQL $(VERSION), Development Files
PKGFILES_CSW$(NAME)-dev  = .*/pgxs/.*
PKGFILES_CSW$(NAME)-dev += $(PKGFILES_DEVEL)
PKGFILES_CSW$(NAME)-dev += $(foreach n,$(BIN_NAMES_DEVEL),.*$(n)$$)
PKGFILES_CSW$(NAME)-dev += $(foreach n,$(BIN_NAMES_DEVEL),.*/man1/$(n)\.1$$)
PKGFILES_CSW$(NAME)-dev += .*/CSW$(NAME)-dev.postmsg
PKGFILES_CSW$(NAME)-dev += .*$(docdir)/$(NAME)_dev/README.CSW
# See `post-merge-modulated:'
PKGFILES_CSW$(NAME)-dev += .*/libpgport\.a$
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibecpg-compat3
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibecpg6
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibpq5
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibpgtypes3
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibxslt1
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibreadline6
RUNTIME_DEP_PKGS_CSW$(NAME)-dev += CSWlibssl0-9-8
# Those '/usr/local' are ok, they are in a HPUX section of the file
CHECKPKG_OVERRIDES_CSW$(NAME)-dev += $(foreach i,$(NEEDED_ISAS), $(subst $(ISA_DEFAULT)/,,file-with-bad-content|/usr/local|root$(libdir)/$(i)/$(NAME)/$(BASE_VERSION_NODOT)/pgxs/src/Makefile.shlib) )
# That's ok too, it's docbook stuff which we don't use in this build
CHECKPKG_OVERRIDES_CSW$(NAME)-dev += $(foreach i,$(NEEDED_ISAS), $(subst $(ISA_DEFAULT)/,,file-with-bad-content|/usr/share|root$(libdir)/$(i)/$(NAME)/$(BASE_VERSION_NODOT)/pgxs/src/Makefile.global) )
# See `post-merge-modulated:' for those overrides
CHECKPKG_OVERRIDES_CSWpostgresql-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libpgport.a
CHECKPKG_OVERRIDES_CSWpostgresql-dev += discouraged-path-in-pkgmap|/opt/csw/lib/$(ISA_DEFAULT64)/libpgport.a

PACKAGES += CSW$(NAME)$(BASE_VERSION_NODOT)-doc
ARCHALL_CSW$(NAME)$(BASE_VERSION_NODOT)-doc = 1
SPKG_DESC_CSW$(NAME)$(BASE_VERSION_NODOT)-doc = PostgreSQL $(VERSION), Documentation Files
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-doc  = .*/doc/$(NAME)/$(BASE_VERSION_NODOT)/.*\.(html|css)
PKGFILES_CSW$(NAME)$(BASE_VERSION_NODOT)-doc += .*/man5/.*

PACKAGES += CSWlibecpg-compat3
SPKG_DESC_CSWlibecpg-compat3 = PostgreSQL $(VERSION), libecpg_compat
PKGFILES_CSWlibecpg-compat3  = $(call pkgfiles_lib,libecpg_compat.so.3)
RUNTIME_DEP_PKGS_CSWlibecpg-compat3  = CSWlibecpg6
RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpgtypes3
RUNTIME_DEP_PKGS_CSWlibecpg-compat3 += CSWlibpq5

PACKAGES += CSWlibecpg6
SPKG_DESC_CSWlibecpg6 = PostgreSQL $(VERSION), libecpg
PKGFILES_CSWlibecpg6  = $(call pkgfiles_lib,libecpg.so.6)
RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpgtypes3
RUNTIME_DEP_PKGS_CSWlibecpg6 += CSWlibpq5

PACKAGES += CSWlibpgtypes3
SPKG_DESC_CSWlibpgtypes3 = PostgreSQL $(VERSION), libpgtypes
PKGFILES_CSWlibpgtypes3  = $(call pkgfiles_lib,libpgtypes.so.3)

PACKAGES += CSWlibpq5
SPKG_DESC_CSWlibpq5 = PostgreSQL $(VERSION), libpq
PKGFILES_CSWlibpq5  = $(call pkgfiles_lib,libpq.so.5)
RUNTIME_DEP_PKGS_CSWlibpq5  = CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibpq5 += CSWlibgssapi-krb5-2

BUILD_DEP_PKGS  = CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWgsed # gsed is used in this recipe
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibgnugetopt-dev

EXTRA_LD_OPTIONS  = -R$(prefix)/lib/\$$ISALIST

BUILD64 = 1
#ISAEXEC = 0
MERGE_DIRS_isa-extra = $(bindir) $(libdir) $(libexecdir)

CONFIGURE_ARGS  = $(DIRPATHS)
# This is one of the quirks mentioned at the beginning: --program-suffix is not
# supported, so IMHO, binaries should go to --libexecdir
CONFIGURE_ARGS += --bindir=$(PGBINDIR)
CONFIGURE_ARGS += --sbindir=$(PGSBINDIR)
CONFIGURE_ARGS += --sysconfdir=$(PGSYSCONFDIR)
CONFIGURE_ARGS += --datadir=$(PGDATADIR)
CONFIGURE_ARGS += --localstatedir=$(PGDATA)
CONFIGURE_ARGS += --with-includes=$(includedir)
CONFIGURE_ARGS += --with-libraries=$(libdir)
CONFIGURE_ARGS += --with-docdir=$(PGDOCDIR)

CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-libxml
CONFIGURE_ARGS += --with-libxslt
CONFIGURE_ARGS += --without-krb5
CONFIGURE_ARGS += --without-bonjour

#SKIPTEST ?= 1

include gar/category.mk
# This will generate the ALTERNATIVEs for the binaries in
# $(libexecdir)/postgresql/XY.
#
# The uppercase_* variables are used to translate the lowercase
# $(myALTERNATIVES) to uppercase.
#
# How it does create the alternatives:
#
# for pkg in $(myALTERNATIVES)
#   -- set alternative priority to 20
#   for alt in $(NEEDED_ISAS)
#     -- increment alternative priority by 10
#     -- create master alternative for pkg, remove default isa from path,
#	 store alternative in $(ALTERNATIVE_$(pkg)_$(alt)
#     -- create slave alternatives for pkg, remove default isa from path,
#	 append slave alternative to $(ALTERNATIVE_$(pkg)_$(alt)
#   end alt
# end pkg
#
# In the post-merge target, the alternatives are written to their
# respective files

uppercase_server = SERVER
uppercase_client = CLIENT
uppercase_contrib = CONTRIB
$(foreach pkg,$(myALTERNATIVES),\
	$(eval alt_priority = 20) \
	$(foreach alt,$(NEEDED_ISAS), \
		$(eval alt_priority=$(shell expr $(alt_priority) + 10)) \
		$(eval ALTERNATIVE_$(pkg)_$(alt) = $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(firstword $(BIN_NAMES_$(uppercase_$(pkg)))),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-$(pkg) $(libexecdir)/$(alt)/$(NAME)/$(BASE_VERSION_NODOT)/$(n))) $(alt_priority)) \
		$(eval ALTERNATIVE_$(pkg)_$(alt) += $(subst /$(ISA_DEFAULT)/,/,$(foreach n,$(wordlist 2,$(words $(BIN_NAMES_$(uppercase_$(pkg)))),$(BIN_NAMES_$(uppercase_$(pkg)))),$(bindir)/$(n)-$(BASE_VERSION_NODOT) $(NAME)$(BASE_VERSION_NODOT)-$(pkg) $(libexecdir)/$(alt)/$(NAME)/$(BASE_VERSION_NODOT)/$(n)))) \
	)\
)

# We adjust the $(pkglibdir) found in $(WORKSRC)/src/Makefile.global.in, so
# that it should be possible to install 8.x and 8.y concurrently
pre-configure-modulated:
	@echo " ===> Adjusting pkglibdir in $(WORKSRC)/src/Makefile.global.in"
	@if [ -r $(WORKSRC)/src/Makefile.global.in ] ; then \
		gsed -i -r -e 's|^(pkglibdir[[:space:]]*=[[:space:]]*)\$$\(libdir\).*$$|\1$$(libdir)/postgresql/$(BASE_VERSION_NODOT)|' $(WORKSRC)/src/Makefile.global.in ; \
	fi
	@$(MAKECOOKIE)

post-build-modulated:
	@echo " ===> Building contrib stuff"
	$(BUILD_ENV) gmake -C $(WORKSRC)/contrib all
	@$(MAKECOOKIE)

post-install-modulated:
	@echo " ===> Installing contrib stuff"
	$(INSTALL_ENV) gmake -C $(WORKSRC)/contrib DESTDIR=$(DESTDIR) install
	@$(MAKECOOKIE)

# We suck in the libpgport.a since pg_config is emitting
# -lpgport. Unfortunately, there is no shared lib version, and I'm too
# lazzy to adjust the build system to generate one...
post-merge-modulated:
ifeq ($(ISA),$(ISA_DEFAULT64))
	ginstall $(WORKSRC)/src/port/libpgport.a $(PKGROOT)$(libpath_install)/$(ISA_DEFAULT64)/
else
	ginstall $(WORKSRC)/src/port/libpgport.a $(PKGROOT)$(libdir)/
endif
# Move the development binaries to the standard location
	ginstall -d $(PKGROOT)$(bindir)/
	for f in $(BIN_NAMES_DEVEL) ; do \
		gmv -v $(PKGROOT)$(libexecdir)/$(NAME)/$(BASE_VERSION_NODOT)/$$f $(PKGROOT)$(bindir)/ ; \
	done

post-merge:  $(foreach n,$(POSTMSG),$(PKGROOT)/$(n)) test-installation
# Create my alternatives files.
	$(foreach a,$(myALTERNATIVES), $(foreach i,$(NEEDED_ISAS), $(info ===> Create alternative $(i) $(a)) $(shell ginstall -d $(PKGROOT)$(sharedstatedir)/alternatives ; echo "$(ALTERNATIVE_$(a)_$(i))" > $(PKGROOT)$(sharedstatedir)/alternatives/$(NAME)$(BASE_VERSION_NODOT)_$(a)_$(i) ) ) )
# Create the PGDATA directory
	@echo " ===> Create pgdata directory"
	@ginstall -d $(PKGROOT)$(PGDATA)
# Adjust the man page names.
	@echo " ===> Adjusting man page file names"
	@for i in 1 5 ; do \
		test -d $(PKGROOT)$(datadir)/man/man$$i || continue ; \
		for f in $(PKGROOT)$(datadir)/man/man$$i/* ; do \
			suffix="`echo $$f | awk 'BEGIN { FS="." } { print $$NF }'`" ; \
			f_no_suffix="`echo $$f | sed -e "s/\.$${suffix}$$//"`" ; \
			dont_move=0 ; \
			for d in $(BIN_NAMES_DEVEL) ; do \
				bname="`basename $${f_no_suffix}`" ; \
				if test "$${bname}" = "$$d" ; then \
					dont_move=1 ; \
					break ; \
				fi ; \
			done ; \
			test $${dont_move} -eq 0 && mv $$f $${f_no_suffix}-$(BASE_VERSION_NODOT).$${suffix} ; \
		done ;\
	done
# Change path names in documentation
	@echo " ===> Adjust path names in documentation"
	@for f in $(PKGROOT)$(docdir)/$(NAME)/$(BASE_VERSION_NODOT)/html/*.html $(PKGROOT)$(mandir)/man1/*.1 $(PKGROOT)$(datadir)/$(NAME)/$(BASE_VERSION_NODOT)/*.sample ; do \
		gsed -i -e 's|/usr/local/pgsql/data|$(localstatedir)/$(NAME)/$(BASE_VERSION_NODOT)|g' \
			-e 's|/usr/local/pgsql/|$(prefix)/|g' \
			-e 's|/usr/local|$(prefix)|g' \
			-e 's|/usr/share|$(datadir)|g' $$f ; \
	done
	@echo " ===> Install postmsg"
	$(foreach n,$(POSTMSG), $(shell ginstall -d $(PKGROOT)$(dir $(n))) $(shell ginstall $(WORKDIR)/$(notdir $(n)) $(PKGROOT)$(n)))
	@$(MAKECOOKIE)

pre-package:
# The postinstall for the server package
	@echo " ===> Install postinstall script"
	@ginstall $(WORKDIR)/$(SERVERPOSTINSTTMPL) $(WORKDIR)/$(SERVERPOSTINST_VERSIONED)
# The usergroup file
	@echo " ===> Install usergroup file"
	@ginstall -d $(PKGROOT)$(USERGROUPDIR)
	@ginstall $(WORKDIR)/$(USERGROUPFILETMPL) $(PKGROOT)$(USERGROUPDIR)/$(USERGROUPFILE_VERSIONED)
# The init script
	@echo " ===> Install init script"
	@ginstall -d $(PKGROOT)$(sysconfdir)/init.d
	@ginstall $(WORKDIR)/$(INITSCRIPTFILETMPL) $(PKGROOT)$(sysconfdir)/init.d/$(INITSCRIPTFILE_VERSIONED)
	@chmod 0755 $(PKGROOT)$(sysconfdir)/init.d/$(INITSCRIPTFILE_VERSIONED)
# The init script config
	@echo " ===> Install init script config"
	@ginstall $(WORKDIR)/$(CSWPGSQLCONFFILETMPL) $(PKGROOT)$(sysconfdir)/$(CSWPGSQLCONFFILE_VERSIONED).CSW
# Remove all the README.CSW, since they have not expanded the
# variables, and copy only the one's we're interested in
	@echo " ===> Remove all README.CSW"
	@for f in $(PKGROOT)$(docdir)/*/README.CSW ; do \
		rm $$f ; \
	done
	@echo " ==> Install variable expanded README.CSW"
	@for d in $(foreach n,$(myALTERNATIVES),$(NAME)$(BASE_VERSION_NODOT)_$(n)) $(NAME)$(BASE_VERSION_NODOT) ; do \
		ginstall $(WORKDIR)/README.CSW $(PKGROOT)$(docdir)/$$d/ ; \
	done
	@$(MAKECOOKIE)

$(foreach n,$(POSTMSG),$(PKGROOT)/$(n)):
	@echo " ===> Linking Post Messages"
	@ginstall -d $(dir $@)
	@ln $(DOWNLOADDIR)/$(notdir $@) $@

$(foreach n,$(POSTMSG),$(DOWNLOADDIR)/$(notdir $(n))):
	@echo " ===> Generating $(notdir $@)"
	@echo "" > $@
	@echo "---" >> $@
	@echo "" >> $@
	@echo "There are 32bit and 64bit versions of $(NAME) $(VERSION) binaries on the system installed:" >> $@
	@echo "" >> $@
	@echo "You can easily select between the versions with the alternatives(8)" >> $@
	@echo "system by executing" >> $@
	@echo "" >> $@
	@echo "  /opt/csw/sbin/alternatives --config $(subst .postmsg,,$(subst CSW,,$(notdir $@)))" >> $@
	@echo "" >> $@
	@echo "See http://www.opencsw.org/packages/alternatives for details." >> $@
	@echo "" >> $@
	@echo "---" >> $@
	@echo "" >> $@
	@$(MAKECOOKIE)

test-installation:
# Check if all binaries and libraries defined in the variables
# BIN_NAMES_* and SO_NAMES_* are there
	@echo " ===> Checking for extra binaries in BIN_NAMES_*"
	@for n in $(BIN_NAMES_SERVER) $(BIN_NAMES_CLIENT) $(BIN_NAMES_CONTRIB) ; do \
		if [ -f $(PKGROOT)$(PGBINDIR)/$$n ] ; then\
			: ; \
		else \
			echo "Extra binary defined $$n" ; \
			exit 1 ; \
		fi ; \
	done
	@echo " ===> Checking for extra libraries in SO_NAMES_*"
	@for n in $(SO_NAMES_SERVER) $(SO_NAMES_CONTRIB) ; do \
		if [ -f $(PKGROOT)$(libdir)/$(NAME)/$(BASE_VERSION_NODOT)/$$n ] ; then\
			: ; \
		else \
			echo "Extra library defined $$n" ; \
			exit 1 ; \
		fi ; \
	done
# Check if all binaries and libraries in the pkgroot are contained in
# the respective recipe variables.
	@echo " ===> Checking for missing binaries in BIN_NAMES_*"
	@for n in `gfind $(PKGROOT)$(PGBINDIR) -maxdepth 1 -type f` ; do \
		echo "$(BIN_NAMES_SERVER) $(BIN_NAMES_CLIENT) $(BIN_NAMES_CONTRIB)" | grep `basename $$n` >/dev/null 2>&1 ; \
		if [ $$? -eq 0 ] ; then \
			: ; \
		else \
			echo "Binary `basename $$n` not defined" ; \
			exit 1 ; \
		fi ; \
	done
	@echo " ===> Checking for missing binaries in SO_NAMES_*"
	@for n in `gfind $(PKGROOT)$(libdir)/$(NAME)/$(BASE_VERSION_NODOT) -maxdepth 1 -type f` ; do \
		echo "$(SO_NAMES_SERVER) $(SO_NAMES_CONTRIB)" | grep `basename $$n` >/dev/null 2>&1 ; \
		if [ $$? -eq 0 ] ; then \
			: ; \
		else \
			echo "Library `basename $$n` not defined" ; \
			exit 1 ; \
		fi ; \
	done
