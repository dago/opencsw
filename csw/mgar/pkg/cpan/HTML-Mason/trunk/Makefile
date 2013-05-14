NAME = HTML-Mason
VERSION = 1.51
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JSWARTZ

DESCRIPTION = High-performance, dynamic web site authoring system
define BLURB
endef

LICENSE = LICENSE

PACKAGES = CSWpm-html-mason
CATALOGNAME = pm_html_mason
SPKG_DESC_CSWpm-html-mason = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-html-mason = CSWpmhtmlmason
CATALOGNAME_CSWpmhtmlmason = pm_htmlmason

BUILD_DEP_PKGS += CSWpm-test-deep

RUNTIME_DEP_PKGS += CSWpmcachecache
RUNTIME_DEP_PKGS += CSWpmclscontainer
RUNTIME_DEP_PKGS += CSWpm-exception-class
RUNTIME_DEP_PKGS += CSWpm-html-parser
RUNTIME_DEP_PKGS += CSWpm-log-any
RUNTIME_DEP_PKGS += CSWpm-params-validate

ARCHALL = 1

include gar/category.mk
