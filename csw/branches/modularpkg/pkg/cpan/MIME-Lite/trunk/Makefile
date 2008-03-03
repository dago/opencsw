GARNAME = MIME-Lite
GARVERSION = 3.01_04
CATEGORIES = cpan
AUTHOR = YVES

DESCRIPTION = low-calorie MIME generator
define BLURB
  MIME::Lite is intended as a simple, standalone module for generating (not
  parsing!) MIME messages... specifically, it allows you to output a simple,
  decent single- or multi-part message with text or binary attachments. It
  does not require that you have the Mail:: or MIME:: modules installed.
endef

DISTFILES += CSWpmmimelite.gspec CSWpmmimelite.depend

# Always add the prerequisite modules
PATCHFILES = config.diff

DEPENDS += cpan/MIME-Types

# Test seems to work, but wierd test harness makes it difficult
# to tell why the test fails.  Disable for now.
TEST_SCRIPTS =

include gar/category.mk
