# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtk-engines
VERSION = 2.20.2
GARTYPE = v2

DESCRIPTION = Brief description

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparc

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += LIBS=-lm
CONFIGURE_ARGS += --enable-static=no

SKIPTEST = 1

PACKAGES = CSWgtkengines
CATALOGNAME_CSWgtkengines = gtk_engines
CHECKPKG_OVERRIDES_CSWgtkengines += catalogname-does-not-match-pkgname|pkgname=CSWgtkengines|catalogname=gtk_engines|expected-catalogname=gtkengines

RDEP_PKGS_CSWgtkengines_5.9 += CSWglib2
RDEP_PKGS_CSWgtkengines_5.9 += CSWgtk2
RDEP_PKGS_CSWgtkengines_5.9 += CSWlibcairo2

RDEP_PKGS_CSWgtkengines_5.10 += CSWlibgdk-x11-2-0-0
RDEP_PKGS_CSWgtkengines_5.10 += CSWlibgdk-pixbuf2-0-0
RDEP_PKGS_CSWgtkengines_5.10 += CSWlibcairo2
RDEP_PKGS_CSWgtkengines_5.10 += CSWlibgobject2-0-0
RDEP_PKGS_CSWgtkengines_5.10 += CSWlibglib2-0-0
RDEP_PKGS_CSWgtkengines_5.10 += CSWlibgtk-x11-2-0-0

RUNTIME_DEP_PKGS_CSWgtkengines += $(RDEP_PKGS_CSWgtkengines_$(GAROSREL))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
