NAME = pygtk
VERSION = 2.17.0
CATEGORIES = lang
GARTYPE = v2
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9].*\.[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = Python bindings for the GTK library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygtk/$(RELVER)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
STRIP_LIBTOOL = 1

PACKAGES = CSWpy-gtk
BUILD_DEP_PKGS = CSWpkgconfig CSWpygobject CSWlibglib2-dev CSWlibatk-dev CSWpangodevel CSWpycairo  CSWlibcairo-dev CSWlibxcbdevel
RUNTIME_DEP_PKGS_CSWpy-gtk  = CSWpython CSWfconfig CSWftype2 CSWggettextrt
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibglade2 CSWlibxml2 CSWpango

CATALOGNAME_CSWpy-gtk = py_gtk
SPKG_DESC_CSWpy-gtk = $(DESCRIPTION)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
RUNTIME_DEP_PKGS += CSWcswclassutils

# PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig
# EXTRA_EXPORTS = PKG_CONFIG_PATH

CONFIGURE_ARGS  = $(DIRPATHS)

#TEST_SCRIPTS = 

include gar/category.mk

