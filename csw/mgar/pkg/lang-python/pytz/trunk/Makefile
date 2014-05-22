# $Id$
NAME = pytz
VERSION = 2014.3
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Pytz brings the Olson timezone database into Python.
define BLURB
  pytz brings the Olson tz database into Python. This library allows
  accurate and cross platform timezone calculations using Python 2.3
  or higher. It also solves the issue of ambiguous times at the end
  of daylight savings, which you can read more about in the Python
  Library Reference (datetime.tzinfo).
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2
VENDOR_URL = http://$(NAME).sourceforge.net/
PACKAGES = CSWpy-tz

LICENSE = LICENSE.txt
ARCHALL = 1

include gar/category.mk
