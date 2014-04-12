# $Id$
NAME = geos
VERSION = 3.4.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Geometry Engine, Open Source
define BLURB
GEOS (Geometry Engine - Open Source) is a C++ port of the  Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the  OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(D
GARCOMPILER = GNU

PATCHFILES += 0000-use-namespace-std-on-isnan-when-building-on-solaris-.patch

PACKAGES = CSWlibgeos3-4-2
PACKAGES += CSWlibgeos-c1
PACKAGES += CSWgeos-dev

SPKG_DESC_CSWlibgeos3-4-2 += $(DESCRIPTION), libgeos-3.4.2.so
PKGFILES_CSWlibgeos3-4-2 += $(call baseisadirs,$(libdir),libgeos-3\.4\.2\.so)
PKGFILES_CSWlibgeos3-4-2 += $(call baseisadirs,$(libdir),libgeos-3\.4\.2\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos3-4-2 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgeos3-4-2 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgeos3-4-2Y_CSWlibgeos3-3-3 = CSWgeos

SPKG_DESC_CSWlibgeos-c1 += Geometry Engine, Open Source, libgeos_c.so.1
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),l8bgeos_c\.so\.1\.6\.2)
PKGFILES_CSWlibgeos-c1 += $(call baseisadirs,$(libdir),libgeos_c\.so\.1(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgeos-c4-2= CSWlibgeos3-3-3
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgeos-c1 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgeos-c1 = CSWgeos

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
RUNTIME_DEP_PKGS_CSWgeos-d4-2 CSWlibgeos-c1
OBSOLETED_BY_CSWlibgeos-dev = CSWgeos

BUILD64 = 1

##
## Ruby did not work (no errors, but was not built)
## Because I want to finish PostGIS, I continue w/o ruby
##

CONFIGURE_ARGS_32 = --enable-ruby
# When compiling on AMD64 with -m64 following error is raised
#
# /opt/csw/include/ruby-1.9.1/ruby/st.h:67:93: error: size of array 'st_check_for_sizeof_st_index_t' is negative
# typedef char st_check_for_sizeof_st_index_t[SIZEOF_VOIDP == (int)sizeof(st_index_t) ? 1 : -1];
#
# So, I'm lazzy and disable ruby on 64bit archs
CONFIGURE_ARGS_64 = --disable-ruby

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-inline
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORY_MODEL))

# -B direct breaks code amd64
LINKER_DIRECT =

include gar/category.mk

# The config process decides that the ruby library is called libruby*. That's
# fine, however, it uses -llibruby*as argument to the compiler/linker. That's
# bad. So fix it.
post-configure:
	gsed -i -E -e 's/^(RUBY_SO_NAME[ ]+=[ ]+)lib(ruby[0-9.]*)\.so.*/\1\2/' $(WORKSRC)/swig/ruby/Makefile
