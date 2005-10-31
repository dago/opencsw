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
DISTFILES += CSWapache2.gspec CSWapache2.prototype CSWapache2.depend
# Apache runtime
DISTFILES += CSWapache2rt.gspec CSWapache2rt.prototype CSWapache2rt.depend
# Apache server (core)
DISTFILES += CSWapache2c.gspec CSWapache2c.prototype CSWapache2c.depend
DISTFILES += CSWapache2c.space CSWapache2c.postinstall
# Apache prefork MPM (default)
DISTFILES += CSWap2prefork.gspec CSWap2prefork.prototype CSWap2prefork.depend
DISTFILES += CSWap2prefork.preinstall CSWap2prefork.postinstall
DISTFILES += CSWap2prefork.preremove CSWap2prefork.postremove
DISTFILES += CSWap2prefork.space 
# Apache manual
DISTFILES += CSWapache2-manual.gspec CSWapache2-manual.prototype
DISTFILES += CSWapache2-manual.depend
# Apache mod_suexec
DISTFILES += CSWap2suexec.gspec CSWap2suexec.prototype CSWap2suexec.depend
DISTFILES += CSWap2suexec.postinstall CSWap2suexec.preremove

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

