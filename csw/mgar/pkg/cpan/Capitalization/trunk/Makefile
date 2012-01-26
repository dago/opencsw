NAME = capitalization
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIYAGAWA

DESCRIPTION = No capitalization on method names
define BLURB
endef

DISTFILES = COPYING

PACKAGES = CSWpmcapitalization
CATALOGNAME = pm_capitalization

DEP_PKGS = CSWpmdevelsymdump

ARCHALL = 1

# The CPAN name *really* does not start with a capital
CHECKPKG_OVERRIDES_CSWpmcapitalization += pkginfo-description-not-starting-with-uppercase

include gar/category.mk
