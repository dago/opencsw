# is obsoleted since CSWgobject 2.90.4 which presents a gtk+3 interface
NAME = pygtk
VERSION = 2.24.0
CATEGORIES = lang
GARTYPE = v2
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9].*\.[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = Python bindings for the GTK library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygtk/$(RELVER)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
SGARCOMPILER = GCC4
STRIP_LIBTOOL = 1

# mgar test fails with "GtkWarning: could not open display"
# however a gmake check works and finish successfull!
SKIPTEST = 1

PACKAGING_PLATFORMS=solaris10-i38
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWpython27-dev
BUILD_DEP_PKGS += CSWpy-gobject-devGS += CSWpygobject
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWpy-cairo
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibglade2
BUILD_DEP_PKGS += CSWpy-numpy
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibharfbuzz-dev
BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWlibxml2-dev += CSWlibxcbdevel

PACKAGES = CSWpy-gtk
CATALOGNAME_CSWpy-gtk = py_gtk
SPKG_DESC_CSWpy-gtk# OBSOLETED_BY_CSWpy-gtk = CSWpygtk
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibglade2CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWpygobject
RUNTIME_DEP_PKGS_CSWpy-gRUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-gtk += CSWlibpangocairo1-0-0
CHECKPKG_OVERRIDES_CSWpy-gtk += surplus-dependency|CSWpythongtk += CSWpy-cairo
CHECKPKG_OVERRIDES_CSWpy-gtk += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/pygtk/class-gtkfilechooser.html
CHECKPKG_OVERRIDES_CSWpy-gtk += file-with-bad-content|/usr/local|root/opt/csw/share/gtk-doc/html/pygtk/class-gtkrcstyle.html
# pygtk do not work without this
CHECKPKG_OVERRIDES_CSWpy-gtk += surplus-dependency|CSWpygobject
# gtk do not work without this
CHECKPKG_OVERRIDES_CSWpy-gtk += surplus-dependency|CSWpy-cairo

# pkg and classa# ction is obsolete
CHECKPKG_OVERRIDES_CSWpygtk += action-class-only-in-pkginfo|cswpycompile

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
RUNTIME_DEP_PKGS += CSWcswclassutils

# PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig
# EXTRA_EXPORTS = PKG_CONFIG_PATH

CONFIGURE_ARGS  = $(DIRPATHS)

#TEST_SCRIPTS = 

include