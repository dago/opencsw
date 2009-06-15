GARNAME = libxfce4menu
CATEGORIES = xfce

DESCRIPTION = Xfce Desktop Menu Library 
define BLURB
  libxfce4menu is a freedesktop.org compliant menu library written for Xfce. It implements the Desktop Menu Specification version 1.0
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Catalog description
PACKAGES = CSWlibxfce4menu CSWlibxfce4menudev CSWlibxfce4menudoc

CATALOGNAME_CSWlibxfce4menu = libxfce4menu
CATALOGNAME_CSWlibxfce4menudev = libxfce4menudev
CATALOGNAME_CSWlibxfce4menudoc = libxfce4menudoc

# Package description
SPKG_DESC_CSWlibxfce4menu    = $(DESCRIPTION)
SPKG_DESC_CSWlibxfce4menudev = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfce4menudoc = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWlibxfce4menudev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfce4menudev += /opt/csw/include/xfce4/libxfce4menu/.*
PKGFILES_CSWlibxfce4menudoc  = /opt/csw/share/gtk-doc/.*

# Defines dependencies
REQUIRED_PKGS_CSWlibxfce4menu    = CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWlibxfce4menudev = CSWlibxfce4menu
REQUIRED_PKGS_CSWlibxfce4menudoc = CSWlibxfce4menu

# BUILD64 = 1
# NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

MSGFMT = /opt/csw/bin/gmsgfmt
MSGMERGE = /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/category.mk

