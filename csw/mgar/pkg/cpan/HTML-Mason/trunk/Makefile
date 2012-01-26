NAME = HTML-Mason
VERSION = 1.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = High-performance, dynamic web site authoring system
define BLURB
  Mason is a tool for building, serving and managing large web sites. Its
  features make it an ideal backend for high load sites serving dynamic
  content, such as online newspapers or database driven e-commerce sites.
endef

LICENSE = LICENSE

PACKAGES = CSWpmhtmlmason
CATALOGNAME = pm_htmlmason

BUILD_DEP_PKGS = CSWpmlogany CSWpmtestdeep
RUNTIME_DEP_PKGS = CSWpmexceptcls CSWpmclscontainer CSWpmparamsvalidate CSWpmcachecache

ARCHALL = 1

include gar/category.mk
