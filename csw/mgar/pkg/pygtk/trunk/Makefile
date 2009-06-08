GARNAME = pygtk
GARVERSION = 2.14.1
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
REQUIRED_PKGS_CSWpygtk  = CSWpython 

CATALOGNAME_CSWpygtk = py_gtk
SPKG_DESC_CSWpygtk = pygtk support for Python

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2

#TEST_TARGET = check
TEST_SCRIPTS = 

include gar/category.mk

