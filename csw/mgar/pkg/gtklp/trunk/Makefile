# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtklp
VERSION = 1.2.9
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = GTK Gui for CUPS
define BLURB
  Gtk-Interface for CUPS Client with theme-support, IPP support, Printer specific options, all standard-cups options
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).src.tar.gz

GARCOMPILER = SOS12U3

BUILD_DEP_PKGS += CSWlibkr5-dev
BUILD_DEP_PKGS += CSWlibgnutls-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev

RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibcups2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-forte 

include gar/category.mk

