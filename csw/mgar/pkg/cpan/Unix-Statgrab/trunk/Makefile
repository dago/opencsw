GARNAME = Unix-Statgrab
GARVERSION = 0.04
CATEGORIES = cpan
AUTHOR = VPARSEVAL

DESCRIPTION = Perl extension for collecting information about the machine
define BLURB
endef

PACKAGES = CSWpmunixstatgrab
CATALOGNAME = pm_unixstatgrab

REQUIRED_PKGS = CSWlibstatgrab
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

EXTRA_PERL_CONFIGURE_ARGS = CC=$(CC) LIBS="-L$(libdir) -lstatgrab -lperl" INC="-I$(includedir)"

include gar/category.mk
