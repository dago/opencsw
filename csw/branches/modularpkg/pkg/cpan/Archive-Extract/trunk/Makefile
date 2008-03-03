GARNAME = Archive-Extract
GARVERSION = 0.16
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = A generic archive extracting mechanism
define BLURB
  Archive::Extract is a generic archive extraction mechanism.  It allows you
  to extract any archive file of the type .tar, .tar.gz, .gz, tar.bz2, .tbz,
  .bz2 or .zip without having to worry how it does so, or use different
  interfaces for each type by using either perl modules, or commandline tools
  on your system.
endef

DISTFILES += $(call admfiles,CSWpmarchiveextract,depend prototype)

DEPENDS += cpan/IPC-Cmd
DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load-Conditional
DEPENDS += cpan/Locale-Maketext-Simple

include gar/category.mk

