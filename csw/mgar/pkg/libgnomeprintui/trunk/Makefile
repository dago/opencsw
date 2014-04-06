# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libgnomeprintui
VERSION = 2.12.1
GARTYPE = v2

DESCRIPTION = The GNOME 2 print UI library

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/libgnomeprintui/$(basename $(VERSION))/
DISTFILES  = $(DISTNAME).tar.gz

UFILES_REGEX = href=\"(\d+(?:\.\d+)*)/\"
UPSTREAM_MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/libgnomeprintui/

BUILD_DEP_PKGS = CSWfontconfig-dev
# TODO: Add more *-dev packages. Maybe we should have some automation which
# would detect which *-dev packages to add?

PACKAGES += CSWlibgnomeprintui2-2-0
PKGFILES_CSWlibgnomeprintui2-2-0 += $(call baseisadirs,$(libdir),libgnomeprintui-2-2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgnomeprintui2-2-0 += $(DESCRIPTION), libgnomeprintui-2-2.so.0

RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += $(RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0_$(GARCH))

RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgnomeprint
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibintl8

PACKAGES += CSWlibgnomeprintui-dev
SPKG_DESC_CSWlibgnomeprintui-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibgnomeprintui-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgnomeprintui-dev += CSWlibgnomeprintui2-2-0

OBSOLETED_BY_CSWlibgnomeprintui2-2-0 = CSWlibgnomeprintui

EXTRA_CONFIGURE_ENV = PATH=/opt/csw/gnu:$(PATH)
EXTRA_LINKER_FLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

STRIP_LIBTOOL = 1

include gar/category.mk

