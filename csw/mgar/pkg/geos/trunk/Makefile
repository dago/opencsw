# $Id$
NAME = geos
VERSION = 3.2.2
CATEGORIES = lib

DESCRIPTION = Geometry Engine, Open Source
define BLURB
GEOS (Geometry Engine - Open Source) is a C++ port of the  Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the  OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.
endef

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.bz2

GARTYPE = v2-defaultchange

GARCOMPILER = GNU

PACKAGES += CSWgeos
PACKAGES += CSWlibgeos3-2-2
PACKAGES += CSWlibgeos-c1
PACKAGES += CSWgeos-dev

CATALOGNAME_CSWgeos = geos
SPKG_DESC_CSWgeos = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgeos += CSWlibgeos3-2-2
RUNTIME_DEP_PKGS_CSWgeos += CSWlibgeos-c1

CATALOGNAME_CSWlibgeos3-2-2 = libgeos3_2_2
SPKG_DESC_CSWlibgeos3-2-2 += $(DESCRIPTION), libgeos-3.2.2.so
PKGFILES_CSWlibgeos3-2-2 += $(call baseisadirs,$(libdir),libgeos-3\.2\.2\.so)
PKGFILES_CSWlibgeos3-2-2 += $(call baseisadirs,$(libdir),libgeos-3\.2\.2\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos3-2-2 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibgeos3-2-2 += CSWgcc4corert

CATALOGNAME_CSWlibgeos-c1 = libgeos_c1
SPKG_DESC_CSWlibgeos-c1 += Geometry Engine, Open Source, libgeos_c.so.1
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),libgeos_c\.so\.1\.6\.2)
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),libgeos_c\.so\.1(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibgeos3-2-2
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWgcc4corert

CATALOGNAME_CSWgeos-dev = geos_dev
SPKG_DESC_CSWgeos-dev = $(DESCRIPTION), development files
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgeos-dev = CSWlibgeos3-2-2 CSWlibgeos-c1

include gar/category.mk
