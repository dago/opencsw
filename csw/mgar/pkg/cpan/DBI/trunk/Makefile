NAME = DBI
VERSION = 1.616
CATEGORIES = cpan
AUTHOR = TIMB

DESCRIPTION = Database independent interface for Perl
define BLURB
  The DBI is a database access module for the Perl programming language.  It
  defines a set of methods, variables, and conventions that provide a
  consistent database interface, independent of the actual database being
  used.
endef

DISTFILES  = COPYING
DISTFILES += CSWpm-dbi.cswreleasenotes

PACKAGES = CSWpm-dbi
CATALOGNAME = pm_dbi
SPKG_DESC_CSWpm-dbi = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-dbi = CSWpmdbi
CATALOGNAME_CSWpmdbi = pm_dbi_stub

CHECKPKG_OVERRIDES_CSWpm-dbi += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/DBD/File.pm
CHECKPKG_OVERRIDES_CSWpm-dbi += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/DBI/ProfileDumper/Apache.pm
CHECKPKG_OVERRIDES_CSWpm-dbi += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/DBD::File.3perl
CHECKPKG_OVERRIDES_CSWpm-dbi += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/DBI::ProfileDumper::Apache.3perl

include gar/category.mk
