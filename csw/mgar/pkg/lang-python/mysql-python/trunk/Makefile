# $Id$

NAME = MySQL-python
VERSION = 1.2.4
CATEGORIES = python
GARTYPE = v2

define BLURB
  MySQL support for Python
endef

SF_PROJECT = $(call TOLOWER,$(NAME))
# MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(DISTNAME).zip

GARCOMPILER = SOS12U3

PACKAGES = CSWpy-mysql
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibmysqlclient18
SPKG_DESC_CSWpy-mysql = MySQL Support for Python

SKIPTEST = 1

include gar/category.mk
