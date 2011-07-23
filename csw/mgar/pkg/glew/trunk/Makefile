# $Id$
#
# TBD:
# - Split package
# - Fixup soname (current: none, packages exist linking libGLEW.so, Linux has libGLEW.so.x.y
#     http://rpmfind.net//linux/RPM/mandriva/devel/cooker/sparc/media/main/release/libglew1.3-1.3.4-3mdv2007.0.sparc.html

NAME = glew
VERSION = 1.6.0
CATEGORIES = lib

DESCRIPTION = OpenGL Extension Wrangler Library (GLEW)
define BLURB
  The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
  extension loading library. GLEW provides efficient run-time mechanisms for determining
  which OpenGL extensions are supported on the target platform. OpenGL core and extension
  functionality is exposed in a single header file. GLEW has been tested on a variety of
  operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tgz

# Use patch until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=3376260&group_id=67586&atid=523274
PATCHFILES = 0001-Use-inttypes-also-for-Solaris.patch

LICENSE = LICENSE.txt

BUILD_DEP_PKGS = CSWmesa

PACKAGES += CSWlibglew1-6
SPKG_DESC_CSWlibglew1-6 = OpenGL extension wrangler library (GLEW), libGLEW.so.1.6
PKGFILES_CSWlibglew1-6 = $(call pkgfiles_lib,libGLEW.so.1.6)
RUNTIME_DEP_PKGS_CSWlibglew1-6 += CSWmesa

PACKAGES += CSWlibglew-dev
SPKG_DESC_CSWlibglew-dev = Development files for libGLEW.so.1.6
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibglew-dev += CSWlibglew1-6
# Existing packages are linked against SONAME libGLEW.so only in this package
OBSOLETED_BY_CSWlibglew-dev = CSWglew

NOISALIST = 1
BUILD64 = 1

LDOPT-64 = -64
EXTRA_CFLAGS-sparc = -xcode=pic32

BUILD_OVERRIDE_VARS = CC CFLAGS.EXTRA OPT LDFLAGS.SO LDFLAGS.EXTRA
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS.EXTRA = $(CFLAGS) $(CPPFLAGS) $(EXTRA_CFLAGS-$(GARCH))
BUILD_OVERRIDE_VAR_LDFLAGS.SO = -G $(LDOPT-$(MEMORYMODEL)) -h libGLEW.so.1.6
# -ldl for dlsym/dlopen in glew.mx
BUILD_OVERRIDE_VAR_LDFLAGS.EXTRA = -L$(libdir) -ldl

# These are for glew.pc
BUILD_OVERRIDE_VARS += GLEW_DEST LIBDIR BINDIR INCDIR
BUILD_OVERRIDE_VAR_GLEW_DEST = $(prefix)
BUILD_OVERRIDE_VAR_LIBDIR = $(libdir)
BUILD_OVERRIDE_VAR_BINDIR = $(bindir)
BUILD_OVERRIDE_VAR_INCDIR = $(includedir)

CONFIGURE_SCRIPTS =

TEST_SCRIPTS = 

INSTALL_OVERRIDE_DIRS = GLEW_DEST BINDIR LIBDIR
GLEW_DEST = $(prefix)
BINDIR = $(bindir)
LIBDIR = $(libdir)
INSTALL_OVERRIDE_VARS = INSTALL LDFLAGS.EXTRA
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall
INSTALL_OVERRIDE_VAR_LDFLAGS.EXTRA = $(LDFLAGS)

include gar/category.mk
