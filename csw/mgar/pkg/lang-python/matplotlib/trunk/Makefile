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

RUNTIME_DEP_PKGS = CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS += CSWlibstdc++6
RUNTIME_DEP_PKGS += CSWlibpng15-15
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibfreetype6

CHECKPKG_OVERRIDES_CSWpy-matplotlib += python-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-matplotlib += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/matplotlib/dviread.py
CHECKPKG_OVERRIDES_CSWpy-matplotlib += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/matplotlib/font_manager.py
CHECKPKG_OVERRIDES_CSWpy-matplotlib += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/matplotlib/_mathtext_data.py
CHECKPKG_OVERRIDES_CSWpy-matplotlib += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/matplotlib/tests/test_agg.py
CHECKPKG_OVERRIDES_CSWpy-matplotlib += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/matplotlib/font_manager.py

PATCHFILES += 0001-avoid-reserved-variable-names.patch
MODULATIONS_PYTHON_VERSION = 2_7
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_MERGE_EXCLUDE_FILES += .*\.egg-info.* .*\.pyo .*\.pyc

pre-configure:
	@rm -f work/build-isa-sparcv8/$(GARNAME)-$(GARVERSION)/lib/$(GARNAME)/tests/baseline_images/test_axes/shaped\ data.svg
	@$(MAKECOOKIE)

include gar/category.mk
