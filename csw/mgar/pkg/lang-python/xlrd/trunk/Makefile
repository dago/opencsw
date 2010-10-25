GARNAME = xlrd
GARVERSION = 0.7.1
CATEGORIES = python
PACKAGES = CSWpy-xlrd
CATALOGNAME = py_xlrd
LICENSE = xlrd/licences.py
ARCHALL_CSWpy-xlrd = 1

DESCRIPTION = Library for developers to extract data from Microsoft Excel (tm) spreadsheet files
define BLURB
  Extract data from new and old Excel spreadsheets on any platform.
  Pure Python (2.1 to 2.6). Strong support for Excel dates. Unicode-aware.
endef

# 1st char of GARNAME is the directory name
MASTER_SITE_DIR = $(echo GARNAME | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(GARNAME)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
