NAME = ftgl
VERSION = 2.1.3rc5
FILEVERSION = 2.1.3-rc5
DISTVERSION = 2.1.3~rc5
CATEGORIES = lib

DESCRIPTION = Library that uses Freetype2 to simplify rendering fonts in OpenGL applications
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(FILEVERSION).tar.bz2
DISTNAME = $(NAME)-$(DISTVERSION)

# Use these patches until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&atid=980351&aid=3077204&group_id=202130
PATCHFILES  = 0001-Do-not-use-gcc-specific-flags.patch 
PATCHFILES += 0002-Use-Sun-Studio-__func__-instead-of-gcc-__FUNCTION__.patch
PATCHFILES += 0003-Force-GNU-sed-when-using-i.patch
PATCHFILES += 0004-Keep-libtool-from-stripping-norunpath-during-linking.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWftgl CSWftgldevel

CATALOGNAME_CSWftgl = ftgl
CATALOGNAME_CSWftgldevel = ftgl_devel

SPKG_DESC_CSWftgl = $(DESCRIPTION)
SPKG_DESC_CSWftgldevel = FTGL Development Files

DEP_PKGS_CSWftgl = CSWmesa CSWzlib CSWftype2 CSWfreeglut
CHECKPKG_OVERRIDES_CSWftgl = surplus-dependency|CSWfreeglut
RUNTIME_DEP_PKGS_CSWftgldevel = CSWftgl
CHECKPKG_OVERRIDES_CSWftgldevel = surplus-dependency|CSWftgl

PKGFILES_CSWftgl = $(PKGFILES_RT)

NOISALIST = 1
# Unless the Solaris 10 compilation problem with both SUNW mesa and CSW mesa
# installed exists disable 64 bit for now.
# BUILD64_LIBS_ONLY = 1

LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

# Needed for __func__ used in Patch 0002
EXTRA_CXXFLAGS = -features=extensions -norunpath
EXTRA_LDFLAGS = -lm
#EXTRA_LIB-5.10 = /usr/X11/lib
#EXTRA_LIB = $(EXTRA_LIB-$(GAROSREL))

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --x-includes=/usr/openwin/include
#CONFIGURE_ARGS += --x-libraries=$(abspath /usr/openwin/lib/$(MM_LIBDIR))
#CONFIGURE_ARGS-5.9 += --with-gl-inc=$(includedir)
#CONFIGURE_ARGS-5.9 += --with-gl-lib=$(libdir)
#CONFIGURE_ARGS-5.10 += --with-gl-inc=/usr/X11/include
#CONFIGURE_ARGS-5.10 += --with-gl-lib=$(abspath /usr/X11/lib/$(MM_LIBDIR))
#CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))
CONFIGURE_ARGS += --with-gl-inc=$(includedir)
CONFIGURE_ARGS += --with-gl-lib=$(libdir)
CONFIGURE_ARGS += --with-glut-inc=$(includedir)
CONFIGURE_ARGS += --with-glut-lib=$(libdir)

include gar/category.mk
