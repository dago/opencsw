GARNAME = m4
GARVERSION = 1.4.13
CATEGORIES = utils

DESCRIPTION = GNU m4 Unix macro processor
define BLURB
  GNU M4 is an implementation of the traditional Unix macro processor.
  It is mostly SVR4 compatible although it has some extensions (for example,
  handling more than 9 positional parameters to macros). GNU m4 also has
  built-in functions for including files, running shell commands, doing arithmetic, etc.
endef

MASTER_SITES = ftp://ftp.gnu.org/gnu/m4/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGE = CSWgm4

SPKG_SOURCEURL = http://www.gnu.org/software/m4/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWlibsigsegv

CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
