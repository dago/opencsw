GARNAME = IO-Pager
GARVERSION = 0.06
CATEGORIES = cpan
AUTHOR = JPIERCE

DESCRIPTION = Select a pager, optionally pipe it output if destination is a TTY
define BLURB
  IO::Pager is lightweight and can be used to locate an available pager and
  set ENV{PAGER} (see "NOTES") or as a factory for creating objects defined
  elsewhere such as IO::Pager::Buffered and IO::Pager::Unbuffered.
endef

MODDIST   = $(GARNAME)-$(GARVERSION).tgz
DISTFILES = $(call admfiles,CSWpmiopager,depend prototype)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

# Tests are mostly visual verification
TEST_SCRIPTS =

include gar/category.mk
