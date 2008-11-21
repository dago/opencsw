GARNAME = Pod-Simple
GARVERSION = 3.05
CATEGORIES = cpan
AUTHOR = ARANDAL

DESCRIPTION = framework for parsing Pod
define BLURB
  Pod::Simple is a Perl library for parsing text in the Pod ("plain old
  documentation") markup language that is typically used for writing
  documentation for Perl and for Perl modules. The Pod format is explained in
  the perlpod man page; the most common formatter is called "perldoc".
endef

DISTFILES = $(call admfiles,CSWpmpodsimple,depend prototype)

DEPENDS += cpan/Pod-Escapes

include ../category.mk
