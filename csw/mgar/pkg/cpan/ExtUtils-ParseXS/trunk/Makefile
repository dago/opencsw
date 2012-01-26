NAME = ExtUtils-ParseXS
VERSION = 2.2206
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAGOLDEN

DESCRIPTION = Converts Perl XS code into C code
define BLURB
  ExtUtils::ParseXS will compile XS code into C code by embedding the
  constructs necessary to let C functions manipulate Perl values and creates
  the glue necessary to let Perl access those functions. The compiler uses
  typemaps to determine how to map C function parameters and variables to Perl
  values.
endef

DISTFILES = COPYING

PACKAGES = CSWpmextutparsexs
CATALOGNAME = pm_extutparsexs

ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmextutcbuilder

# Skip manpages as they are also in CSWperldoc. See
#   https://www.opencsw.org/mantis/view.php?id=4571
EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.* .*\/man\/man1\/.*

include gar/category.mk
