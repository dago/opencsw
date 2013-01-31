# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = iniparse
VERSION = 0.4
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = CSWiniparse is an iniparser for Python
define BLURB
  CSWiniparse is an iniparser for Python which is API compatible with the standard library's ConfigParser, preserves structure of INI files (order of sections & options, indentation, comments, and blank lines are preserved when data is updated), and is more convenient to use.
endef

MASTER_SITES = http://pypi.python.org/packages/source/i/iniparse/
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE

BUILD_DEP_PKGS = CSWpython
RUNTIME_DEP_PKGS = CSWpython

PACKAGES = CSWpy-iniparse

GARCOMPILER = SOS12U3
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)
ARCHALL=1

CHECKPKG_OVERRIDES_CSWpy-iniparse += dependency-listed-more-than-once|CSWpython

include gar/category.mk

