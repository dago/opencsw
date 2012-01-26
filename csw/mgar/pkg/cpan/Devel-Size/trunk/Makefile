NAME = Devel-Size
VERSION = 0.71
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TELS

DESCRIPTION = Extension for finding the memory usage of Perl variables
define BLURB
  This module figures out the real sizes of Perl variables in bytes. Call
  functions with a reference to the variable you want the size of. If the
  variable is a plain scalar it returns the size of the scalar. If the
  variable is a hash or an array, use a reference when calling.
endef

MASTER_SITES = $(addsuffix devel/,$(CPAN_MIRRORS))
DISTFILES = COPYING

PACKAGES = CSWpmdevelsize
CATALOGNAME = pm_develsize

include gar/category.mk
