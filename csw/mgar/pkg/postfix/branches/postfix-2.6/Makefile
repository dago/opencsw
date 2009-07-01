# TODO
# - Integrate the manifest with cswinitsmf
# - Understand what the sed main.cf script is doing
# - Build scripts to handle the spool location change
# - Check open bugs
# - Read postfix build instructions and verify CSW flags/lib/...
# - See how the csw_conf_config for cfg files was handled in gar v1
GARNAME = postfix
GARVERSION = 2.6.2
CATEGORIES = server

DESCRIPTION = Postfix aims to be an alternative to the widely-used sendmail program
define BLURB
What is Postfix? It is Wietse Venema's mailer that started life as an 
alternative to the widely-used Sendmail program. 

Postfix attempts to be fast, easy to administer, and secure, while at the same 
time being sendmail compatible enough to not upset existing users. Thus, the 
outside has a sendmail-ish flavor, but the inside is completely different.
endef

MASTER_SITES = http://mirrors.isc.org/pub/postfix/official/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
SPKG_SOURCEURL = http://www.postfix.org

DISTFILES += CSWpostfix.cswusergroup
DISTFILES += CSWpostfix.postinstall
DISTFILES += CSWpostfix.postremove
#DISTFILES += cswpostfix.xml

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWbdb4 CSWmysql4devel CSWlibpq CSWossldevel CSWoldapdevel
REQUIRED_PKGS = CSWbdb3 CSWlibpq CSWmysql4rt CSWoldaprt CSWosslrt CSWpcrert
REQUIRED_PKGS += CSWsasl CSWzlib

SPKG_CLASSES = none cswusergroup cswcpsampleconf cswinitsmf

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

CONFIG_BASE = \/etc\/opt\/csw\/postfix\/
CONFIG_FILES = access aliases canonical generic header_checks
CONFIG_FILES += main.cf master.cf
CONFIG_FILES += relocated transport virtual

PROTOTYPE_FILTER  = awk '\
	$(foreach C,$(prefix $(CONFIG_BASE),$(CONFIG_FILES)), \
		$$$$3 ~ /^$(C)$$$$/ { $$$$2 = "cswcpsampleconf" }) \
	$$$$3 ~ /^\/etc\/default\/cswpostgrey$$$$/ { $$$$2 = "cswcpsampleconf" } \
	$$$$3 ~ /\/init.d\/cswpostfix$$$$/ { $$$$2 = "cswinitsmf" } \
	$$$$3 ~ /cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
	 { print }'

include gar/category.mk

DEF_COMMAND_DIR    = /opt/csw/sbin
DEF_CONFIG_DIR     = /etc/opt/csw/postfix
DEF_DAEMON_DIR     = /opt/csw/libexec/postfix
DEF_MAILQ_PATH     = /opt/csw/bin/mailq
DEF_HTML_DIR       = yes
DEF_MANPAGE_DIR    = /opt/csw/man
DEF_NEWALIAS_PATH  = /opt/csw/bin/newaliases
DEF_QUEUE_DIR      = /var/opt/csw/spool/postfix
DEF_README_DIR     = yes

FLAGS=\
	-DUSE_TLS \
	-DUSE_SASL_AUTH \
	-DHAS_LDAP \
	-DHAS_PCRE \
	-DHAS_MYSQL \
	-DHAS_PGSQL \
	-DHAS_DB \
	-DUSE_CYRUS_SASL 

DEFAULTS=\
	-DDEF_MANPAGE_DIR=\"$(DEF_MANPAGE_DIR)\" \
	-DDEF_COMMAND_DIR=\"$(DEF_COMMAND_DIR)\" \
	-DDEF_CONFIG_DIR=\"$(DEF_CONFIG_DIR)\" \
	-DDEF_DAEMON_DIR=\"$(DEF_DAEMON_DIR)\" \
	-DDEF_MAILQ_PATH=\"$(DEF_MAILQ_PATH)\" \
	-DDEF_HTML_DIR=\"$(DEF_HTML_DIR)\" \
	-DDEF_NEWALIAS_PATH=\"$(DEF_NEWALIAS_PATH)\" \
	-DDEF_QUEUE_DIR=\"$(DEF_QUEUE_DIR)\" \
	-DDEF_README_DIR=\"$(DEF_README_DIR)\"

INCLUDES=\
	-I/opt/csw/include \
	-I/opt/csw/include/openssl \
	-I/opt/csw/include/sasl \
	-I/opt/csw/mysql4/include/mysql \
	-I/opt/csw/postgresql/include \
	-I/opt/csw/bdb4/include

AUXLIBS=\
	-R/opt/csw/lib \
	-R/opt/csw/lib/sasl2 \
	-R/opt/csw/mysql4/lib/mysql \
	-R/opt/csw/postgresql/lib \
	-R/opt/csw/bdb4/lib \
	-L/opt/csw/lib \
	-L/opt/csw/lib/sasl2 \
	-L/opt/csw/mysql4/lib/mysql \
	-L/opt/csw/postgresql/lib \
	-L/opt/csw/bdb4/lib \
	-lssl -lcrypto -lsasl2 -lldap -llber -lpcre -lmysqlclient -lz -lm -lpq -ldb

CCARGS=$(FLAGS) $(DEFAULTS) $(INCLUDES)

configure-custom:
	echo $(MAKE) -C $(WORKDIR)/$(DISTNAME) makefiles CC=$(CC_HOME)/bin/$(CC) CCARGS=$(CCARGS)
	$(MAKE) -C $(WORKDIR)/$(DISTNAME) makefiles CC=$(CC_HOME)/bin/$(CC) CCARGS='$(CCARGS)' AUXLIBS='$(AUXLIBS)'
	@$(MAKECOOKIE)
# CC=compiler OPT=compiler-flags DEBUG=debug-flags

build-custom:
	$(MAKE) -C $(WORKDIR)/$(DISTNAME)
	@$(MAKECOOKIE)

# Files that will be copied to .CSW files
install-custom: TEMPLATE_FILES = access aliases canonical generic header_checks
install-custom: TEMPLATE_FILES += main.cf master.cf relocated transport virtual
install-custom:
	$(MAKE) -C $(WORKDIR)/$(DISTNAME) non-interactive-package install_root=$(DESTDIR) \
		config_directory=$(DEF_CONFIG_DIR) \
		daemon_directory=$(DEF_DAEMON_DIR) \
		command_directory=$(DEF_COMMAND_DIR) \
		queue_directory=$(DEF_QUEUE_DIR) \
		sendmail_path=$(DEF_COMMAND_DIR)/sendmail \
		newaliases_path=$(DEF_NEWALIAS_PATH) \
		mailq_path=$(DEF_MAILQ_PATH) \
		manpage_directory=/opt/csw/share/man \
		setgid_group=postdrop \
		sample_directory=/opt/csw/share/doc/postfix/samples \
		readme_directory=/opt/csw/share/doc/postfix/README_FILES \
		html_directory=/opt/csw/share/doc/postfix/html
	sed -f $(FILEDIR)/fix_main.cf.sed $(DESTDIR)/etc/opt/csw/postfix/main.cf > $(WORKDIR)/main.cf
	cp $(WORKDIR)/main.cf $(DESTDIR)/etc/opt/csw/postfix/main.cf
	for file in $(TEMPLATE_FILES); do \
		cp $(DESTDIR)/etc/opt/csw/postfix/$$file $(DESTDIR)/etc/opt/csw/postfix/$$file.CSW; \
	done
	rm \
		$(DESTDIR)/etc/opt/csw/postfix/LICENSE \
		$(DESTDIR)/etc/opt/csw/postfix/TLS_LICENSE \
		$(DESTDIR)/etc/opt/csw/postfix/makedefs.out
	mkdir -p $(DESTDIR)/opt/csw/share/postfix
	cp $(FILEDIR)/upgrade $(DESTDIR)/opt/csw/share/postfix/upgrade

	# Files for cswinitsmf and cswusergroup
	ginstall -m 755 $(FILEDIR)/cswpostfix  \
		$(DESTDIR)/etc/opt/csw/init.d/cswpostfix
	cp $(FILEDIR)/CSWpostfix.cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/CSWpostfix/cswusergroup
	@$(MAKECOOKIE)
