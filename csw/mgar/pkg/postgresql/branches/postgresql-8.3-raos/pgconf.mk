# $Id$

#
# Postgres specific variables
#
PGBINDIR		= $(libexecdir)/$(NAME)/$(BASE_VERSION_NODOT)
PGSBINDIR		= $(libexecdir)/$(NAME)/$(BASE_VERSION_NODOT)
PGDATADIR		= $(datadir)/$(NAME)/$(BASE_VERSION_NODOT)
PGDOCDIR		= $(datadir)/doc/$(NAME)/$(BASE_VERSION_NODOT)
PGLOCALSTATEDIR_BASE	= $(localstatedir)/$(NAME)
PGDATA			= $(PGLOCALSTATEDIR_BASE)/$(BASE_VERSION_NODOT)
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

# These are the alternatives provided for the packages.  I use them in the
# recipe to iterate over all possible alternatives (see 'post-merge:')
myALTERNATIVES= server client devel contrib

# My sed, since EXPANDVARS has proven unreliable to me
mySED = gsed -e 's|@USERGROUPFILE_VERSIONED@|$(USERGROUPFILE_VERSIONED)|g' \
	-e 's|@CSWPGSQLCONFFILE_VERSIONED@|$(CSWPGSQLCONFFILE_VERSIONED)|g' \
	-e 's|@INITSCRIPTFILE_VERSIONED@|$(INITSCRIPTFILE_VERSIONED)|g' \
	-e 's|@NAME@|$(NAME)|g' \
	-e 's|@VERSION@|$(VERSION)|g' \
	-e 's|@BASE_VERSION_NODOT@|$(BASE_VERSION_NODOT)|g' \
	-e 's|@PGLOCALSTATEDIR_BASE@|$(PGLOCALSTATEDIR_BASE)|g' \
	-e 's|@PGDATA@|$(PGDATA)|g' \
	-e 's|@sysconfdir@|$(sysconfdir)|g' \
	-e 's|@bindir@|$(bindir)|g'

