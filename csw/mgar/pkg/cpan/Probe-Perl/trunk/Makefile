NAME = Probe-Perl
VERSION = 0.01
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KWILLIAMS

DESCRIPTION = Information about the currently running perl
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-probe-perl
CATALOGNAME_CSWpm-probe-perl = pm_probe_perl
SPKG_DESC_CSWpm-probe-perl = Information about the currently running perl
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-probe-perl = 1
OBSOLETED_BY_CSWpm-probe-perl += CSWpmprobeperl
CATALOGNAME_CSWpmprobeperl = pm_probeperl_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
