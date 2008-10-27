GARNAME = httpd
GARVERSION = 2.2.10
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include ../apache2/files/config.mk

# Apache worker MPM
CSWADMIN   = depend prototype postinstall postremove space
DISTFILES += $(call admfiles,CSWap2worker,$(CSWADMIN))
DISTFILES += CSWapache2.killproc

DEPENDS   += server/apache2

APACHE_ROOT = $(DESTDIR)$(prefix)/apache2

# Build Configuration
CONFIGURE_ARGS += --with-mpm=worker

include ../category.mk
include ../apache2/files/rules.mk

post-install: rename-httpd

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.worker ) ; \
	fi

