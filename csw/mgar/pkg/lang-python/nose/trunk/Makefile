GARNAME = nose
GARVERSION = 0.11.2
CATEGORIES = python

DESCRIPTION = Nose extends unittest to make testing easier
define BLURB
  Nose collects tests from unittest.TestCase subclasses. But you can
  also write simple test functions, as well as test classes that are not
  subclasses of unittest.TestCase. nose also supplies a number of
  helpful functions for writing timed tests, testing for exceptions, and
  other common use cases.
endef

MASTER_SITES = http://somethingaboutorange.com/mrl/projects/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpy-nose
CATALOGNAME = py_nose
SPKG_DESC = $(DESCRIPTION)

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =
# tests fail because some multiprocessing module doesn't like Solaris sem_open
# TEST_SCRIPTS = $(WORKSRC)/selftest.py

LICENSE = lgpl.txt
ARCHALL = 1

include gar/category.mk

INSTALL_ARGS += --install-data=$(prefix)/share
