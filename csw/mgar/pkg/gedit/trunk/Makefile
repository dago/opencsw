# $Id: Makefile 16916 2012-01-26 13:25:13Z dmichelsen $
NAME = gedit
VERSION = 2.30.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The official GNOME text editor
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

# Old patch from Phil
PATCHFILES += 0001-Patch-from-Phil-to-add-ACCESSPERMS.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWgedit
RUNTIME_DEP_PKGS_CSWgedit += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWenchant
RUNTIME_DEP_PKGS_CSWgedit += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgedit += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgedit += CSWgtksourceview
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWpango
RUNTIME_DEP_PKGS_CSWgedit += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWfconfig
RUNTIME_DEP_PKGS_CSWgedit += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgedit += CSWlibatk1-0-0

# These are just docs
CHECKPKG_OVERRIDES_CSWgedit += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/gedit/gedit-gedit-document.html
CHECKPKG_OVERRIDES_CSWgedit += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/gedit/gedit-gedit-view.html
CHECKPKG_OVERRIDES_CSWgedit += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/gedit/gedit-gedit-utils.html

# There is one failing test, probably due to glib issues
SKIPTEST ?= 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
