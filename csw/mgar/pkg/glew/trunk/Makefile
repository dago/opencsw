# $Id$
#

NAME = glew
VERSION = 1.7.0
CATEGORIES = lib
GARTYPE = v2

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

LICENSE = LICENSE.txt

BUILD_DEP_PKGS = CSWmesa

PACKAGES += CSWlibglew1-7
SPKG_DESC_CSWlibglew1-7 = OpenGL extension wrangler library (GLEW), libGLEW.so.1.7
PKGFILES_CSWlibglew1-7 = $(call pkgfiles_lib,libGLEW.so.1.7)
RUNTIME_DEP_PKGS_CSWlibglew1-7 += CSWmesa

PACKAGES += CSWlibglew-dev
SPKG_DESC_CSWlibglew-dev = Development files for libGLEW.so.1.7
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibglew-dev += CSWlibglew1-7

NOISALIST = 1
BUILD64_LIBS_ONLY = 1

LDOPT-64 = -64
EXTRA_CFLAGS-sparc = -xcode=pic32

BUILD_OVERRIDE_VARS = CC CFLAGS.EXTRA OPT LDFLAGS.SO LDFLAGS.EXTRA
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS.EXTRA = $(CFLAGS) $(CPPFLAGS) $(EXTRA_CFLAGS-$(GARCH))
BUILD_OVERRIDE_VAR_LDFLAGS.SO = -G $(LDOPT-$(MEMORYMODEL)) -h libGLEW.so.1.7
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
