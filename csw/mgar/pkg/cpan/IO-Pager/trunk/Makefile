NAME = IO-Pager
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JPIERCE

DESCRIPTION = Select a pager, optionally pipe it output if destination is a TTY
define BLURB
  IO::Pager is lightweight and can be used to locate an available pager and
  set ENV{PAGER} (see "NOTES") or as a factory for creating objects defined
  elsewhere such as IO::Pager::Buffered and IO::Pager::Unbuffered.
endef

MODDIST   = $(NAME)-$(VERSION).tgz
DISTFILES = $(call admfiles,CSWpmiopager,depend prototype)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

# Tests are mostly visual verification
TEST_SCRIPTS =

include gar/category.mk
