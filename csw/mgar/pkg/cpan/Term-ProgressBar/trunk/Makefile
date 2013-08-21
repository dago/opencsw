NAME = Term-ProgressBar
VERSION = 2.14
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SZABGAB

DESCRIPTION = Provide a progress meter on a standard terminal
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-capture-tiny

PACKAGES += CSWpm-term-progressbar
CATALOGNAME_CSWpm-term-progressbar = pm_term_progressbar
SPKG_DESC_CSWpm-term-progressbar = Provide a progress meter on a standard terminal
ARCHALL_CSWpm-term-progressbar = 1
RUNTIME_DEP_PKGS_CSWpm-term-progressbar += CSWpm-term-readkey
RUNTIME_DEP_PKGS_CSWpm-term-progressbar += CSWpm-class-methodmaker

include gar/category.mk
