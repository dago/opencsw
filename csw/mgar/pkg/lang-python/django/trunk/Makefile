# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = django
VERSION = 1.6.1
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
SPKG_SOURCEURL = http://www.djangoproject.com/
# UFILES_REGEX = Django-(\d+(?:\.\d+)*).tar.gz

MASTER_SITES = http://www.djangoproject.com/download/$(VERSION)/tarball/
DISTFILES  = $(DISTNAME).tar.gz
DISTNAME = Django-$(VERSION)

PACKAGES = CSWpy-django
CATALOGNAME_CSWpy-django = py_django
ARCHALL = 1
# /opt/csw/lib/python2.6/site-packages/django/contrib/auth/hashers.py 
# likes to import test/signals.py
# https://code.djangoproject.com/ticket/20349
MERGE_EXCLUDE_CATEGORY = 

RUNTIME_DEP_PKGS =
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpython-dev

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
LICENSE = LICENSE
# There's a problem that the download URL of the Django source tarball does not
# contain the file name. The browser is being redirected instead. Hard-coding
# the URL and using a custom target to fit the rest of mGAR.
http//www.djangoproject.com/download/$(VERSION)/tarball/Django-$(VERSION).tar.gz:
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) http://www.djangoproject.com/download/$(VERSION)/tarball
	pwd
	mv $(DOWNLOADDIR)/partial/tarball $(DOWNLOADDIR)/partial/$(DISTFILES)

CHECKPKG_OVERRIDES_CSWpy-django += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/django/conf/__init__.py
CHECKPKG_OVERRIDES_CSWpy-django += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/django/conf/__init__.py

include gar/category.mk

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)
