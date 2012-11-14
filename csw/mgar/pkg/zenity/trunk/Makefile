# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zenity
VERSION = 2.32.1
GARTYPE = v2

DESCRIPTION = Display graphical dialog boxes from shell scripts
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/gnome/sources/zenity/$(basename $(VERSION))/
DISTFILES  = $(DISTNAME).tar.bz2

REINPLACE_USRLOCAL = src/gdialog.in

GARCOMPILER = SOS12U3

# scrollkeeper is outdateded ? anyway it is an other product
EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/var/.*

RUNTIME_DEP_PKGS_CSWzenity += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWzenity += CSWlibintl8
RUNTIME_DEP_PKGS_CSWzenity += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWzenity += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWzenity += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWzenity += CSWlibgtk-x11-2-0-0

EXTRA_CONFIGURE_ENV += PATH=/opt/csw/gnu:$(PATH)
EXTRA_TEST_ENV += $(EXTRA_CONFIGURE_ENV)
EXTRA_INSTALL_ENV += $(EXTRA_CONFIGURE_ENV)
# scrollkeeper issue
SKIPTEST = 1

# because of missing libpng12.pc define it manualy
EXTRA_INC += /opt/csw/include/gtk-2.0
EXTRA_INC += /opt/csw/include/glib-2.0
EXTRA_INC += /opt/csw/lib/glib-2.0/include
EXTRA_INC += /opt/csw/lib/gtk-2.0/include
EXTRA_INC += /opt/csw/include/atk-1.0
EXTRA_INC += /opt/csw/include/pango-1.0
EXTRA_INC += /opt/csw/include/gdk-pixbuf-2.0
EXTRA_INC += /opt/csw/include/cairo
EXTRA_INC += /opt/csw/include/freetype2
EXTRA_INC += /opt/csw/include/libpng15
EXTRA_CFLAGS += -D_REENTRANT -D_PTHREADS

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

