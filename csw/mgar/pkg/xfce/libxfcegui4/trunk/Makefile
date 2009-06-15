GARNAME = libxfcegui4
CATEGORIES = xfce

DESCRIPTION = Xfce Widget Library 
define BLURB
   Xfce Widget Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# Don't forget to add this after checking dependencies with panel CSWlibxfcegui4dep.preinstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Catalog description
PACKAGES = CSWlibxfcegui4 CSWlibxfcegui4dev CSWlibxfcegui4doc

CATALOGNAME_CSWlibxfcegui4 = libxfcegui4
CATALOGNAME_CSWlibxfcegui4dev = libxfcegui4dev
CATALOGNAME_CSWlibxfcegui4doc = libxfcegui4doc

# Package description
SPKG_DESC_CSWlibxfcegui4    = $(DESCRIPTION)
SPKG_DESC_CSWlibxfcegui4dev = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfcegui4doc = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWlibxfcegui4dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfcegui4dev += /opt/csw/include/xfce4/libxfcegui4/.*
PKGFILES_CSWlibxfcegui4doc  = /opt/csw/share/gtk-doc/.*

# Defines dependencies
REQUIRED_PKGS_CSWlibxfcegui4    = 
REQUIRED_PKGS_CSWlibxfcegui4dev = 
REQUIRED_PKGS_CSWlibxfcegui4doc = 

# BUILD64 = 1
# NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-xinerama

TEST_SCRIPTS = 

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/category.mk

