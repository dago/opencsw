# XFCE
XFCE_ROOT      = http://www.us.xfce.org
XFCE_VERSION   = 4.4.0
XFCE_MIRROR    = $(XFCE_ROOT)/archive/xfce-$(XFCE_VERSION)/src/

MASTER_SITES ?= $(XFCE_MIRROR)
GARVERSION   ?= $(XFCE_VERSION)
PKGDIST      ?= $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES    += $(PKGDIST)

include ../../gar.mk

# Compiler options
CFLAGS   += -xlibmil
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS  += -L/opt/csw/lib -R/opt/csw/lib

# Configure common options
CONFIGURE_ARGS = --prefix=/opt/csw --disable-debug --enable-final --mandir=/opt/csw/share/man

# pkg-config
PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig
