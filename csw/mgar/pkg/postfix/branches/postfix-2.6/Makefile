# Status
# - Basic configuration, build completes, packaging not yet tested
# - Beware: uses a modified GARv2 for USERGROUP=
# TODO
# - Check open bugs
# - Activate features (SSL, LDAP, *SQL, ...)
# - Integrate the manifest from files/ with cswinitsmf
# - Check sed main.cf script functionality, do we need this?
# - Check update script functionality, add handling for spool location change
# - See how the csw_conf_config for cfg files was handled in gar v1
#   Does the currently available package preserve configuration files on
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
SPKG_SOURCEURL = http://www.postfix.org

DISTFILES += CSWpostfix.cswusergroup
DISTFILES += CSWpostfix.postinstall
DISTFILES += CSWpostfix.postremove
#DISTFILES += cswpostfix.xml

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWpcre
REQUIRED_PKGS = CSWpcrert

# Tag files for cswclassutils
CONFIG_BASE  = /etc/opt/csw/postfix/
CONFIG_FILES  = access aliases canonical generic header_checks
CONFIG_FILES += main.cf master.cf
CONFIG_FILES += relocated transport virtual

SAMPLECONF  = $(prefix $(CONFIG_BASE), $(CONFIG_FILES))
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

CCARGS=$(CFLAGS) $(DEFAULTS)

# We zero makedef's DEBUG and OPT, the relevant flags are set via GAR & CFLAGS
configure-custom:
	echo $(MAKE) -C $(WORKSRC) makefiles CC=$(CC) CCARGS='$(CCARGS)' DEBUG= OPT=
	$(MAKE) -C $(WORKSRC) makefiles \
		CC=$(CC) \
		CCARGS='$(CCARGS)' \
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

	# mv configuration files to .CSW
	$(foreach F,$(prefix $(DESTDIR),$(SAMPLECONF)), mv $(F) $(F).CSW;)

	# Script to handle the sysconfdir location change /opt -> /etc
	# XXX: Needs to be checked and amended with /opt -> /var changes
	ginstall -D -m 755 $(FILEDIR)/upgrade \
		$(DESTDIR)/opt/csw/share/postfix/upgrade

	# Files for cswinitsmf and cswusergroup
	ginstall -Dm 755 $(FILEDIR)/cswpostfix  \
		$(DESTDIR)/etc/opt/csw/init.d/cswpostfix
	ginstall -D $(FILEDIR)/CSWpostfix.cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/CSWpostfix/cswusergroup
	@$(MAKECOOKIE)
