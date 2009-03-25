GARNAME = Pod-Simple
GARVERSION = 3.07
CATEGORIES = cpan
AUTHOR = ARANDAL

DESCRIPTION = Framework for parsing Pod
define BLURB
  Pod::Simple is a Perl library for parsing text in the Pod ("plain old
  documentation") markup language that is typically used for writing
  documentation for Perl and for Perl modules. The Pod format is explained in
  the perlpod man page; the most common formatter is called "perldoc".
endef

#DISTFILES = $(call admfiles,CSWpmpodsimple,depend prototype)

PACKAGES = CSWpmpodsimple
CATALOGNAME = pm_podsimple
#SPKG_DESC = $(DESCRIPTION)
ALLARCH = 1

REQUIRED_PKGS = CSWpmpodescapes

include gar/category.mk
