NAME = libsoup
VERSION = 2.33.92
CATEGORIES = lib
GARTYPE = v2
  

DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PACKAGES  = CSWlibsoup2
PACKAGES  += CSWlibsoup2dev
SPKG_DESC_CSWlibsoup2 = HTTP client/server library for GNOME
SPKG_DESC_CSWlibsoup2dev = HTTP client/server library for GNOME, dev files

RUNTIME_DEP_PKGS_CSWlibsoup2 = CSWgconf2
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWgnutls
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWlibproxy
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWsqlite3rt

RUNTIME_DEP_PKGS_CSWlibsoup2dev += CSWlibsoup2


PKGFILES_CSWlibsoup2dev  = /opt/csw/lib/pkgconfig/.*
PKGFILES_CSWlibsoup2dev  += /opt/csw/include/.*


EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 
STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --disable-static 
CONFIGURE_ARGS += --disable-tls-check

# Test disabled because of missing Apache stuff
TEST_TARGET = 

include gar/category.mk
