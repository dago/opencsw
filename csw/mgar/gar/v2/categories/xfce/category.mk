# XFCE
XFCE_ROOT       = http://www.us.xfce.org
XFCE_VERSION   ?= 4.6.1
XFCE_MIRROR     = $(XFCE_ROOT)/archive/xfce-$(XFCE_VERSION)/src/

MASTER_SITES   ?= $(XFCE_MIRROR)
GARVERSION     ?= $(XFCE_VERSION)
PKGDIST        ?= $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES      += $(PKGDIST)

include gar/gar.mk

# Compiler options
# Compiler options
CFLAGS   += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/xfce4 
LDFLAGS  += -L/opt/csw/lib -R/opt/csw/lib

# pkg-config options
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

# Configure common options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --enable-final
CONFIGURE_ARGS += --enable-xinerama
CONFIGURE_ARGS += --enable-dbus
