NAME = GD
VERSION = 2.50
CATEGORIES = cpan
GARTYPE = v2
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

# The LICENSE file is missing in v2.50
LICENSE = README

PACKAGES += NIMOSSpm-gd
SPKG_DESC_NIMOSSpm-gd = Interface to GD graphics library
# PKGFILES is catchall
RUNTIME_DEP_PKGS_NIMOSSpm-gd += NIMOSSlibgd3
OBSOLETED_BY_NIMOSSpm-gd += NIMOSSpmgd
CATALOGNAME_NIMOSSpmgd = pm_gd_stub

# These are just docs and examples
CHECKPKG_OVERRIDES_NIMOSSpm-gd += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/qd.pl

REINPLACE_USRLOCAL += GD.pm

# These don't actually do anything as the pathes are already confgured
CONFIGURE_ARGS  = lib_gd_path $(libdir)
CONFIGURE_ARGS += lib_ft_path $(libdir)
CONFIGURE_ARGS += lib_png_path $(libdir)
CONFIGURE_ARGS += lib_jpeg_path $(libdir)
# This does not work due to different inclusion pathes
# CONFIGURE_ARGS += lib_xpm_path /usr/openwin/lib
CONFIGURE_ARGS += lib_xpm_path $(libdir)
CONFIGURE_ARGS += lib_zlib_path $(libdir)

# BUILD_OVERRIDE_VARS = CCFLAGS LD
BUILD_OVERRIDE_VARS = CCFLAGS
# Don't use hardcoded -Wformat=0
BUILD_OVERRIDE_VAR_CCFLAGS =

include gar/category.mk

# Needed to avoid https://rt.cpan.org/Public/Bug/Display.html?id=85789
pre-test-modulated:
	@cp files/t/test.out.* ${WORKSRC}/t/
	@$(MAKECOOKIE)
