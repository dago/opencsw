GARNAME = GD
GARVERSION = 2.45
CATEGORIES = cpan
AUTHOR = LDS

DESCRIPTION = Interface to GD Graphics Library
define BLURB
  GD.pm is a Perl interface to Thomas Boutell\'s gd graphics library (version
  2.01 or higher; see below). GD allows you to create color drawings using a
  large number of graphics primitives, and emit the drawings as PNG files.
endef

# The file format for files written with libjpeg.so.7 has changed.
# Disable binary identity test until this is fixed:
#   https://rt.cpan.org/Ticket/Display.html?id=49053
PATCHFILES = diff-GD.t

PACKAGES = CSWpmgd
CATALOGNAME = pm_gd

LICENSE = LICENSE

DEP_PKGS = CSWftype2 CSWgd CSWiconv CSWjpeg CSWpng
DEP_PKGS += CSWzlib CSWfconfig

# Make sure we bind against Openwin libXpm
NOISALIST = 1
EXTRA_LIB = /usr/openwin/lib

CONFIGURE_ARGS  = lib_gd_path $(libdir)
CONFIGURE_ARGS += lib_ft_path $(libdir)
CONFIGURE_ARGS += lib_png_path $(libdir)
CONFIGURE_ARGS += lib_jpeg_path $(libdir)
CONFIGURE_ARGS += lib_xpm_path /usr/openwin/lib
CONFIGURE_ARGS += lib_zlib_path $(libdir)

# Don't use hardcoded -Wformat=0
BUILD_OVERRIDE_DIRS = CCFLAGS

CHECKPKG_OVERRIDES_CSWpmgd += linked-against-discouraged-library|GD.so|libX11.so.4

include gar/category.mk
