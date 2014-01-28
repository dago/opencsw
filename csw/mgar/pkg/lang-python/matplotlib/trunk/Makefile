# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# This recipe does not build, because the code is in C++, and Python's setup
# script insists on calling the 'cc' binary instead of 'CC'. I don't know how
# to change it.
#
# upstream bug: http://bugs.python.org/issue1250

NAME = matplotlib
VERSION = 1.3.1
CATEGORIES = python
CATALOGNAME = py_matplotlib

DESCRIPTION = Python 2D plotting library
define BLURB
  Matplotlib is a python 2D plotting library which produces publication
  quality figures in a variety of hardcopy formats and interactive
  environments across platforms. matplotlib can be used in python scripts,
  the python and ipython shell, web application servers, and six
  graphical user interface toolkits.
endef

SPKG_SOURCEURL = http://matplotlib.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE/LICENSE

BUILD_DEP_PKGS = CSWpython27-dev

RUNTIME_DEP_PKGS = CSWlibatk
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWpng
RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWzlib

PATCHFILES += 0001-avoid-reserved-variable-names.patch
MODULATIONS_PYTHON_VERSION = 2_7
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_MERGE_EXCLUDE_FILES += .*\.egg-info.* .*\.pyo .*\.pyc

pre-configure:
	@rm -f work/build-isa-sparcv8/$(GARNAME)-$(GARVERSION)/lib/$(GARNAME)/tests/baseline_images/test_axes/shaped\ data.svg
	@$(MAKECOOKIE)

include gar/category.mk
