GARNAME = GD
GARVERSION = 2.35
CATEGORIES = cpan
AUTHOR = LDS

DESCRIPTION = interface to Gd Graphics Library
define BLURB
  GD.pm is a Perl interface to Thomas Boutell\'s gd graphics library (version
  2.01 or higher; see below). GD allows you to create color drawings using a
  large number of graphics primitives, and emit the drawings as PNG files.
endef

# The GD test gives strange results on test 10. Visual
# inspection shows the images to be identical, but the
# created data is smaller than the regression data.
# Skip test 10 for now.
#PATCHFILES = gdtest.diff

DISTFILES += CSWpmgd.gspec CSWpmgd.depend

DEPENDS += lib/gd

CONFIGURE_ARGS  = -options "JPEG,FT,XPM"
CONFIGURE_ARGS += -lib_gd_path $(libdir)
CONFIGURE_ARGS += -lib_ft_path $(libdir)
CONFIGURE_ARGS += -lib_png_path $(libdir)
CONFIGURE_ARGS += -lib_jpeg_path $(libdir)
CONFIGURE_ARGS += -lib_xpm_path $(libdir)
CONFIGURE_ARGS += -lib_zlib_path $(libdir)

include ../category.mk
