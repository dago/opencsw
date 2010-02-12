# TODO (release-critical prefixed with !, non release-critical with *)
# ! Update to most recent postfix version (2.6.5 as of 13th Jan 2010)
# ! Build, install and test package (works? spool permissions ok?)
#   WRT to permissions, run "postfix set-permissions" and compare
# * Ship simple default configuration
#
# NICE TO KNOW
# - 2.4.6,REV=2008.05.28 preserves modified configuration files via
#   package-shipped CAS class csw_conf.
#
GARNAME = postfix
GARVERSION = 2.6.5
CATEGORIES = server

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
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE      = LICENSE TLS_LICENSE

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
INITSMF     = $(sysconfdir)/init.d/csw$(GARNAME)
USERGROUP   = $(sysconfdir)/pkg/CSW$(GARNAME)/cswusergroup

# For the sake of simplicity and user choice we dropped the automatic
# replacement of the /usr/{lib,bin} sendmail binaries. Ref.
# http://article.gmane.org/gmane.os.solaris.opencsw.maintainers/5313
POSTMSG     = POSTMSG = $(DOCDIR)/$(GARNAME)/README.upgradefrom.24

# Make postdrop setgid so that it can deliver to $(DEF_QUEUE_DIR)/maildrop
PROTOTYPE_MODIFIERS = makesgid
PROTOTYPE_FILES_makesgid = $(sbindir)/postdrop
PROTOTYPE_PERMS_makesgid = 2755

# Make $(DEF_QUEUE_DIR) subdirs accessible/writable to postfix only
PROTOTYPE_MODIFIERS += spooldir
PROTOTYPE_FILES_spooldir = $(DEF_QUEUE_DIR)/*
PROTOTYPE_USER_spooldir  = postfix
PROTOTYPE_PERMS_spooldir = 0700
PROTOTYPE_CLASS_spooldir = ugfiles

# Make $(DEF_QUEUE_DIR)/maildrop accessible by postdrop group
PROTOTYPE_MODIFIERS += maildrop
PROTOTYPE_FILES_maildrop = $(DEF_QUEUE_DIR)/maildrop
PROTOTYPE_GROUP_maildrop = postdrop
PROTOTYPE_PERMS_maildrop = 0730
PROTOTYPE_CLASS_maildrop = ugfiles

# IMPORTANT! Make $(DEF_QUEUE_DIR)/pid accessible by root only
# http://www.openwall.com/lists/oss-security/2009/09/18/6
PROTOTYPE_MODIFIERS += pid
PROTOTYPE_FILES_pid = $(DEF_QUEUE_DIR)/pid
PROTOTYPE_USER_pid  = root
PROTOTYPE_GROUP_pid = bin
PROTOTYPE_PERMS_pid = 0755
PROTOTYPE_CLASS_pid = ugfiles

EXTRA_MERGE_EXCLUDE_FILES  = /etc/opt/csw/postfix/LICENSE
EXTRA_MERGE_EXCLUDE_FILES += /etc/opt/csw/postfix/TLS_LICENSE
EXTRA_MERGE_EXCLUDE_FILES += /etc/opt/csw/postfix/makedefs.out

STRIP_DIRS = $(DESTDIR)$(libexecdir)/postfix

CONFIGURE_SCRIPTS = custom
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

include gar/category.mk

# Supporting documentation for building postfix
# - Postfix Installation From Source Code 
#   http://www.postfix.org/INSTALL.html
# - Guidelines for Package Builders
#   http://www.postfix.org/PACKAGE_README.html

DEF_COMMAND_DIR    = /opt/csw/sbin
DEF_CONFIG_DIR     = /etc/opt/csw/postfix
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

# Make sure libraries in the default location can be found
AUXLIBS = -L/opt/csw/lib

# Activate support for PCRE
# http://www.postfix.org/PCRE_README.html
FEATURES += -DHAS_PCRE
AUXLIBS  += -lpcre
BUILD_DEP_PKGS += CSWpcre
RUNTIME_DEP_PKGS += CSWpcrert

# Activate support for hash and btree lookup tables
# http://www.postfix.org/DB_README.html
FEATURES += -DHAS_DB
INCLUDES += -I/opt/csw/bdb42/include 
AUXLIBS  += -L/opt/csw/bdb42/lib -R/opt/csw/bdb42/lib -ldb-4.2
BUILD_DEP_PKGS += CSWbdb42devel
RUNTIME_DEP_PKGS += CSWbdb42

# Activate support for SSL/TLS
# http://www.postfix.org/TLS_README.html
FEATURES += -DUSE_TLS
AUXLIBS  += -lssl -lcrypto
BUILD_DEP_PKGS += CSWossldevel
RUNTIME_DEP_PKGS += CSWosslrt

# Activate support for Cyrus SASL (dovecot is incl. automatically)
# http://www.postfix.org/SASL_README.html
FEATURES += -DUSE_SASL_AUTH -DUSE_CYRUS_SASL
INCLUDES += -I/opt/csw/include/sasl/
AUXLIBS  += -lsasl2
BUILD_DEP_PKGS += CSWsasl
RUNTIME_DEP_PKGS += CSWsasl

# Activate support for OpenLDAP
# http://www.postfix.org/LDAP_README.html
FEATURES += -DHAS_LDAP
AUXLIBS  += -lldap -llber
BUILD_DEP_PKGS += CSWoldapdevel
RUNTIME_DEP_PKGS += CSWoldaprt

# Activate support for MySQL
# http://www.postfix.org/MYSQL_README.html
FEATURES += -DHAS_MYSQL
INCLUDES += -I/opt/csw/mysql5/include/mysql
AUXLIBS  += -L/opt/csw/mysql5/lib/mysql -R/opt/csw/mysql5/lib/mysql
AUXLIBS  += -lmysqlclient
BUILD_DEP_PKGS += CSWmysql5devel
RUNTIME_DEP_PKGS += CSWmysql5rt

# Activate support for PostgreSQL
# http://www.postfix.org/PGSQL_README.html
FEATURES += -DHAS_PGSQL
INCLUDES += -I/opt/csw/postgresql/include/
AUXLIBS  += -L/opt/csw/postgresql/lib/ -R/opt/csw/postgresql/lib/
AUXLIBS  += -lpq
BUILD_DEP_PKGS += CSWlibpq
RUNTIME_DEP_PKGS += CSWlibpq


# Make sure to include $(CFLAGS) so that we get sane defaults via GAR
CCARGS=$(CPPFLAGS) $(INCLUDES) $(FEATURES) $(DEFAULTS) $(CFLAGS)

# We zero makedef's DEBUG and OPT, the relevant flags are set via GAR & CFLAGS
configure-custom:
	echo $(MAKE) -C $(WORKSRC) makefiles CC=$(CC) CCARGS='$(CCARGS)'
	$(MAKE) -C $(WORKSRC) makefiles \
		CC=$(CC) \
		CCARGS='$(CCARGS)' \
		AUXLIBS='$(AUXLIBS)' \
		DEBUG= \
		OPT=
	@$(MAKECOOIE)

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
		$(DESTDIR)$(docdir)/$(GARNAME)/scripts/migrate-queuefiles.sh
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
#	@echo "OK"
#	@$(MAKECOOKIE)	
