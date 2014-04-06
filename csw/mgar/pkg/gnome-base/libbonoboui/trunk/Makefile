NAME = libbonoboui
VERSION = 2.24.5
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = UI code for the GNOME 2 Object Activation Framework

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWlibbonoboui2-0
SPKG_DESC_CSWlibbonoboui2-0 += $(DESCRIPTION), libbonoboui-2.so.0
OBSOLETED_BY_CSWlibbonoboui2-0 = CSWlibbonoboui

RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbonoboui2-0 += CSWorbit2

PACKAGES += CSWlibbonoboui-dev
SPKG_DESC_CSWlibbonoboui-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibbonoboui-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibbonoboui2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbonoboui-dev += CSWorbit2

# There is a problem with the 64 bits build and the
# the previous package didn't have the 64 bits libraries
# so we disable this for now
#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --enable-static=no
#CONFIGURE_ARGS += --enable-gtk-doc

EXTRA_TEST_EXPORTS = DISPLAY
TEST_SCRIPTS =

include gar/category.mk

# For GNU gettext
CONFIGURE_ENV += XGETTEXT=/opt/csw/gnu/xgettext
CONFIGURE_ENV += MSGMERGE=/opt/csw/gnu/msgmerge
CONFIGURE_ENV += MSGFMT=/opt/csw/gnu/msgfmt

