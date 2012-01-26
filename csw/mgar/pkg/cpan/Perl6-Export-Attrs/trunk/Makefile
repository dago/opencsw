NAME = Perl6-Export-Attrs
VERSION = 0.0.3
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Perl6::Export::Attrs - The Perl 6 'is export(...)' trait as a Perl 5 attribute
define BLURB
	Implements a Perl 5 native version of what the Perl 6 symbol export mechanism will look like.

	It's very straightforward:

			* If you want a subroutine to be capable of being exported (when explicitly requested in the use arguments), you mark it with the :Export attribute.
			* If you want a subroutine to be automatically exported when the module is used (without specific overriding arguments), you mark it with the :Export(:DEFAULT) attribute.
			* If you want a subroutine to be automatically exported when the module is used (even if the user specifies overriding arguments), you mark it with the :Export(:MANDATORY) attribute.
			* If the subroutine should also be exported when particular export groups are requested, you add the names of those export groups to the attribute's argument list.

	That's it.	
endef

PACKAGES = CSWpmperl6exportattr
CATALOGNAME = pm_perl6exportattr

ARCHALL = 1
LICENSE = README

include gar/category.mk
