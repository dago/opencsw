# $Id$
NAME = ZConfig
VERSION = 3.0.3
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Structured Configuration Library
define BLURB
  ZConfig is a configuration library intended for general use. It supports a
  hierarchical schema-driven configuration model that allows a schema to specify
  data conversion routines written in Python. ZConfig's model is very different
  from the model supported by the ConfigParser module found in Python's standard
  library, and is more suitable to configuration-intensive applications.
endef

MASTER_SITES = http://pypi.python.org/packages/source/Z/ZConfig/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWpy-zconfig
CATALOGNAME = py_zconfig

LICENSE = LICENSE.txt
ARCHALL = 1

# tests need zope.testrunner
TEST_SCRIPTS =

# /usr/local is only an example here
CHECKPKG_OVERRIDES_CSWpy-zconfig += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ZConfig-3.0.3-py2.6.egg-info/PKG-INFO
CHECKPKG_OVERRIDES_CSWpy-zconfig += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/ZConfig-3.0.3-py2.7.egg-info/PKG-INFO

include gar/category.mk
