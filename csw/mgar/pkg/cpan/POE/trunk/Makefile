NAME = POE
VERSION = 1.350
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCAPUTO

DESCRIPTION = Portable, event-loop agnostic eventy networking and multitasking
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = README

BUILD_DEP_PKGS += CSWpm-poe-test-loops

PACKAGES += CSWpm-poe
CATALOGNAME_CSWpm-poe = pm_poe
SPKG_DESC_CSWpm-poe = Portable, event-loop agnostic eventy networking and multitasking.
ARCHALL_CSWpm-poe = 1
RUNTIME_DEP_PKGS_CSWpm-poe += CSWpm-io-tty
RUNTIME_DEP_PKGS_CSWpm-poe += CSWpm-poe-test-loops
OBSOLETED_BY_CSWpm-poe += CSWpmpoe
CATALOGNAME_CSWpmpoe = pm_poe_stub

# These are just examples:
CHECKPKG_OVERRIDES_CSWpm-poe += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/POE.3perl
CHECKPKG_OVERRIDES_CSWpm-poe += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/POE.pm

include gar/category.mk
