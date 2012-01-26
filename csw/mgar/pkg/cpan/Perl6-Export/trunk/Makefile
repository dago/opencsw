NAME = Perl6-Export
VERSION = 0.07
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Perl6::Export - Implements the Perl 6 'is export(...)' trait
define BLURB
	Implements what I hope the Perl 6 symbol export mechanism might look like.

	It's very straightforward:

		* If you want a subroutine to be capable of being exported (when explicitly requested in the use arguments), you mark it with the is export trait.
		* If you want a subroutine to be automatically exported when the module is used (without specific overriding arguments), you mark it with the is export(:DEFAULT) trait.
		* If you want a subroutine to be automatically exported when the module is used (even if the user specifies overriding arguments), you mark it with the is export(:MANDATORY) trait.
		* If the subroutine should also be exported when particular export groups are requested, you add the names of those export groups to the trait's argument list.

	That's it.
endef

PACKAGES = CSWpmperl6export
CATALOGNAME = pm_perl6export
ARCHALL = 1
LICENSE = README

CHECKPKG_OVERRIDES = 

include gar/category.mk
