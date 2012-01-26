NAME = File-Tail
VERSION = 0.99.3
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MGRABNAR

DESCRIPTION = Perl extension for reading from continously updated files
define BLURB
  The primary purpose of File::Tail is reading and analysing log files while
  they are being written, which is especialy usefull if you are monitoring the
  logging process with a tool like Tobias Oetiker's MRTG.
endef

PACKAGES = CSWpmfiletail
CATALOGNAME = pm_filetail
ARCHALL = 1

DISTFILES += LICENSE

LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWpmfiletail += catalogname-does-not-match-pkgname|pkgname=CSWpmfiletail|catalogname=pm_filetail|expected-catalogname=pmfiletail

include gar/category.mk
