# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = django
VERSION = 1.8.2
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A high-level Python Web framework
define BLURB
  Django is a high-level Python Web framework that encourages rapid development
  and clean, pragmatic design.

  Developed four years ago by a fast-moving online-news operation, Django was
  designed to handle two challenges: the intensive deadlines of a newsroom and
  the stringent requirements of the experienced Web developers who wrote it. It
  lets you build high-performing, elegant Web applications quickly.
endef

#MASTER_SITES = http://www.djangoproject.com/download/$(VERSION)/tarball/
MASTER_SITES += https://www.djangoproject.com/m/releases/1.8/
DISTNAME = Django-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.djangoproject.com/

# Django 1.8 only supports Python 2.7:
#   https://docs.djangoproject.com/en/1.8/faq/install/#what-python-version-can-i-use-with-django
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWpy-django
SPKG_DESC_CSWpy-django = A high-level Python Web framework
# PKGFILES is catchall
ARCHALL_CSWpy-django = 1

# /usr/share/zoneinfo
CHECKPKG_OVERRIDES_CSWpy-django += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/django/conf/__init__.py

# Django 1.8 only supports Python 2.7, see above
CHECKPKG_OVERRIDES_CSWpy-django += python-package-missing-py26-files

# /opt/csw/lib/python2.6/site-packages/django/contrib/auth/hashers.py 
# likes to import test/signals.py
# https://code.djangoproject.com/ticket/20349
MERGE_EXCLUDE_CATEGORY = 

include gar/category.mk
