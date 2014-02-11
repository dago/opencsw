# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libgnomeprintui
VERSION = 2.18.6
GARTYPE = v2

DESCRIPTION = The GNOME 2 print UI library 
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/libgnomeprintui/$(basename $(VERSION))/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES += CSWlibgnomeprintui2-2-0
CATALOGNAME_CSWlibgnomeprintui2-2-0 = libgnomeprintui2_2_0
PKGFILES_CSWlibgnomeprintui2-2-0 += $(call baseisadirs,$(libdir),libgnomeprintui-2-2\.so\.0\.1\.0)
PKGFILES_CSWlibgnomeprintui2-2-0 += $(call baseisadirs,$(libdir),libgnomeprintui-2-2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgnomeprintui2-2-0 += $(DESCRIPTION), libgnomeprintui-2-2.so.0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgnomeprint
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomeprintui2-2-0 += CSWlibatk1-0-0

PACKAGES += CSWlibgnomeprintui-dev
CATALOGNAME_CSWlibgnomeprintui-dev = libgnomeprintui_dev
SPKG_DESC_CSWlibgnomeprintui-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibgnomeprintui-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgnomeprintui-dev += CSWlibgnomeprintui
RUNTIME_DEP_PKGS_CSWlibgnomeprintui-dev += CSWlibgnomeprintui2-2-0

PACKAGES += CSWlibgnomeprintui
CATALOGNAME_CSWlibgnomeprintui = libgnomeprintui
SPKG_DESC_CSWlibgnomeprintui += $(DESCRIPTION)
ARCHALL_CSWlibgnomeprintui = 1
RUNTIME_DEP_PKGS_CSWlibgnomeprintui += CSWlibgnomeprintui2-2-0
CHECKPKG_OVERRIDES_CSWlibgnomeprintui += surplus-dependency|CSWlibgnomeprintui2-2-0


EXTRA_CONFIGURE_ENV = PATH=/opt/csw/gnu:$(PATH)
EXTRA_LINKER_FLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

