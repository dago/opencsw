GARNAME = httpd
GARVERSION = 2.2.13
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include ../../apache2/trunk/files/config.mk

# Apache worker MPM
CSWADMIN   = depend prototype postinstall postremove space
DISTFILES += $(call admfiles,CSWap2worker,$(CSWADMIN))
DISTFILES += CSWapache2.killproc

DEPENDS   += server/apache2

APACHE_ROOT = $(DESTDIR)$(prefix)/apache2

include gar/category.mk
include ../../apache2/trunk/files/rules.mk

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); \
	./buildconf)

# Build Configuration
CONFIGURE_ARGS += --with-mpm=worker

post-install-modulated: rename-httpd

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.worker ) ; \
	fi

