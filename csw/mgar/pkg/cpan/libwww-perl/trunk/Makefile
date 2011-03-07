NAME = libwww-perl
VERSION = 5.837
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = A general-purpose Web API for Perl, based on W3C libwww
define BLURB
  The DBI is a database access module for the Perl programming language.  It
  defines a set of methods, variables, and conventions that provide a
  consistent database interface, independent of the actual database being
  used.
endef

DISTFILES = COPYING

PACKAGES = CSWpm-libwww-perl
CATALOGNAME = pm_libwww_perl
SPKG_DESC_CSWpm-libwww-perl = $(DESCRIPTION)
ARCHALL = 1
OBSOLETES_CSWpm-libwww-perl = CSWpmlibwww
CATALOGNAME_CSWpmlibwww = pm_libwww

RUNTIME_DEP_PKGS = CSWpmhtmltagset CSWpmuri CSWpmhtmlparser CSWpmiocompress CSWpmhtmlfmt CSWpmmimebase64

include gar/category.mk
