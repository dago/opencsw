NAME = ExtUtils-F77
VERSION = 1.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KGB

DESCRIPTION = Simple interface to F77 libs
define BLURB
  This module tries to figure out how to link C programs with Fortran
  subroutines on your system. Basically one must add a list of Fortran runtime
  libraries. The problem is their location and name varies with each
  OS/compiler combination!
endef

PACKAGES = CSWpmextutilsf77
CATALOGNAME = pm_extutilsf77

ARCHALL = 1

# Exclude crap the author has accidently left there from his Mac OS system
EXTRA_MERGE_EXCLUDE_FILES = .*/\..*

include gar/category.mk
