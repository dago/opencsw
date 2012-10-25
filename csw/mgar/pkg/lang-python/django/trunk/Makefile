# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# A known issue: There's a problem with getpass.getpass() on Solaris, in which
# it echoes the entered password.
# http://bugs.python.org/issue7208

NAME = django
VERSION = 1.2.3
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

MASTER_SITES = http://www.djangoproject.com/download/$(VERSION)/tarball/
DISTFILES  = $(DISTNAME).tar.gz
PACKAGES = CSWpy-django
CATALOGNAME_CSWpy-django = py_django
ARCHALL = 1
UFILES_REGEX = Django-(\d+(?:\.\d+)*).tar.gz
DISTNAME = Django-$(VERSION)
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

include gar/category.mk

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)
