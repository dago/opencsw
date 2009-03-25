GARNAME = DBI
GARVERSION = 1.607
CATEGORIES = cpan
AUTHOR = TIMB

DESCRIPTION = Database independent interface for Perl
define BLURB
  The DBI is a database access module for the Perl programming language.  It
  defines a set of methods, variables, and conventions that provide a
  consistent database interface, independent of the actual database being
  used.
endef

DISTFILES = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpmdbi
CATALOGNAME = pm_dbi

REQUIRED_PKGS = CSWpmplrpc

include gar/category.mk
