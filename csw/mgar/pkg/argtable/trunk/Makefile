NAME = argtable
VERSION = 2.12
CATEGORIES = utils

DESCRIPTION = Parsing GNU style command line options with a minimum of fuss
define BLURB
  Argtable is an ANSI C library for parsing GNU style command line options with a minimum of fuss.
  It enables a program's command line syntax to be defined in the source code as an array of argtable
  structs. The command line is then parsed according to that specification and the resulting values
  are returned in those same structs where they are accessible to the main program. Both tagged
  (-v, --verbose, --foo=bar) and untagged arguments are supported, as are multiple instances of
  each argument. Syntax error handling is automatic and the library also provides the means for
  generating a textual description of the command line syntax.
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME)$(subst .,-,$(VERSION))
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://argtable.sourceforge.net/

EXTRA_LDFLAGS = -lintl

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
