NAME = Perl6-Slurp
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Perl6::Slurp - Implements the Perl 6 'slurp' built-in
define BLURB
  slurp takes:

			* a filename,
			* a filehandle,
			* a typeglob reference,
			* an IO::File object, or
			* a scalar reference,

	converts it to an input stream if necessary, and reads in the entire stream.
	If slurp fails to set up or read the stream, it throws an exception.
endef

PACKAGES = CSWpmperl6slurp
CATALOGNAME = pm_perl6slurp

ARCHALL = 1
LICENSE = README

RUNTIME_DEP_PKGS = CSWpmperl6export
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)

include gar/category.mk
