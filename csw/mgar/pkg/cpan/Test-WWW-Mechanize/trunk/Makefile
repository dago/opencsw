NAME = Test-WWW-Mechanize
VERSION = 1.44
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PETDANCE

DESCRIPTION = Testing-specific WWW::Mechanize subclass
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-test-www-mechanize
CATALOGNAME = pm_test_www_mechanize
SPKG_DESC_CSWpm-test-www-mechanize = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-test-www-mechanize = CSWpmtestwwwmech
CATALOGNAME_CSWpmtestwwwmech = pm_testwwwmech

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-carp-assert-more
RUNTIME_DEP_PKGS += CSWpm-html-tree
RUNTIME_DEP_PKGS += CSWpm-http-server-simple
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpm-test-longstring
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWpm-www-mechanize

# Released at same time, remove next time
CHECKPKG_OVERRIDES_CSWpm-test-www-mechanize += dependency-on-nonexistent-package|CSWpm-www-mechanize

include gar/category.mk
