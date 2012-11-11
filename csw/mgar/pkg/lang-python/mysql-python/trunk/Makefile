# $Id$

NAME = MySQL-python
VERSION = 1.2.4b4
CATEGORIES = python
GARTYPE = v2

define BLURB
  MySQL support for Python
endef

SF_PROJECT = $(call TOLOWER,$(NAME))
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).tar.gz

GARCOMPILER = SOS12U3

PACKAGES = CSWpy-mysql
CATALOGNAME_CSWpy-mysql = py_mysql
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibmysqlclient18

SPKG_DESC_CSWpy-mysql = MySQL Support for Python

OBSOLETED_BY_CSWpy-mysql = CSWpymysql
CATALOGNAME_CSWpymysql = pymysql

mysql_prefix = $(prefix)/mysql5
mysql_bindir = $(mysql_prefix)/bin/$(ISA_DEFAULT_$(GARCH))

CHECKPKG_OVERRIDES_CSWpymysql += surplus-dependency|CSWpython

SKIPTEST = 1

include gar/category.mk

PATH       := $(mysql_bindir):$(PATH)
export PATH 
