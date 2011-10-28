MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

# Perhaps there is a category-level variable set?
EXTRA_INC += /usr/X11/include
EXTRA_INC += /usr/openwin/share/include

include gar/gar.mk
