GARNAME = httpd
GARVERSION = 2.0.55
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include ../apache2/files/config.mk

# Apache worker MPM
DISTFILES += CSWap2worker.gspec CSWap2worker.prototype CSWap2worker.depend
DISTFILES += CSWap2worker.preinstall CSWap2worker.postinstall
DISTFILES += CSWap2worker.preremove CSWap2worker.postremove
DISTFILES += CSWap2worker.space 

# Build Configuration
CONFIGURE_ARGS += --with-mpm=worker

include ../category.mk
include ../apache2/files/rules.mk

LIBS += -lnsl
export LIBS
