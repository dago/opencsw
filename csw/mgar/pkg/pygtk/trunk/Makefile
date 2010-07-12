GARNAME = pygtk
GARVERSION = 2.17.0
CATEGORIES = lang
RELVER = $(shell echo $(GARVERSION) |gsed 's/\(^[0-9].*\.[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = pygtk support for Python
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygtk/$(RELVER)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
STRIP_LIBTOOL = 1

PACKAGES = CSWpygtk
BUILD_DEP_PKGS = CSWpkgconfig CSWpygobject CSWglib2devel CSWlibatkdevel CSWpangodevel CSWpycairo CSWlibcairodevel CSWlibxcbdevel
RUNTIME_DEP_PKGS_CSWpygtk  = CSWpython CSWfconfig CSWftype2 CSWggettextrt
RUNTIME_DEP_PKGS_CSWpygtk += CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo
RUNTIME_DEP_PKGS_CSWpygtk += CSWlibglade2 CSWlibxml2 CSWpango

CATALOGNAME_CSWpygtk = pygtk
SPKG_DESC_CSWpygtk = pygtk support for Python

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
RUNTIME_DEP_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2

PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig
EXTRA_EXPORTS = PKG_CONFIG_PATH

CONFIGURE_ARGS  = $(DIRPATHS)

TEST_TARGET = check
#TEST_SCRIPTS = 

include gar/category.mk

