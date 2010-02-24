GARNAME = xz
GARVERSION = 4.999.9beta
CATEGORIES = utils

DESCRIPTION = XZ Utils is free data compression software with high compression ratio
define BLURB
  XZ Utils is free general-purpose data compression software with high compression
  ratio. XZ Utils were written for POSIX-like systems (GNU/Linux, *BSDs, etc.), but
  also work on some not-so-POSIX systems like Windows. XZ is based on the LZMA2
  algorithm. The implementation is much more heavywight than lzip.
endef

MASTER_SITES = http://tukaani.org/xz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

RUNTIME_DEP_PKGS = CSWggettextrt CSWgcc4corert

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER    = GNU
CONFIGURE_ARGS = $(DIRPATHS)

# not able to figure out which target runs the tests in "tests"
TEST_TARGET = check

include gar/category.mk
