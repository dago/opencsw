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
PACKAGES  += CSWlibsoup2dev
PACKAGES  += CSWlibsoup2gnome
PACKAGES  += CSWlibsoup2gnomedev
SPKG_DESC_CSWlibsoup2 = HTTP client/server library for GNOME
SPKG_DESC_CSWlibsoup2dev = HTTP client/server library for GNOME, dev files
SPKG_DESC_CSWlibsoup2gnome = HTTP client/server library for GNOME, gnome part 
SPKG_DESC_CSWlibsoup2gnomedev = HTTP client/server library for GNOME, gnome dev part

REQUIRED_PKGS_CSWlibsoup2gnome = CSWgconf2
REQUIRED_PKGS_CSWlibsoup2gnome += CSWgcrypt
REQUIRED_PKGS_CSWlibsoup2gnome += CSWggettextrt
REQUIRED_PKGS_CSWlibsoup2gnome += CSWglib2
REQUIRED_PKGS_CSWlibsoup2gnome += CSWgnutls
REQUIRED_PKGS_CSWlibsoup2gnome += CSWgpgerr
REQUIRED_PKGS_CSWlibsoup2gnome += CSWlibproxy
REQUIRED_PKGS_CSWlibsoup2gnome += CSWlibxml2
REQUIRED_PKGS_CSWlibsoup2gnome += CSWsqlite3rt

REQUIRED_PKGS_CSWlibsoup2gnome += CSWlibsoup2

REQUIRED_PKGS_CSWlibsoup2dev = CSWlibsoup2
REQUIRED_PKGS_CSWlibsoup2gnomedev = CSWlibsoup2gnome

REQUIRED_PKGS_CSWlibsoup2 = CSWgcrypt
REQUIRED_PKGS_CSWlibsoup2 += CSWggettextrt
REQUIRED_PKGS_CSWlibsoup2 += CSWglib2
REQUIRED_PKGS_CSWlibsoup2 += CSWgnutls
REQUIRED_PKGS_CSWlibsoup2 += CSWgpgerr
#REQUIRED_PKGS_CSWlibsoup2 += CSWlibproxy
REQUIRED_PKGS_CSWlibsoup2 += CSWlibxml2

REQUIRED_PKGS_CSWlibsoup2dev = CSWlibsoup2

PKGFILES_CSWlibsoup2  = /opt/csw/lib/libsoup-2.4.so.1.2.0
PKGFILES_CSWlibsoup2dev  = /opt/csw/lib/pkgconfig/libsoup-2.4.pc
PKGFILES_CSWlibsoup2dev  += /opt/csw/include/libsoup-2.4/.*
PKGFILES_CSWlibsoup2gnomedev = /opt/csw/lib/pkgconfig/libsoup-gnome-2.4.pc
PKGFILES_CSWlibsoup2gnomedev += /opt/csw/include/libsoup-gnome-2.4/.*



EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 
STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS) --disable-static --with-apache-httpd=/opt/csw/apache2/sbin/httpd --with-apache-module-dir=/opt/csw/apache2/libexec/

#TEST_TARGET = check
TEST_TARGET =

include gar/category.mk
