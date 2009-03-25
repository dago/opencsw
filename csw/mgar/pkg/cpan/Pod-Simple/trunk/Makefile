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

DISTFILES = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpmpodsimple
CATALOGNAME = pm_podsimple
ARCHALL = 1

REQUIRED_PKGS = CSWpmpodescapes

include gar/category.mk
