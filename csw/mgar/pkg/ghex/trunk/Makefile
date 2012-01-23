# TODO (release-critical prefixed with !, non release-critical with *)
# ! Build fails
#   libtool: link: cannot find the library `/opt/csw/lib/libgconf-2.la' or unhandled argument `/opt/csw/lib/libgconf-2.la'
#
NAME = ghex
VERSION = 2.24.0
CATEGORIES = utils

DESCRIPTION = The GNOME binary hex editor
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.gz

PACKAGES += CSWghex
CATALOGNAME_CSWghex = ghex
SPKG_DESC_CSWghex = The GNOME binary hex editor
RUNTIME_DEP_PKGS_CSWghex += CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWghex += CSWbonobo2
RUNTIME_DEP_PKGS_CSWghex += CSWlibatk
RUNTIME_DEP_PKGS_CSWghex += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWghex += CSWglib2
RUNTIME_DEP_PKGS_CSWghex += CSWlibgnome
RUNTIME_DEP_PKGS_CSWghex += CSWlibgnomeprintui
RUNTIME_DEP_PKGS_CSWghex += CSWggettextrt
RUNTIME_DEP_PKGS_CSWghex += CSWfconfig
RUNTIME_DEP_PKGS_CSWghex += CSWgconf2
RUNTIME_DEP_PKGS_CSWghex += CSWorbit2
RUNTIME_DEP_PKGS_CSWghex += CSWlibpopt
RUNTIME_DEP_PKGS_CSWghex += CSWzlib
RUNTIME_DEP_PKGS_CSWghex += CSWftype2
RUNTIME_DEP_PKGS_CSWghex += CSWpango
RUNTIME_DEP_PKGS_CSWghex += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWghex += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWghex += CSWgtk2
RUNTIME_DEP_PKGS_CSWghex += CSWlibcairo
RUNTIME_DEP_PKGS_CSWghex += CSWlibxml2
RUNTIME_DEP_PKGS_CSWghex += CSWlibgnomeprint
RUNTIME_DEP_PKGS_CSWghex += CSWlibart

STRIP_LIBTOOL = 1

EXTRA_LINKER_FLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# GNU gettext required
PATH := $(prefix)/gnu:$(PATH)
