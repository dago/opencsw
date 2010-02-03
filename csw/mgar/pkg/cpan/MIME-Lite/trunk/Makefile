GARNAME = MIME-Lite
GARVERSION = 3.027
CATEGORIES = cpan
AUTHOR = RJBS

DESCRIPTION = Perl low-calorie MIME generator
define BLURB
  MIME::Lite is intended as a simple, standalone module for generating (not
  parsing!) MIME messages... specifically, it allows you to output a simple,
  decent single- or multi-part message with text or binary attachments. It
  does not require that you have the Mail:: or MIME:: modules installed.
endef

PACKAGES = CSWpmmimelite
CATALOGNAME = pm_mimelite

REQUIRED_PKGS = CSWpmmimetypes CSWpmmailtools CSWpmemaildateformat
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

# Do not prompt for stuff
PATCHFILES = 0001-Skip-prompting.patch

ARCHALL = 1

include gar/category.mk
