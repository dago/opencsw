GARNAME = Inline
GARVERSION = 0.45
CATEGORIES = cpan
AUTHOR = SISYPHUS

DESCRIPTION = Write Perl subroutines in other programming languages
define BLURB
  The Inline module allows you to put source code from other programming
  languages directly "inline" in a Perl script or module. The code is
  automatically compiled as needed, and then loaded for immediate access from
  Perl.
endef

PATCHFILES = 0001-Skip-question-on-install.patch

PACKAGES = CSWpminline
CATALOGNAME = pm_inline

ARCHALL = 1

# The current licensing is unknown as is stated on CPAN
CHECKPKG_OVERRIDES = license-missing

include gar/category.mk
