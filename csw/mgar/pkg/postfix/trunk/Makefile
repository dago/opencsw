#
#
# !!! This package can be built in two flavors, a regular one with full
# !!! features enabled and one with a core feature set, i.e. reduced
# !!! dependencies (package name suffix: -simple).
# !!! To build the simplified set, the whole build needs to run with
# !!! BUILDTYPE=simple. Further details below. By now this needs to be
# !!! carried out manually. Ideas to automate the process of building
# !!! the two packages are welcome.
#
#
# TODO (release-critical prefixed with !, non release-critical with *)
# * Some files collide with CSWsendmail, the following are alternatives lines from
#   the Sendmail package, they should be adapted to Postfix so Postfix and Sendmail
#   can co-exist on the same system (and pass checkpkg file collision detection).
#     ALTERNATIVES_CSWsendmail  = sendmail
#     ALTERNATIVE_sendmail  = $(bindir)/mailq sendmail $(bindir)/mailq.sendmail 100
#     ALTERNATIVE_sendmail += $(bindir)/newaliases newaliases $(bindir)/newaliases.sendmail
#     ALTERNATIVE_sendmail += $(mandir)/man1/mailq.1 mailq.1 $(mandir)/man1/mailq1.1.sendmail
#     ALTERNATIVE_sendmail += $(mandir)/man1/newaliases.1 newaliases.1 $(mandir)/man1/newaliases.1.sendmail
#     ALTERNATIVE_sendmail += $(mandir)/man5/aliases.5 aliases.5 $(mandir)/man5/aliases.5.sendmail
# * Ship simple default configuration (restrict mynetworks to 127.0.0.1?)
# * alias_database points to /etc/mail/aliases, symlink
#   /etc/opt/csw/postfix/aliases to /etc/mail/aliases?
#
# NICE TO KNOW
# - 2.4.6,REV=2008.05.28 preserves modified configuration files via
#   package-shipped CAS class csw_conf.
#
# $Id$
# 
NAME = postfix
VERSION = 2.11.5
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A high-performance mail transport agent
define BLURB
  What is Postfix? It is Wietse Venema's mailer that started life as an
  alternative to the widely-used Sendmail program. 
  
  Postfix attempts to be fast, easy to administer, and secure, while at
  the same time being sendmail compatible enough to not upset existing
  users. Thus, the outside has a sendmail-ish flavor, but the inside is
  completely different.
endef

VENDOR_URL   = http://www.postfix.org
MASTER_SITES = ftp://ftp.porcupine.org/mirrors/postfix-release/official/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE      = LGARCOMPILER = GCC4 LICENSE TLS_LICENSE

# Tag configuration files for handling via cswclassutils
CONFIG_BASE  := /etc/opt/csw/postfix/
CONFIG_FILES := access 
CONFIG_FILES += aliases
CONFIG_FILES += canonical
CONFIG_FILES += generic
CONFIG_FILES += header_checks
CONFIG_FILES += main.cf
CONFIG_FILES += master.cf
CONFIG_FILES += relocated
CONFIG_FILES += transport
CONFIG_FILES += virtual
SAMPLECONF   := $(addprefix $(CONFIG_BASE), $(CONFIG_FILES))

sysconfdir  = /etc/opt/csw
INITSMF     = $(sysconfdir)/init.d/csw$(NAME)
USERGROUP   = $(sysconfdir)/pkg/CSW$(NAME)/cswusergroup

# For the sake of simplicity and user choice we dropped the automatic
# replacement of the /usr/{lib,bin} sendmail binaries. Ref.
# http://article.gmane.org/gmane.os.solaris.opencsw.maintainers/5313
POSTMSG     = $(docdir)/$(NAME)/README.upgradefrom.24

# For file permissions reference and verification purposes, postfix ships
# /opt/csw/libexec/postfix/postfix-files which contains a list of the
# desired settings. "postfix check" can be used to verify the permissions,
# "postfix set-permissions" can be used to adjust them (which shouldn't
# be necessary from a user standpoint, it's our job to ship the right perms).

# Make postdrop setgid so that it can deliver to $(DEF_QUEUE_DIR)/maildrop
PROTOTYPE_MODIFIERS = makesgid
PROTOTYPE_FILES_makesgid = $(sbindir)/post(drop|queue)
PROTOTYPE_GROUP_makesgid = postdrop
PROTOTYPE_PERMS_makesgid = 2755
PROTOTYPE_CLASS_makesgid = ugfiles

# Make $(DEF_QUEUE_DIR) subdirs accessible/writable to postfix only
PROTOTYPE_MODIFIERS += spooldir
PROTOTYPE_FILES_spooldir = $(DEF_QUEUE_DIR)/.*
PROTOTYPE_USER_spooldir  = postfix
PROTOTYPE_PERMS_spooldir = 0700
PROTOTYPE_CLASS_spooldir = ugfiles

# Make $(DEF_DATA_DIR) writable by postfix (used for master.lock)
PROTOTYPE_MODIFIERS += lockdir
PROTOTYPE_FILES_lockdir = $(DEF_DATA_DIR)
PROTOTYPE_USER_lockdir  = postfix
PROTOTYPE_PERMS_lockdir = 0700
PROTOTYPE_CLASS_lockdir = ugfiles

# Make $(DEF_QUEUE_DIR)/maildrop accessible by postdrop group
PROTOTYPE_MODIFIERS += maildrop
PROTOTYPE_FILES_maildrop = $(DEF_QUEUE_DIR)/maildrop
PROTOTYPE_GROUP_maildrop = postdrop
PROTOTYPE_PERMS_maildrop = 0730
PROTOTYPE_CLASS_maildrop = ugfiles

# Make $(DEF_QUEUE_DIR)/public accessible by postdrop group, likely
# used for IPC with other processes (public contains sockets).
PROTOTYPE_MODIFIERS += public
PROTOTYPE_FILES_public = $(DEF_QUEUE_DIR)/public
PROTOTYPE_GROUP_public = postdrop
PROTOTYPE_PERMS_public = 2710
PROTOTYPE_CLASS_public = ugfiles

# IMPORTANT! Make $(DEF_QUEUE_DIR)/pid accessible by root only
# http://www.openwall.com/lists/oss-security/2009/09/18/6
PROTOTYPE_MODIFIERS += pid
PROTOTYPE_FILES_pid = $(DEF_QUEUE_DIR)/pid
PROTOTYPE_USER_pid  = root
PROTOTYPE_GROUP_pid = bin
PROTOTYPE_PERMS_pid = 0755
PROTOTYPE_CLASS_pid = ugfiles

EXTRA_MERGE_EXCLUDE_FILES  = $(CONFIG_BASE)/LICENSE
EXTRA_MERGE_EXCLUDE_FILES += $(CONFIG_BASE)/TLS_LICENSE
EXTRA_MERGE_EXCLUDE_FILES += $(CONFIG_BASE)/makedefs.out

STRIP_DIRS = $(DESTDIR)$(libexecdir)/postfix

CONFIGURE_SCRIPTS = custom
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

# Supporting documentation for building postfix
# - Postfix Installation From Source Code 
#   http://www.postfix.org/INSTALL.html
# - Guidelines for Package Builders
#   http://www.postfix.org/PACKAGE_README.html

DEF_COMMAND_DIR    = /opt/csw/sbin
DEF_CONFIG_DIR     = $(CONFIG_BASE)
DEF_DAEMON_DIR     = /opt/csw/libexec/postfix
DEF_MAILQ_PATH     = /opt/csw/bin/mailq
DEF_HTML_DIR       = /opt/csw/share/doc/postfix/html
DEF_MANPAGE_DIR    = /opt/csw/share/man
DEF_NEWALIAS_PATH  = /opt/csw/bin/newaliases
DEF_QUEUE_DIR      = /var/opt/csw/spool/postfix
DEF_DATA_DIR       = /var/opt/csw/lib/postfix
DEF_README_DIR     = /opt/csw/share/doc/postfix/README_FILES

DEFAULTS=\
	-DDEF_MANPAGE_DIR=\"$(DEF_MANPAGE_DIR)\" \
	-DDEF_COMMAND_DIR=\"$(DEF_COMMAND_DIR)\" \
	-DDEF_CONFIG_DIR=\"$(DEF_CONFIG_DIR)\" \
	-DDEF_DAEMON_DIR=\"$(DEF_DAEMON_DIR)\" \
	-DDEF_MAILQ_PATH=\"$(DEF_MAILQ_PATH)\" \
	-DDEF_HTML_DIR=\"$(DEF_HTML_DIR)\" \
	-DDEF_NEWALIAS_PATH=\"$(DEF_NEWALIAS_PATH)\" \
	-DDEF_QUEUE_DIR=\"$(DEF_QUEUE_DIR)\" \
	-DDEF_DATA_DIR=\"$(DEF_DATA_DIR)\" \
	-DDEF_README_DIR=\"$(DEF_README_DIR)\"

# By setting BUILDTYPE=simple on the command line you can produce a
# bare-bones postfix package without any dependencies to other CSW pkgs.
# This is currently for on demand personal use, as Phil insists on the
# possibility of "pkg-get -i all" and two postfix's would clash.
# Eventually it might be nice two have a bare-bones postfix in the catalog
# as not everyone might want to pull in all the extra deps from CSWpostfix.
ifeq ($(BUILDTYPE),simple)
PACKAGES = CSW$(NAME)-simple
CATALOGNAME = $(NAME)_simple
else
# Make sure libraries in the default location can be found
AUXLIBS = $(LDFLAGS)

# Activate support for PCRE
# http://www.postfix.org/PCRE_README.html
FEATURES += -DHAS_PCRE
AUXLIBS  += -lpcre
BUILD_DEP_PKGS += CSWlibpcre-dev
RUNTIME_DEP_PKGS += CSWlibpcre1

# Activate support for hash and btree lookup tables
# http://www.postfix.org/DB_README.html. !! Takeaway: Use same DB as SASL !!
# "If you compile Postfix with a different Berkeley DB implementation,
# then every Postfix program will dump core because either the system library,
# the SASL library, or Postfix itself ends up using the wrong version."
#
FEATURES += -DHAS_DB
INCLUDES += -I/opt/csw/bdb48/include 
AUXLIBS  += -L/opt/csw/bdb48/lib -R/opt/csw/bdb48/lib -ldb-4.8
BUILD_DEP_PKGS += CSWbdb48devel
RUNTIME_DEP_PKGS += CSWbdb48

# Activate support for SSL/TLS
# http://www.postfix.org/TLS_README.html
FEATURES += -DUSE_TLS
AUXLIBS  += -lssl -lcrypto
BUILD_DEP_PKGS += CSWlibssl-dev
RUNTIME_DEP_PKGS += CSWlibssl1-0-0

# Activate support for Cyrus SASL (dovecot is incl. automatically)
# http://www.postfix.org/SASL_README.html
FEATURES += -DUSE_SASL_AUTH -DUSE_CYRUS_SASL
INCLUDES += -I/opt/csw/include/sasl/
AUXLIBS  += -lsasl2
BUILD_DEP_PKGS += CSWsasl-dev
RUNTIME_DEP_PKGS += CSWlibsasl2-2

# Activate support for OpenLDAP
# http://www.postfix.org/LDAP_README.html
FEATURES += -DHAS_LDAP
AUXLIBS  += -lldap -llber
BUILD_DEP_PKGS += CSWopenldap-dev
RUNTIME_DEP_PKGS += CSWlibldap2-4-2
RUNTIME_DEP_PKGS += CSWliblber2-4-2

# Activate support for MySQL
# http://www.postfix.org/MYSQL_README.html
FEATURES += -DHAS_MYSQL
INCLUDES += -I/opt/csw/include/mysql
AUXLIBS  += -L/opt/csw/lib -R/opt/csw/mysql5/lib/mysql
AUXLIBS  += -lmysqlclient
BUILD_DEP_PKGS += CSWmysql-dev
RUNTIME_DEP_PKGS += CSWlibmysqlclient18

# Activate support for PostgreSQL
# http://www.postfix.org/PGSQL_README.html
FEATURES += -DHAS_PGSQL
INCLUDES += -I/opt/csw/include/
AUXLIBS  += -L/opt/csw/lib/ -R/opt/csw/lib/
AUXLIBS  += -lpq
BUILD_DEP_PKGS += CSWpostgresql-dev
RUNTIME_DEP_PKGS += CSWlibpq5
endif

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Postgres package outdated, libs aren't located below /opt/csw/lib/
CHECKPKG_OVERRIDES_CSWpostfix += bad-rpath-entry

EXTRA_LD_OPTIONS = -Bdirect -z ignore

include gar/category.mk

# Postfix's build system relies on CCARGS, populate it with the defaults from
# GAR. For the bare-bones build don't leak anything located in */csw/* to the
# build (we want to rely on as little additional CSW pkgs as possible).
ifeq ($(BUILDTYPE),simple)
LD_OPTIONS  =
CCARGS      = $(CFLAGS)
CCARGS     += $(filter-out -I/opt/csw/include,$(CPPFLAGS))
CCARGS     += $(filter-out -I/opt/csw/%,$(INCLUDES))
CCARGS     += -DNO_PCRE         # on by default, would trigger our pcre-config
CCARGS     += $(DEFAULTS)
else
CCARGS=$(CFLAGS) $(CPPFLAGS) $(INCLUDES) $(FEATURES) $(DEFAULTS)
endif

# Postfix doesn't use autoconf, but it's own tool called makedefs. It's
# triggered by "gmake makefiles" in the source root and expects it's options
# via environment variables CC CCARGS AUXLIBS DEBUG OPT. For us there is no
# need to use DEBUG and OPT. The relevant flags are (amongst others) contained
# in GAR's CFLAGS which we already pushed into CCARGS (see above).
configure-custom:
	echo $(MAKE) -C $(WORKSRC) makefiles CC=$(CC) CCARGS='$(CCARGS)'
	$(MAKE) -C $(WORKSRC) makefiles \
		CC=$(CC) \
		CCARGS='$(CCARGS)' \
		AUXLIBS='$(AUXLIBS)' \
		DEBUG= \
		OPT=
	@$(MAKECOOKIE)

install-custom:
	$(MAKE) -C $(WORKSRC) non-interactive-package install_root=$(DESTDIR) \
		config_directory=$(DEF_CONFIG_DIR) \
		daemon_directory=$(DEF_DAEMON_DIR) \
		command_directory=$(DEF_COMMAND_DIR) \
		queue_directory=$(DEF_QUEUE_DIR) \
		sendmail_path=$(DEF_COMMAND_DIR)/sendmail \
		newaliases_path=$(DEF_NEWALIAS_PATH) \
		mailq_path=$(DEF_MAILQ_PATH) \
		manpage_directory=$(DEF_MANPAGE_DIR) \
		setgid_group=postdrop \
		sample_directory=/opt/csw/share/doc/postfix/samples \
		readme_directory=$(DEF_README_DIR) \
		html_directory=$(DEF_HTML_DIR)

	# Files for cswinitsmf and cswusergroup
	ginstall -Dm 755 $(FILEDIR)/cswpostfix  \
		$(DESTDIR)/etc/opt/csw/init.d/cswpostfix
	ginstall -D $(FILEDIR)/cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/CSWpostfix/cswusergroup

    # Helper script for spool location migration (2.4.x -> 2.6.x)
	ginstall -Dm 755 $(FILEDIR)/migrate-queuefiles.sh \
		$(DESTDIR)$(docdir)/$(NAME)/scripts/migrate-queuefiles.sh

	# Upgrade notice for users upgrading from the 2.4 package
	ginstall -Dm 644 $(FILEDIR)/README.upgradefrom.24 \
		$(DESTDIR)$(docdir)/$(NAME)/README.upgradefrom.24

	# Instructions to replace the system's sendmail
	ginstall -Dm 644 $(FILEDIR)/README.CSW \
		$(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@echo "===> Fixing /usr/local into /opt/csw"
	find $(DESTDIR)/$(DEF_HTML_DIR) -type f -depth -print | \
	   xargs -n 1 gsed -i -e 's|/usr/local|/opt/csw|g'
	find $(DESTDIR)/$(DEF_README_DIR) -type f -depth -print | \
	   xargs -n 1 gsed -i -e 's|/usr/local|/opt/csw|g'
	find $(DESTDIR)/$(DEF_DAEMON_DIR) -type f -name '*.cf' -depth -print | \
	   xargs -n 1 gsed -i -e 's|/usr/local|/opt/csw|g'
	find $(DESTDIR)/$(CONFIG_BASE) -type f -name '*.cf' -depth -print | \
	   xargs -n 1 gsed -i -e 's|/usr/local|/opt/csw|g'
	@$(MAKECOOKIE)

# Fails. A subsequent manual verify-config run is successfull,
# seems as if there might be some delay required.
#post-merge-modulated: verify-config

# Warn if there are any files in $(sysconfdir)/postfix which are not
# covered by cswsampleconf. This is a safety net in case new config file
# get introduced by more recent postfix versions. I know this runs for
# most bloated awkwardness. Feel free to trim it down.
#verify-config: SHIPPED_CFGFILES  = $(wildcard $(PKGROOT)$(CONFIG_BASE)*)
#verify-config: SHIPPED_CFGFILES := $(subst $(PKGROOT),,$(SHIPPED_CFGFILES))
#verify-config: IGNORE_FILES += /etc/opt/csw/postfix/bounce.cf.default
#verify-config: IGNORE_FILES += /etc/opt/csw/postfix/main.cf.default
#verify-config: IGNORE_FILES += $(addsuffix .CSW, $(SAMPLECONF))
#verify-config: SHELL=/bin/bash
#verify-config:
#	@echo "Checking for files in $(CONFIG_BASE) not covered by cswsampleconf"
#	@gdiff \
#		<( echo $(IGNORE_FILES) | tr " " "\n" | sort) \
#		<( echo $(SHIPPED_CFGFILES) | tr " " "\n" | sort )
#	@echo "OK