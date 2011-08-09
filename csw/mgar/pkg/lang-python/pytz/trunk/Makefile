# $Id$
NAME = pytz
VERSION = 2011h
CATEGORIES = python

DESCRIPTION = Pytz brings the Olson timezone database into Python.
define BLURB
  pytz brings the Olson tz database into Python. This library allows
  accurate and cross platform timezone calculations using Python 2.3
  or higher. It also solves the issue of ambiguous times at the end
  of daylight savings, which you can read more about in the Python
  Library Reference (datetime.tzinfo).
endef

MASTER_SITES = http://pypi.python.org/packages/source/p/pytz/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
SPKG_SOURCEURL = http://$(NAME).sourceforge.net/
PACKAGES = CSWpy-tz
CATALOGNAME = py_tz

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

LICENSE = LICENSE.txt
ARCHALL = 1

include gar/category.mk
