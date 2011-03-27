# $Id$
NAME = proj
VERSION = 4.7.0
CATEGORIES = lib

GARTYPE = v2-defaultchange

DESCRIPTION = Cartographic Projections Library
define BLURB
The PROJ.4 Cartographic Projections library was originally written by Gerald Evenden then of the USGS.
endef

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(NAME)-datumgrid-1.5.zip

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWproj CSWproj-dev CSWlibproj0 CSWproj-data

CATALOGNAME_CSWproj = $(NAME)
SPKG_DESC_CSWproj = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWproj += CSWlibproj0
PKGFILES_CSWproj = $(bindir).* $(mandir)/man1.*

CATALOGNAME_CSWlibproj0 = libproj0
SPKG_DESC_CSWlibproj0 += Cartographic Projections Library, libproj.so.0
PKGFILES_CSWlibproj0 += $(call baseisadirs,$(libdir),libproj\.so\.0\.6\.6)
PKGFILES_CSWlibproj0 += $(call baseisadirs,$(libdir),libproj\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibproj0 = CSWproj-data
CHECKPKG_OVERRIDES_CSWlibproj0 += surplus-dependency|CSWproj-data

CATALOGNAME_CSWproj-dev = proj_dev
SPKG_DESC_CSWproj-dev = The development files for proj
RUNTIME_DEP_PKGS_CSWproj-dev += CSWlibproj0
PKGFILES_CSWproj-dev = $(PKGFILES_DEVEL)

CATALOGNAME_CSWproj-data = proj_data
ARCHALL_CSWproj-data = 1
SPKG_DESC_CSWproj-data = Data files used by $(NAME)
PKGFILES_CSWproj-data = /opt/csw/share/$(NAME)/.*

include gar/category.mk
