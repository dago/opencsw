# Status
# - Build with all activated features completes, packaging completes
# - Beware: uses a modified GARv2 for USERGROUP=
#   http://lists.opencsw.org/pipermail/maintainers/2009-July/003143.html
# - Fixed bugs:
#   #3580 Not sun4m compatible 
#         $(CFLAGS) are now incorporated into $(CCARGS)
#   #3063 /opt/csw/libexec/postfix not stripped, takes ~30MB 
#         $(STRIP_DIRS) added to build description
#   #3017 Please depend against CSWpcrert instead of CSWpcre 
#   #2843 No cyrus-sasl support
#         Added cyrus SASL support, link postfix against the same 
#         bdb version that CSWsasl uses.
# - Moved queue and data dirs to /var/opt/csw (see DDEFs) as per standard
# - Integrated CSWcswclassutils for user/group creation, configuration
#   file handling, and SMF / init script support
# 
# TODO
# - Check remaining open bugs
# - Check sed main.cf script functionality
# - Check update script functionality, add handling for spool location change
# - Do we need to take care of file ownerships?
# - Does the currently available package preserve configuration files on
#   removal?
GARNAME = postfix
GARVERSION = 2.6.2
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

MASTER_SITES = ftp://ftp.porcupine.org/mirrors/postfix-release/official/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.postfix.org

# Conflicting files (bin/mailq and bin/sendmail) in sendmail
INCOMPATIBLE_PKGS = CSWsendmail

DISTFILES += CSWpostfix.cswusergroup
DISTFILES += CSWpostfix.postinstall
DISTFILES += CSWpostfix.postremove

# Tag files for cswclassutils
CONFIG_BASE  = /etc/opt/csw/postfix/
CONFIG_FILES  = access aliases canonical generic header_checks
CONFIG_FILES += main.cf master.cf relocated transport virtual

SAMPLECONF  = $(addprefix $(CONFIG_BASE), $(CONFIG_FILES))
INITSMF     = /etc/opt/csw/init.d/cswpostfix
USERGROUP   = $(sysconfdir)/pkg/CSWpostfix/cswusergroup

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
PREREQUISITE_PKGS += CSWpcre
REQUIRED_PKGS += CSWpcrert

# Activate support for hash and btree lookup tables
# http://www.postfix.org/DB_README.html
FEATURES += -DHAS_DB
INCLUDES += -I/opt/csw/bdb4/include
AUXLIBS  += -L/opt/csw/bdb4/lib -R/opt/csw/bdb4/lib -ldb-4
PREREQUISITE_PKGS += CSWbdb4
REQUIRED_PKGS += CSWbdb4

# Activate support for SSL/TLS
# http://www.postfix.org/TLS_README.html
FEATURES += -DUSE_TLS
AUXLIBS  += -lssl -lcrypto
PREREQUISITE_PKGS += CSWossldevel
REQUIRED_PKGS += CSWosslrt

# Activate support for Cyrus SASL (dovecot is incl. automatically)
# http://www.postfix.org/SASL_README.html
FEATURES += -DUSE_SASL_AUTH -DUSE_CYRUS_SASL
INCLUDES += -I/opt/csw/include/sasl/
AUXLIBS  += -lsasl2
PREREQUISITE_PKGS += CSWsasl
REQUIRED_PKGS += CSWsasl

# Activate support for OpenLDAP
# http://www.postfix.org/LDAP_README.html
FEATURES += -DHAS_LDAP
AUXLIBS  += -lldap -llber
PREREQUISITE_PKGS += CSWoldapdevel
REQUIRED_PKGS += CSWoldaprt

# Activate support for MySQL
# http://www.postfix.org/MYSQL_README.html
FEATURES += -DHAS_MYSQL
INCLUDES += -I/opt/csw/mysql5/include/mysql
AUXLIBS  += -L/opt/csw/mysql5/lib/mysql -R/opt/csw/mysql5/lib/mysql
AUXLIBS  += -lmysqlclient
PREREQUISITE_PKGS += CSWmysql5devel
REQUIRED_PKGS += CSWmysql5rt

# Activate support for PostgreSQL
# http://www.postfix.org/PGSQL_README.html
FEATURES += -DHAS_PGSQL
INCLUDES += -I/opt/csw/postgresql/include/
AUXLIBS  += -L/opt/csw/postgresql/lib/ -R/opt/csw/postgresql/lib/
AUXLIBS  += -lpq
PREREQUISITE_PKGS += CSWlibpq
REQUIRED_PKGS += CSWlibpq


# Make sure to include $(CFLAGS) so that we get sane defaults via GAR
CCARGS=$(CFLAGS) $(FEATURES) $(DEFAULTS) $(INCLUDES)

# We zero makedef's DEBUG and OPT, the relevant flags are set via GAR & CFLAGS
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

	# XXX: Needs to be checked/revised for current version
	sed -f $(FILEDIR)/fix_main.cf.sed $(DESTDIR)/etc/opt/csw/postfix/main.cf > $(WORKDIR)/main.cf
	cp $(WORKDIR)/main.cf $(DESTDIR)/etc/opt/csw/postfix/main.cf

	# Script to handle the sysconfdir location change /opt -> /etc
	# XXX: Needs to be checked and amended with /opt -> /var changes
	ginstall -D -m 755 $(FILEDIR)/upgrade \
		$(DESTDIR)/opt/csw/share/postfix/upgrade

	# Files for cswinitsmf and cswusergroup
	ginstall -Dm 755 $(FILEDIR)/cswpostfix  \
		$(DESTDIR)/etc/opt/csw/init.d/cswpostfix
	ginstall -D $(FILEDIR)/cswpostfix.xml \
		$(DESTDIR)/var/opt/csw/svc/manifest/network/cswpostfix.xml"
	ginstall -D $(FILEDIR)/CSWpostfix.cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/CSWpostfix/cswusergroup
	@$(MAKECOOKIE)
