# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = django
GARVERSION = 1.1.1
CATEGORIES = python

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

MASTER_SITES = http://www.djangoproject.com/download/$(GARVERSION)/tarball/
DISTFILES  = Django-$(GARVERSION).tar.gz
PACKAGES = CSWpy-django
CATALOGNAME_CSWpy-django = py_django
# In case someone has an old version from testing
INCOMPATIBLE_PKGS = CSWdjango
ARCHALL = 1
UFILES_REGEX = Django-(\d+(?:\.\d+)*).tar.gz
WORKSRC = $(WORKDIR)/Django-$(GARVERSION)
REQUIRED_PKGS =
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWpython-devel
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
# There's a problem that the download URL of the Django source tarball does not
# contain the file name. The browser is being redirected instead. Hard-coding
# the URL and using a custom target to fit the rest of mGAR.
http//www.djangoproject.com/download/$(GARVERSION)/tarball/Django-$(GARVERSION).tar.gz:
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) http://www.djangoproject.com/download/$(GARVERSION)/tarball

include gar/category.mk

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)
