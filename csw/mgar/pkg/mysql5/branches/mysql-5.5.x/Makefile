# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# If you are involved in packaging MySQL, consider subscribing to the
# packagers mailing list:
# http://lists.mysql.com/packagers
#
# About building MySQL with cmake:
# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
#
# http://dev.mysql.com/doc/refman/5.5/en/source-configuration-options.html
#
PROJ_NAME    = mysql
NAME         = $(PROJ_NAME)5
BASE_VERSION = 5.5
PATCHLEVEL   = 44
ALTS_PRIO    = 55
VERSION = $(BASE_VERSION).$(PATCHLEVEL)

# Useful when making a series of builds on the same day
# GARFLAVOR ?= DBG

#PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# Keep default old Studio 12.0 for old S9 only
ifneq ($(shell /usr/bin/uname -r),5.9)
       GARCOMPILER = GCC4
       # Try to get some more oomph out of a sparc
       # Benchmarks w/ 5.5.34 show no obvious benefit, so disabled for now
       #EXTRA_BUILD_ISAS_sparc = sparcv9+vis2
endif

# There is some assembler code, which doesn't work on sparcv8, and I don't see
# an easy way to switch it off.
ISA_DEFAULT_sparc-5.9 = sparcv8plus

# Solaris 10 needs a special map file since we need libnsl Version 1.9.1
# and libc 1.22.5

ifneq ($(shell /usr/bin/uname -r),5.9)
	LINKER_MAPS ?= -M "$(abspath $(WORKDIR)/map.mysql)"
endif

DISTNAME = mysql-$(VERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

### For Studio 12.3
# Those options follow those of the Solaris 11 build
# https://java.net/projects/solaris-userland/sources/gate/show/components/mysql-5-1?rev=1502
EXTRA_CXXFLAGS_SOS12_64  += -features=no%except

# Required at -xO4
# https://java.net/projects/solaris-userland/sources/gate/content/make-rules/shared-macros.mk?rev=1505`
EXTRA_CFLAGS_SOS12_sparc += -xregs=no%appl
EXTRA_CFLAGS_SOS12_i386  += -xregs=no%frameptr

EXTRA_CFLAGS_SOS12 += -xstrconst -xprefetch=auto -xprefetch_level=3 -fns=no -fsimple=1 -xbuiltin=%none -xlibmil -xlibmopt -xnorunpath -mt -KPIC -DPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm $(EXTRA_CFLAGS_SOS12_$(GARCH))
EXTRA_CXXFLAGS_SOS12 += -noex -xprefetch=auto -xprefetch_level=3 -fns=no -fsimple=1 -xbuiltin=%none -xlibmil -xlibmopt -mt -KPIC -DPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm $(EXTRA_CXXFLAGS_SOS12_$(MEMORYMODEL))

### For GCC4
EXTRA_CFLAGS_GCC4_sparc += -mno-app-regs

EXTRA_CFLAGS_GCC4 += -pthread -fPIC -DPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm $(EXTRA_CFLAGS_GCC4_$(GARCH))
EXTRA_CXXFLAGS_GCC4 += -pthread -fPIC -DPIC -DDBUG_OFF -DHAVE_OPENSSL -DMULTI_THREADED -lm $(EXTRA_CXXFLAGS_GCC4_$(MEMORYMODEL))

###
EXTRA_CFLAGS = $(EXTRA_CFLAGS_$(GARCOMPILER))
###

EXTRA_LINKER_FLAGS = -lm


# The Solaris 11 build uses -xO4 by default
OPT_FLAGS_SOS12_32 = -xO4
OPT_FLAGS_SOS12_64 = -xO4
OPT_FLAGS_SOS12_sparc_32 = -xmemalign=8s
OPT_FLAGS_SOS12_sparc_64 = -xmemalign=16s
OPT_FLAGS_SOS12 += $(OPT_FLAGS_SOS12_$(MEMORYMODEL)) $(OPT_FLAGS_SOS12_$(GARCH)_$(MEMORYMODEL)) $(OPT_FLAGS_SOS12_$(ISA))

OPT_FLAGS_GCC4_32 = -O3
OPT_FLAGS_GCC4_64 = -O3
OPT_FLAGS_GCC4 += $(OPT_FLAGS_GCC4_$(MEMORYMODEL)) $(OPT_FLAGS_GCC4_$(GARCH)_$(MEMORYMODEL)) $(OPT_FLAGS_GCC4_$(ISA))

INITSMF = $(sysconfdir)/init\.d/csw$(NAME)

MYSQL_LIB_VER = 18

# The daemon to launch is selected by script, should not be automatic
# Some other files too should probably not be isaexec'd
EXTRA_ISAEXEC_EXCLUDE_FILES  = /opt/csw/libexec/mysqld
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/mysql_config
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/mysqld_safe
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/mysqld_multi
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/my_print_defaults
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/mysqlaccess
EXTRA_ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/mysqlaccess.conf

PATCHFILES += 0003-I-HATE-CMAKE.patch
#PATCHFILES += 0003-WHY-IS-CMAKE-TRYING-TO-BE-SMARTER-THAN-ME.patch
PATCHFILES += 0003-Use-bash-for-mysqld_safe.patch
# https://java.net/projects/solaris-userland/sources/gate/content/components/mysql-5-1/patches/xO4_optimization.patch?rev=1502
PATCHFILES += 0004-xO4-fix.patch

PACKAGES += CSWmysql-dev
SPKG_DESC_CSWmysql-dev = MySQL development files
PKGFILES_CSWmysql-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWmysql-dev += CSWlibmysqlclient$(MYSQL_LIB_VER)
CSWmysql-dev_programs += mysql_config
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(bindir)/$(bin_name))
PKGFILES_CSWmysql-dev  += $(foreach bin_name,$(CSWmysql-dev_programs),$(sbindir)/$(bin_name))
PKGFILES_CSWmysql-dev  += $(mandir)/man1/mysql_config.*
PKGFILES_CSWmysql-dev  += $(prefix)/include.*
CHECKPKG_OVERRIDES_CSWmysql-dev += file-collision                             

PACKAGES += CSWlibmysqlclient$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_5.9 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += $(RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER)_$(GAROSREL))
# For GCC4
RUNTIME_DEP_PKGS_CSWlibmysqlclient$(MYSQL_LIB_VER) += CSWlibgcc-s1

PACKAGES += CSWlibmysqlclient-r$(MYSQL_LIB_VER)
PKGFILES_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += $(call baseisadirs,$(libdir),libmysqlclient_r\.so\.$(MYSQL_LIB_VER)(\.\d+)*)
SPKG_DESC_CSWlibmysqlclient-r$(MYSQL_LIB_VER) += MySQL $(BASE_VERSION) client library, libmysqlclient_r.so.$(MYSQL_LIB_VER)
RUNTIME_DEP_PKGS_CSWlibmysqlclient-r18 += CSWlibmysqlclient18
# Appears required by recent chkpkg changes, may be a bug
CHECKPKG_OVERRIDES_CSWlibmysqlclient-r18 += surplus-dependency|CSWlibmysqlclient18

# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
client_programs += myisamlog
client_programs += myisampack
client_programs += mysql
client_programs += mysqlaccess
client_programs += mysqladmin
client_programs += mysqlbin
client_programs += mysqlbinlog
client_programs += mysqlcheck
client_programs += mysql_client_test
client_programs += mysqldump
client_programs += mysqlhotcopy
client_programs += mysqlimport
client_programs += mysqlshow
client_programs += mysql_zap
client_programs += perror
client_programs += replace

PACKAGES += CSW$(NAME)client
SPKG_DESC_CSW$(NAME)client = MySQL $(BASE_VERSION) client binaries
PKGFILES_CSW$(NAME)client  = $(bindir)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(bindir)/$(bin_name))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(client_programs),$(sbindir)/$(bin_name))
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)client_5.9 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)client_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)client += $(RUNTIME_DEP_PKGS_CSW$(NAME)client_$(GAROSREL))
### For GCC4
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibstdc++6
CHECKPKG_OVERRIDES_CSW$(NAME)client += file-collision
#CHECKPKG_OVERRIDES_CSW$(NAME)client += bad-rpath-entry

# It's intentional. There's a sparcv8-incompatible assembler code there, so we
# must build for sparcv8+ on Solaris 9.
ifeq ($(shell /usr/bin/uname -pr),5.9 sparc)
  CHECKPKG_OVERRIDES_CSW$(NAME)client += binary-architecture-does-not-match-placement
  CHECKPKG_OVERRIDES_CSW$(NAME) += binary-architecture-does-not-match-placement
  CHECKPKG_OVERRIDES_CSWlibmysqlclient18 += binary-architecture-does-not-match-placement
endif

#CHECKPKG_OVERRIDES_CSWlibmysqlclient18 += bad-rpath-entry

PACKAGES += CSW$(NAME)
SPKG_DESC_CSW$(NAME) = Multithreaded SQL database
RUNTIME_DEP_PKGS_CSW$(NAME) += CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibz1
RUNTIME_DEP_PKGS_CSW$(NAME)_5.9 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)_5.10 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME) += $(RUNTIME_DEP_PKGS_CSW$(NAME)_$(GAROSREL))
### For GCC4
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSW$(NAME) += CSWlibwrap1

CHECKPKG_OVERRIDES_CSW$(NAME) += bad-rpath-entry
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/sparcv9/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1
CHECKPKG_OVERRIDES_CSW$(NAME) += no-direct-binding|/opt/csw/libexec/amd64/mysqld|is|not|directly|bound|to|soname|libmtmalloc.so.1
CHECKPKG_OVERRIDES_CSW$(NAME) += file-collision

# An example:
# s9_preload.so.1|is|needed|by|/opt/csw/bin/innochecksum|but|never|used
#CHECKPKG_OVERRIDES_CSW$(NAME) += soname-unused

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/mysql-test.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/sql-bench.*
EXTRA_MERGE_EXCLUDE_FILES += $(datadir)/mysql-test.*

# Enable 64 bits, but not for Solaris 9 x86
BUILD64_5.9_sparc = 1
BUILD64_5.10_sparc = 1
BUILD64_5.9_i386 =
BUILD64_5.10_i386 = 1
BUILD64 = $(BUILD64_$(GAROSREL)_$(GARCH))
ISAEXEC = 1

MASTER_SITES  = http://ftp.heanet.ie/mirrors/www.mysql.com/Downloads/MySQL-$(BASE_VERSION)/
MASTER_SITES += http://mysql.skynet.be/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(VERSION).tar.gz
DISTFILES += csw$(NAME).tpl
DISTFILES += quick_start-csw
DISTFILES += CSW$(NAME).preinstall
DISTFILES += CSW$(NAME).postinstall
DISTFILES += cswusergroup
DISTFILES += map.mysql
DISTFILES += README.CSW

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWcmake
BUILD_DEP_PKGS += CSWbison
BUILD_DEP_PKGS += CSWlibwrap-dev

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DINSTALL_LAYOUT=RPM
CMAKE_ARGS += -DMYSQL_DATADIR=$(localstatedir)/$(NAME)
CMAKE_ARGS += -DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS += -DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SCRIPTDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
CMAKE_ARGS += -DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS += -DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/plugin
CMAKE_ARGS += -DINSTALL_DOCDIR=$(subst $(prefix)/,,$(docdir))/$(NAME)
CMAKE_ARGS += -DINSTALL_DOCREADMEDIR=$(subst $(prefix)/,,$(docdir))/$(NAME)
CMAKE_ARGS += -DINSTALL_INFODIR=$(subst $(prefix)/,,$(infodir))/$(NAME)
CMAKE_ARGS += -DINSTALL_MYSQLSHAREDIR=$(subst $(prefix)/,,$(sharedstatedir))/$(NAME)
CMAKE_ARGS += -DINSTALL_SUPPORTFILESDIR=$(subst $(prefix)/,,$(sharedstatedir))/$(NAME)/support-files
CMAKE_ARGS += -DWITH_LIBWRAP=1
CMAKE_ARGS += -DWITH_SSL=system
CMAKE_ARGS += -DWITH_ZLIB=system
CMAKE_ARGS += -DDEFAULT_CHARSET=utf8
CMAKE_ARGS += -DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS += -DCOMPILATION_COMMENT='OpenCSW'
CMAKE_ARGS += -DBUILD_CONFIG=mysql_release
CMAKE_ARGS += -DOPENSSL_ROOT_DIR=$(prefix)
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS += -DBISON_EXECUTABLE=$(prefix)/bin/bison
CMAKE_ARGS += "-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON"

# The line below come from the official MySQL build configuration
CMAKE_ARGS += "-DENABLED_PROFILING:BOOL=ON"
CMAKE_ARGS += "-DENABLE_DEBUG_SYNC:BOOL=ON"
CMAKE_ARGS += "-DENABLE_GCOV:BOOL=OFF"
CMAKE_ARGS += "-DWITH_ARCHIVE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_BLACKHOLE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_DEBUG:BOOL=OFF"
CMAKE_ARGS += "-DWITH_EMBEDDED_SERVER:BOOL=ON"
CMAKE_ARGS += "-DWITH_EXAMPLE_STORAGE_ENGINE:BOOL=OFF"
CMAKE_ARGS += "-DWITH_EXTRA_CHARSETS:STRING=all"
CMAKE_ARGS += "-DWITH_FEDERATED_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_INNOBASE_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_PARTITION_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_PERFSCHEMA_STORAGE_ENGINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_PIC:BOOL=ON"
CMAKE_ARGS += "-DWITH_READLINE:BOOL=ON"
CMAKE_ARGS += "-DWITH_UNIT_TESTS:BOOL=ON"
CMAKE_ARGS += "-DWITH_VALGRIND:BOOL=OFF"
ifneq ($(shell /usr/bin/uname -r),5.9)
CMAKE_ARGS += "-DENABLE_DTRACE:BOOL=ON"
endif


USERGROUP = $(sysconfdir)/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS   = dbdir
PROTOTYPE_FILES_dbdir = $(localstatedir)/$(NAME)
PROTOTYPE_USER_dbdir  = mysql
PROTOTYPE_GROUP_dbdir = mysql
PROTOTYPE_PERMS_dbdir = 0700
PROTOTYPE_CLASS_dbdir = ugfiles

CHECKPKG_OVERRIDES_CSW$(NAME) += surplus-dependency|CSW$(NAME)client
CHECKPKG_OVERRIDES_CSW$(NAME)bench += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME)bench += surplus-dependency|CSW$(NAME)
CHECKPKG_OVERRIDES_CSW$(NAME)test += file-with-bad-content
CHECKPKG_OVERRIDES_CSW$(NAME)test += surplus-dependency|CSW$(NAME)

# This could be reviewed.
CHECKPKG_OVERRIDES_CSW$(NAME) += file-with-bad-content

EXECUTABLES += innochecksum
EXECUTABLES += msql2mysql
EXECUTABLES += my_print_defaults
EXECUTABLES += myisam_ftdump
EXECUTABLES += myisamchk
EXECUTABLES += myisamlog
EXECUTABLES += myisampack
EXECUTABLES += mysql
EXECUTABLES += mysql_client_test
EXECUTABLES += mysql_config
EXECUTABLES += mysql_convert_table_format
EXECUTABLES += mysql_find_rows
EXECUTABLES += mysql_fix_extensions
EXECUTABLES += mysql_plugin
EXECUTABLES += mysql_secure_installation
EXECUTABLES += mysql_setpermission
EXECUTABLES += mysql_tzinfo_to_sql
EXECUTABLES += mysql_upgrade
EXECUTABLES += mysql_waitpid
EXECUTABLES += mysql_zap
EXECUTABLES += mysqlaccess
EXECUTABLES += mysqlaccess.conf
EXECUTABLES += mysqladmin
EXECUTABLES += mysqlbinlog
EXECUTABLES += mysqlbug
EXECUTABLES += mysqlcheck
EXECUTABLES += mysqld
EXECUTABLES += mysqld_multi
EXECUTABLES += mysqld_safe
EXECUTABLES += mysqldump
EXECUTABLES += mysqldumpslow
EXECUTABLES += mysqlhotcopy
EXECUTABLES += mysqlimport
EXECUTABLES += mysqlshow
EXECUTABLES += mysqlslap
EXECUTABLES += mysqltest
EXECUTABLES += perror
EXECUTABLES += replace
EXECUTABLES += resolve_stack_dump
EXECUTABLES += resolveip

CONFIGURE_SCRIPTS = custom

TEST_TARGET = test

include gar/category.mk

test-custom:
	alias sh=/usr/bin/bash;                           \
		cd $(WORKSRC)/mysql-test;                       \
		perl mysql-test-run.pl --mem --big-test --force \
		--skip-test=archive-big --skip-test=/gis/

configure-custom:
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)

post-configure-modulated:
	gsed \
		-e 's|@prefix@|$(prefix)|g' \
		-e 's|@localstatedir@|$(localstatedir)/$(NAME)|g' \
		-e 's|@sysconfdir@|$(sysconfdir)|g' \
		-e 's|@bindir@|$(bindir)|g' \
		-e 's|@BASE_VERSION@|$(BASE_VERSION)|g' \
		< $(WORKDIR)/csw$(NAME).tpl \
		> $(WORKDIR)/csw$(NAME)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/csw$(NAME) $(DESTDIR)$(sysconfdir)/init.d
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18; \
		ln -s libmysqlclient.so.18 libmysqlclient_r.so.18)
	(cd $(DESTDIR)$(libdir); rm libmysqlclient_r.so.18.0.0; \
		ln -s libmysqlclient.so.18.0.0 libmysqlclient_r.so.18.0.0)

	# Make sure the proper binary is called by the script since
	# mgar does the configure part using only the base arch name, w/o
	# the special instructions part
	# Only needed for 64 bit
	if [ "$(MEMORYMODEL)" = 64 ]; then \
		for file in mysqld_safe mysqld_multi; do \
			perl -pi \
				-e 'if (/^[^#]/) { s|/bin(?!/$(ISABINDIR))|/bin/$(ISABINDIR)|g }' \
				-e 'if (/^[^#]/) { s|/sbin(?!/$(ISABINDIR))|/sbin/$(ISABINDIR)|g }' \
				-e 'if (/^[^#]/) { s|/libexec(?!/$(ISABINDIR))|/libexec/$(ISABINDIR)|g }' \
				$(DESTDIR)$(bindir)/$$file; \
		done; \
	fi

	# Remove compiler-specific parameters
	gsed -i \
		-e '/^[^#]/s/-xO[0-5][^ ]* *//g' \
		-e '/^[^#]/s/-xarch=[^ ]* *//g' \
		-e '/^[^#]/s/-xchip=[^ ]* *//g' \
		-e '/^[^#]/s/-norunpath[^ ]* *//g' \
		-e '/^[^#]/s/-lCrun[^ ]* *//g' \
		-e '/^[^#]/s/-lCstd[^ ]* *//g' \
		-e '/^[^#]/s/-mtune=[^ ]* *//g' \
		-e '/^[^#]/s/-march=[^ ]* *//g' \
		-e '/^[^#]/s/-Wall *//g' \
		-e '/^[^#]/s/-pipe *//g' \
		-e '/^[^#]/s/-KPIC/-fPIC/g' \
		-e '/^[^#]/s/-mno-app-regs//g' \
		-e '/^[^#]/s/-fno-omit-frame-pointer//g' \
		-e '/^[^#]/s/-fno-strict-aliasing//g' \
		-e '/^[^#]/s/-Wa[^ ]*//g' \
		-e '/^[^#]/s/-static-libgcc//g' \
		-e '/^[^#]/s/-pthread//g' \
		$(DESTDIR)$(bindir)/mysql_config

	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)/$(NAME)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/doc/$(NAME)
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)
	# http://www.opencsw.org/bugtrack/view.php?id=4149
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)
	@$(MAKECOOKIE)
