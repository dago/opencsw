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
PACKAGES = CSWlibxfcegui4 CSWlibxfcegui4devel CSWlibxfcegui4doc

CATALOGNAME_CSWlibxfcegui4      = libxfcegui4
CATALOGNAME_CSWlibxfcegui4devel = libxfcegui4_devel
CATALOGNAME_CSWlibxfcegui4doc   = libxfcegui4_doc

# Package description
SPKG_DESC_CSWlibxfcegui4      = $(DESCRIPTION)
SPKG_DESC_CSWlibxfcegui4devel = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfcegui4doc   = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWlibxfcegui4devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfcegui4devel += /opt/csw/include/xfce4/libxfcegui4/.*
PKGFILES_CSWlibxfcegui4doc    = /opt/csw/share/gtk-doc/.*

# Defines dependencies
REQUIRED_PKGS_CSWlibxfcegui4      = CSWdbusglib CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo
REQUIRED_PKGS_CSWlibxfcegui4     += CSWlibdbus CSWlibglade2 CSWlibxfce4util CSWlibxml2 CSWpango
REQUIRED_PKGS_CSWlibxfcegui4     += CSWstartupnotif CSWxfconf CSWfconfig
REQUIRED_PKGS_CSWlibxfcegui4     += CSWftype2
REQUIRED_PKGS_CSWlibxfcegui4     += CSWsunmath

REQUIRED_PKGS_CSWlibxfcegui4devel = 
REQUIRED_PKGS_CSWlibxfcegui4doc   = 

# BUILD64 = 1
# NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-xinerama

LDFLAGS  += -lm

TEST_SCRIPTS = 

include gar/category.mk

