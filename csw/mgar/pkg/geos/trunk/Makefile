# $Id$
NAME = geos
VERSION = 3.3.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Geometry Engine, Open Source
define BLURB
GEOS (Geometry Engine - Open Source) is a C++ port of the  Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the  OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.bz2
PATCHFILES += 0001-use-namespace-std-on-isnan-when-building-on-solaris-.patch
PATCHFILES += 0002-drop-use-of-macro-in-test-suite-that-conflicts-with-.patch

GARCOMPILER = GNU

PACKAGES = CSWlibgeos3-3-3
PACKAGES += CSWlibgeos-c1
PACKAGES += CSWgeos-dev
PACKAGES += CSWrb18-geos3-3-3

CATALOGNAME_CSWrb18-geos3-3-3 = rb18_geos3_2_2
SPKG_DESC_CSWrb18-geos3-3-3 += $(DESCRIPTION), ruby 1.8 bindings
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 = CSWruby18
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 += CSWlibgeos-c1
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWrb18-geos3-3-3 += CSWlibgeos3-3-3
PKGFILES_CSWrb18-geos3-3-3 += .*ruby.*
CHECKPKG_OVERRIDES_CSWrb18-geos3-3-3 += surplus-dependency|CSWruby18

CATALOGNAME_CSWlibgeos3-3-3 = libgeos3_2_2
SPKG_DESC_CSWlibgeos3-3-3 += $(DESCRIPTION), libgeos-3.2.2.so
PKGFILES_CSWlibgeos3-3-3 += $(call baseisadirs,$(libdir),libgeos-3\.3\.3\.so)
PKGFILES_CSWlibgeos3-3-3 += $(call baseisadirs,$(libdir),libgeos-3\.3\.3\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos3-3-3 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgeos3-3-3 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgeos3-3-3 = CSWgeos
CHECKPKG_OVERRIDES_CSWlibgeos3-3-3 += soname-equals-filename|file=/opt/csw/lib/libgeos-3.2.2.so

CATALOGNAME_CSWlibgeos-c1 = libgeos_c1
SPKG_DESC_CSWlibgeos-c1 += Geometry Engine, Open Source, libgeos_c.so.1
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),libgeos_c\.so\.1\.6\.2)
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),libgeos_c\.so\.1(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibgeos3-3-3
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgeos-c1 = CSWgeos

CATALOGNAME_CSWgeos-dev = geos_dev
SPKG_DESC_CSWgeos-dev = $(DESCRIPTION), development files
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_CONFIG)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_STATICLIB)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_LIBTOOL)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_INCLUDEDIR)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_PKGCONFIG)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_ACLOCAL)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_CONFIG_MANPAGE)
PKGFILES_CSWgeos-dev += $(PKGFILES_DEVEL_MAN3_MANPAGE)
PKGFILES_CSWgeos-dev += .*libgeos.so .*libgeos_c.so
RUNTIME_DEP_PKGS_CSWgeos-dev = CSWlibgeos3-3-3 CSWlibgeos-c1
OBSOLETED_BY_CSWlibgeos-dev = CSWgeos

# c++ libraries, so move things around a bit
libdir = $(abspath /opt/csw/gxx/lib/$(MM_LIBDIR))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-inline
CONFIGURE_ARGS += --enable-ruby

include gar/category.mk
