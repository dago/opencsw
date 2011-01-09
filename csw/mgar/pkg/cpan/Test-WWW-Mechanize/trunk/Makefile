NAME = Test-WWW-Mechanize
VERSION = 1.30
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = Testing-specific WWW::Mechanize subclass
define BLURB
  Testing-specific WWW::Mechanize subclass
endef

DISTFILES += COPYING

PACKAGES = CSWpmtestwwwmech
CATALOGNAME = pm_testwwwmech
ARCHALL = 1

SKIPTEST = 1

RUNTIME_DEP_PKGS += CSWpmtestlongstring
RUNTIME_DEP_PKGS += CSWpmwwwmechanize
RUNTIME_DEP_PKGS += CSWpmhtmltree
RUNTIME_DEP_PKGS += CSWpmcarpassertmore

CHECKPKG_OVERRIDES_CSWpmtestwwwmech += unidentified-dependency

include gar/category.mk
