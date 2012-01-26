NAME = ExtUtils-CBuilder
VERSION = 0.2703
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAGOLDEN

DESCRIPTION = Compile and link C code for Perl modules
define BLURB
  This module can build the C portions of Perl modules by invoking the
  appropriate compilers and linkers in a cross-platform manner. It was
  motivated by the Module::Build project, but may be useful for other purposes
  as well.  However, it is not intended as a general cross-platform interface
  to all your C building needs. That would have been a much more ambitious
  goal!
endef

DISTFILES = COPYING

PACKAGES = CSWpmextutcbuilder
CATALOGNAME = pm_extutcbuilder

ARCHALL = 1

# Skip manpages as they are also in CSWperldoc. See
#   https://www.opencsw.org/mantis/view.php?id=4572
EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.* .*\/man\/man1\/.*

include gar/category.mk
