# pkg-config options
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

# Perhaps there is a category-level variable set?
EXTRA_INC ?= /opt/csw/X11/include /usr/X11/include /usr/openwin/share/include
EXTRA_LIB ?= /opt/csw/X11/lib

include gar/gar.mk
