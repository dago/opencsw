NAME = PDL
VERSION = 2.4.6
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHM

DESCRIPTION = The Perl Data Language
define BLURB
  PDL is the Perl Data Language, a perl extension that is designed for
  scientific and bulk numeric data processing and display. It extends perl's
  syntax and includes fully vectorized, multidimensional array handling, plus
  several paths for device-independent graphics output.
endef

PACKAGES = CSWpmpdl
CATALOGNAME = pm_pdl

PATCHFILES += patch-quiet_nan.c
PATCHFILES += patch-perldl.conf

RUNTIME_DEP_PKGS = CSWpmextutilsf77 CSWpminline CSWgd
BUILD_DEP_PKGS = CSWpminline CSWgd

include gar/category.mk

post-configure-modulated:
	gfind $(WORKSRC) -name Makefile | xargs \
		perl -pi -e 's,-L/opt/csw/lib/libperl.so,-R/opt/csw/lib -lperl,'
