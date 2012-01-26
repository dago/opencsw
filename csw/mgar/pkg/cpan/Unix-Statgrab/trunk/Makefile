NAME = Unix-Statgrab
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = VPARSEVAL

DESCRIPTION = Perl extension for collecting information about the machine
define BLURB
endef

PACKAGES = CSWpmunixstatgrab
CATALOGNAME = pm_unixstatgrab

RUNTIME_DEP_PKGS = CSWlibstatgrab
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

EXTRA_PERL_CONFIGURE_ARGS = CC=$(CC) LIBS="-L$(libdir) -lstatgrab -lperl" INC="-I$(includedir)"

include gar/category.mk
