NAME = libbonoboui
VERSION = 2.24.5
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = UI code for the GNOME 2 Object Activation Framework
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibart
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibbonoboui += CSWlibatk1-0-0


CHECKPKG_OVERRIDES_CSWlibbonoboui += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libbonoboui-2.so
CHECKPKG_OVERRIDES_CSWlibbonoboui += shared-lib-pkgname-mismatch|file=opt/csw/lib/libbonoboui-2.so.0.0.0|soname=libbonoboui-2.so.0|pkgname=CSWlibbonoboui|expected=CSWlibbonoboui2-0

# There is a problem with the 64 bits build and the
# the previous package didn't have the 64 bits libraries
# so we disable this for now
#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --enable-static=no
#CONFIGURE_ARGS += --enable-gtk-doc

EXTRA_LD_OPTIONS = -z ignore -Bdirect

EXTRA_TEST_EXPORTS = DISPLAY
TEST_SCRIPTS = 

include gar/category.mk

# For GNU gettext
CONFIGURE_ENV += XGETTEXT=/opt/csw/gnu/xgettext
CONFIGURE_ENV += MSGMERGE=/opt/csw/gnu/msgmerge
CONFIGURE_ENV += MSGFMT=/opt/csw/gnu/msgfmt

