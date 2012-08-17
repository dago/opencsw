NAME = UNIVERSAL-require
VERSION = 0.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MSCHWERN

DESCRIPTION = Require() modules from a variable
define BLURB
  If you've ever had to do this...
    eval "require $module";
  to get around the bareword caveats on require(), this module is for you. It
  creates a universal require() class method that will work with every Perl
  module and its secure.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGES = CSWpm-universal-require
CATALOGNAME = pm_universal_require
ARCHALL = 1

# name change handling
SPKG_DESC_CSWpm-universal-require = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-universal-require = CSWpmunivrequire

include gar/category.mk
