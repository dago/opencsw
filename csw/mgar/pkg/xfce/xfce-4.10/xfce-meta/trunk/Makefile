# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce-meta
VERSION = 4.10
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce lightweight desktop environment, meta
define BLURB
  Xfce lightweight desktop environment, meta
endef

# Catalog description
PACKAGES = CSWxfcemeta

# Package description
SPKG_DESC_CSWxfcemeta       = $(DESCRIPTION)

ARCHALL_CSWxfcemeta     = 1

RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWgtkxfceengine
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibxfce4ui
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibxfce4util
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfce4appfinder
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfce4panel
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfce4session
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfce4settings
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfcedtlogin
# RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfcepowermanager
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWexo
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWgarcon
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfdesktop
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfconf
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfwm4
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWthunar
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWthunarvolman
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWtumbler

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = 

include gar/category.mk
