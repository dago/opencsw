GARNAME = libwww-perl
GARVERSION = 5.820
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = a general-purpose Web API for Perl, based on W3C libwww.
define BLURB
  The DBI is a database access module for the Perl programming language.  It
  defines a set of methods, variables, and conventions that provide a
  consistent database interface, independent of the actual database being
  used.
endef

#DISTFILES += $(call admfiles,CSWpmlibwww,depend prototype)
DISTFILES += $(call admfiles,CSWpmlibwww,depend)

DEPENDS += cpan/URI
DEPENDS += cpan/HTML-Parser
DEPENDS += cpan/Crypt-SSLeay
DEPENDS += cpan/Data-Dump

#CONFIGURE_ARGS = -n
CONFIGURE_ARGS =

include ../category.mk
