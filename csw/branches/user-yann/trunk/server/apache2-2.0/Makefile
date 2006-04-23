GARNAME = httpd
GARVERSION = 2.0.55
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include files/config.mk

# Configuration Files
AP2_CONFIG = httpd.conf.tmpl ssl.conf.tmpl
AP2_RC     = cswapache2

# Apache template/layout files
DISTFILES += $(AP2_CONFIG) $(AP2_RC)
# Apache dummy toplevel package
DISTFILES += $(call admfiles,CSWapache2,$(ADMSTANDARD))
# Apache runtime
DISTFILES += $(call admfiles,CSWapache2rt,$(ADMSTANDARD))
# Apache server (core)
DISTFILES += $(call admfiles,CSWapache2c,$(ADMSTANDARD) space postinstall)
# Apache prefork MPM (default)
DISTFILES += $(call admfiles,CSWap2prefork,$(ADMFULLSTD))
# Apache manual
DISTFILES += $(call admfiles,CSWapache2-manual,$(ADMSTANDARD))
# Apache mod_suexec
DISTFILES += $(call admfiles,CSWap2suexec,$(ADMADDON))

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

include ../category.mk
include files/rules.mk

LIBS += -lnsl
export LIBS

post-install: install-httpd-conf fix-libtool

install-httpd-conf:
	@for file in $(AP2_CONFIG) ; do \
		install $(WORKDIR)/$$file $(DESTDIR)$(prefix)/apache2/etc ; \
	done
	install -d $(DESTDIR)/etc/init.d
	install $(WORKDIR)/$(AP2_RC) $(DESTDIR)/etc/init.d
	@$(MAKECOOKIE)

fix-libtool:
	@sed -i -e s,/export/home/comand/bin/sed,$(bindir)/gsed,g \
		$(DESTDIR)$(prefix)/apache2/share/build/libtool
	@$(MAKECOOKIE)

