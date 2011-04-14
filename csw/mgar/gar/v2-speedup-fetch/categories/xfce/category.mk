# XFCE
XFCE_ROOT       = http://www.us.xfce.org
XFCE_VERSION   ?= 4.6.1
XFCE_MIRROR     = $(XFCE_ROOT)/archive/xfce-$(XFCE_VERSION)/src/

MASTER_SITES   ?= $(XFCE_MIRROR)
VERSION     ?= $(XFCE_VERSION)
PKGDIST        ?= $(NAME)-$(VERSION).tar.bz2
DISTFILES      += $(PKGDIST)

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

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/gar.mk
