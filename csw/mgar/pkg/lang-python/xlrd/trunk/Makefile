NAME = xlrd
VERSION = 0.7.1
CATEGORIES = python
GARTYPE = v2
PACKAGES = CSWpy-xlrd
CATALOGNAME = py_xlrd
LICENSE = xlrd/licences.py
ARCHALL_CSWpy-xlrd = 1

DESCRIPTION = Library for developers to extract data from Microsoft Excel (tm) spreadsheet files
define BLURB
  Extract data from new and old Excel spreadsheets on any platform.
  Pure Python (2.1 to 2.6). Strong support for Excel dates. Unicode-aware.
endef

# 1st char of NAME is the directory name
MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
