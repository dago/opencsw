# $Id$
GARNAME = glew
GARVERSION = 1.5.6
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
PATCHFILES = 0001-Use-inttypes-also-for-Solaris.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

DEP_PKGS = CSWmesa

LICENSE = LICENSE.txt

NOISALIST = 1
NOISAEXEC = 1
BUILD64 = 1

LDOPT-64 = -64
EXTRA_CFLAGS-sparc = -xcode=pic32

BUILD_OVERRIDE_VARS = CC CFLAGS.EXTRA OPT LDFLAGS.SO LDFLAGS.EXTRA
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS.EXTRA = $(CFLAGS) $(CPPFLAGS) $(EXTRA_CFLAGS-$(GARCH))
BUILD_OVERRIDE_VAR_LDFLAGS.SO = -G $(LDOPT-$(MEMORYMODEL))
BUILD_OVERRIDE_VAR_LDFLAGS.EXTRA = -L$(libdir)

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

MERGE_DIRS_isa-extra = $(libdir)

# These are NOT bad...
CHECKPKG_OVERRIDES_CSWglew += bad-rpath-entry|/usr/openwin/lib/64|opt/csw/bin/sparcv9/glewinfo
CHECKPKG_OVERRIDES_CSWglew += bad-rpath-entry|/usr/openwin/lib/64|opt/csw/bin/sparcv9/visualinfo
CHECKPKG_OVERRIDES_CSWglew += bad-rpath-entry|/usr/openwin/lib/64|opt/csw/lib/sparcv9/libGLEW.so.1.5.6

include gar/category.mk
