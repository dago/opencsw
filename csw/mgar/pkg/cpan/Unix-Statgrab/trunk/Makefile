NAME = Unix-Statgrab
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = VPARSEVAL

DESCRIPTION = Perl extension for collecting information about the machine
define BLURB
endef

LICENSE = README

BUILD_DEP_PKGS += CSWlibstatgrab-dev

PACKAGES += CSWpm-unix-statgrab
SPKG_DESC_CSWpm-unix-statgrab = Perl extension for collecting information about the machine
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpm-unix-statgrab = CSWlibstatgrab6
OBSOLETED_BY_CSWpm-unix-statgrab = CSWpmunixstatgrab
CATALOGNAME_CSWpmunixstatgrab = pm_unixstatgrab_stub

EXTRA_PERL_CONFIGURE_ARGS = CC=$(CC) LIBS="-L$(libdir) -lstatgrab -lperl" INC="-I$(includedir)"

include gar/category.mk
