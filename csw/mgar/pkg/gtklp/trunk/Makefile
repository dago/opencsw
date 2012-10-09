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
PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386

BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWlibgnutls-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev

RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWpango
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtklp += CSWlibgnutls26

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-forte 

include gar/category.mk

