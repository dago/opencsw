NAME = Moo
VERSION = 1.003000
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = HAARG

DESCRIPTION = Minimalist Object Orientation (with Moose compatibility)
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-fatal

PACKAGES += CSWpm-moo
CATALOGNAME_CSWpm-moo = pm_moo
SPKG_DESC_CSWpm-moo = Minimalist Object Orientation (with Moose compatibility)
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-moo = 1
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-strictures
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-class-method-modifiers
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-role-tiny
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-devel-globaldestruction
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-dist-checkconflicts
RUNTIME_DEP_PKGS_CSWpm-moo += CSWpm-module-runtime

include gar/category.mk
