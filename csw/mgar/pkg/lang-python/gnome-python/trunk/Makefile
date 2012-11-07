# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnome-python
VERSION = 2.28.1
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.gnome.org/pub/gnome/sources/gnome-python/$(basename $(VERSION))/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWlibgnome-dev
BUILD_DEP_PKGS += CSWlibpopt-dev
PACKAGING_PLATFORMS += Solaris10-sparc Solaris10-i386

EXTRA_MERGE_EXCLUDE_FILES +=  .*/.*\.py[co]

PACKAGES += CSWpy-gnome
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWorbit2
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWpango
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibart
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWpy-gnome += CSWlibgio2-0-0

EXTRA_LINKER_FLAGS += -lgobject-2.0 # is missing in glib-2.0.pc ?

CONFIGURE_ARGS = $(DIRPATHS)

SKIPTEST = 1

include gar/category.mk

