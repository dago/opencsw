GARNAME = libwww-perl
GARVERSION = 5.825
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = A general-purpose Web API for Perl, based on W3C libwww
define BLURB
  The DBI is a database access module for the Perl programming language.  It
  defines a set of methods, variables, and conventions that provide a
  consistent database interface, independent of the actual database being
  used.
endef

DISTFILES += $(call admfiles,CSWpmlibwww,)

REQUIRED_PKGS = CSWpmhtmltagset CSWpmuri CSWpmhtmlparser CSWpmcompresszlib CSWpmhtmlfmt CSWpmmimebase64

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

DEPENDS += cpan/URI
DEPENDS += cpan/HTML-Parser
DEPENDS += cpan/Crypt-SSLeay
DEPENDS += cpan/Data-Dump

CONFIGURE_ARGS =

include gar/category.mk
