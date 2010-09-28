GARNAME = ftgl
GARVERSION = 2.1.3rc5
FILEVERSION = 2.1.3-rc5
DISTVERSION = 2.1.3~rc5
CATEGORIES = lib

DESCRIPTION = Library that uses Freetype2 to simplify rendering fonts in OpenGL applications
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(FILEVERSION).tar.bz2
DISTNAME = $(GARNAME)-$(DISTVERSION)

PATCHFILES  = 0001-Do-not-use-gcc-specific-flags.patch 
PATCHFILES += 0002-Use-Sun-Studio-__func__-instead-of-gcc-__FUNCTION__.patch
PATCHFILES += 0003-Force-GNU-sed-when-using-i.patch
PATCHFILES += 0004-Keep-libtool-from-stripping-norunpath-during-linking.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWftgl CSWftgldevel

CATALOGNAME_CSWftgl = ftgl
CATALOGNAME_CSWftgldevel = ftgl_devel

SPKG_DESC_CSWftgl = $(DESCRIPTION)
SPKG_DESC_CSWftgldevel = FTGL Development Files

DEP_PKGS_CSWftgl = CSWmesa CSWzlib CSWftype2
RUNTIME_DEP_PKGS_CSWftgldevel = CSWftgl
CHECKPKG_OVERRIDES_CSWftgldevel = surplus-dependency|CSWftgl

PKGFILES_CSWftgl = $(PKGFILES_RT)

NOISAEXEC = 1
NOISALIST = 1

# First we need CSWfreeglut in 64 bit
# BUILD64 = 1

# Needed for __func__ used in Patch 0002
EXTRA_CXXFLAGS = -features=extensions -norunpath
EXTRA_LDFLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gl-inc=$(includedir)
CONFIGURE_ARGS += --with-gl-lib=$(libdir)
CONFIGURE_ARGS += --with-glut-inc=$(includedir)
CONFIGURE_ARGS += --with-glut-lib=$(libdir)

include gar/category.mk
