# pkg-config options
EXTRA_PKG_CONFIG_DIRS += /opt/csw/X11/lib

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

# Perhaps there is a category-level variable set?
EXTRA_INC += /opt/csw/X11/include
EXTRA_INC += /usr/X11/include
EXTRA_INC += /usr/openwin/share/include
EXTRA_LIB += /opt/csw/X11/lib

include gar/gar.mk
