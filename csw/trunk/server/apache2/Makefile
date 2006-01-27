GARNAME = httpd
GARVERSION = 2.2.0
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include files/config.mk

# Dummy toplevel package
DISTFILES += $(call admfiles,CSWapache2,depend prototype)
# Runtime
DISTFILES += $(call admfiles,CSWapache2rt,depend prototype)
# Server (core)
CSWapache2c_admfiles = depend prototype postinstall space
DISTFILES += $(call admfiles,CSWapache2c,$(CSWapache2c_admfiles))
# Prefork MPM (default)
CSWap2prefork_admfiles  = depend prototype preinstall postinstall
CSWap2prefork_admfiles += preremove postremove space
DISTFILES += $(call admfiles,CSWap2prefork,$(CSWap2prefork_admfiles))
# mod_suexec
CSWap2suexec_admfiles = depend prototype postinstall preremove
DISTFILES += $(call admfiles,CSWap2suexec,$(CSWap2suexec_admfiles))
# Manual
DISTFILES += $(call admfiles,CSWapache2-manual,depend prototype)
# Development support
DISTFILES += $(call admfiles,CSWapache2-devel,depend prototype)

# Configuration templates
DISTFILES += cswapache2 httpd.conf.tmpl httpd-ssl.conf.tmpl
DISTFILES += update20to22

#DEPENDS += lib/apr-util

# Build Configuration
CONFIGURE_ARGS += --with-mpm=prefork
CONFIGURE_ARGS += --enable-suexec
CONFIGURE_ARGS += --with-suexec-caller=nobody
CONFIGURE_ARGS += --with-suexec-docroot=$(prefix)/apache2/share/htdocs
CONFIGURE_ARGS += --with-suexec-userdir=public_html
CONFIGURE_ARGS += --with-suexec-uidmin=100
CONFIGURE_ARGS += --with-suexec-gidmin=100
CONFIGURE_ARGS += --with-suexec-logfile=$(prefix)/apache2/var/log/suexec_log
CONFIGURE_ARGS += --with-suexec-bin=$(prefix)/apache2/sbin/suexec

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

include ../category.mk
include files/rules.mk

post-install: fix-config-vars copy-local-files 
	@$(MAKECOOKIE)

copy-local-files:
	@install -d $(DESTDIR)/etc/init.d
	@install $(WORKDIR)/cswapache2 $(DESTDIR)/etc/init.d
	@install $(WORKDIR)/httpd.conf.tmpl $(APACHE_ROOT)/etc
	@install $(WORKDIR)/httpd-ssl.conf.tmpl $(APACHE_ROOT)/etc/extra
	@install $(WORKDIR)/update20to22 $(APACHE_ROOT)/sbin

fix-config-vars:
	@replacer $(DESTDIR)

