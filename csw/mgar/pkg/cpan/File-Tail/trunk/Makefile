NAME = File-Tail
VERSION = 0.99.3
CATEGORIES = cpan
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

CHECKPKG_OVERRIDES_CSWpmfiletail += license-missing

include gar/category.mk
