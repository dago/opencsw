NAME = experimental
VERSION = 0.005
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = LEONT

DESCRIPTION = Experimental features made easy
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build-tiny

PACKAGES += CSWpm-experimental
CATALOGNAME_CSWpm-experimental = pm_experimental
SPKG_DESC_CSWpm-experimental = Experimental features made easy
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-experimental = 1

PERLBUILD_INSTALL_ARGS = --destdir=$(DESTDIR) --mandir=$(mandir) $(EXTRA_PERLBUILD_INSTALL_ARGS)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
