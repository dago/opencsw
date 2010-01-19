GARNAME = libsoup
GARVERSION = 2.26.3
CATEGORIES = lib
  

DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PACKAGES  = CSWlibsoup2


EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 

CONFIGURE_ARGS = $(DIRPATHS) --disable-static --with-apache-httpd=/opt/csw/apache2/sbin/httpd --with-apache-module-dir=/opt/csw/apache2/libexec/

TEST_TARGET = check

include gar/category.mk
