# $Id$
NAME = proj
VERSION = 4.8.0

GARTYPE = v2
GARCOMPILER = GNU

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386lib

GARTYPE = v2

DESCRIPTION = Cartographic Projections Library
define BLURB
The PROJ.4 Cartographic Projections library was originally written by Gerald Evenden then of the USGS.
endef

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(NAME)-datumgrid = 1RGS = $(DIRPATHS)

PACKAGES = CSWproj CSWproj-dev CSWlibproj0 CSWproj-data

CATALOGNAME_CSWproj = $(NAME)
SPKG_DESC_CSWproj = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWproj += CSWlibproj0
PKGFILES_CSWproj = $(bindir).* $(mandir)/man1.*

CATALOGNAME_CSWlibproj0 = libproj0
SPKG_DESC_CSWlibproj0 += Cartographic Projections Library, libproj.so.0
PKGFILES_CSWlibproj0 += $(call baseisadirs,$(libdir)7\.0proj\.so\.0\.6\.6)
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
PKGFILES_CSWproj-data = /opt/csw/sCONFIGURE_ARGS  = $(DIRPATHS)

CONFIGURE_ARGS += --without-jni/share/$(NAME)/.*

include gar/category.mk

zip-extract-proj-datumgrid-1.5.zip:
	@(unzip -d $(WORKSRC)/nad $(DOWNLOADDIR)/proj-datumgrid-1.5.zip)