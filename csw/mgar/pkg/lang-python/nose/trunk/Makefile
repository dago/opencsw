# $Id$

NAME = nose
VERSION = 1.3.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Nose extends unittest to make testing easier
define BLURB
  Nose collects tests from unittest.TestCase subclasses. But you can
  also write simple test functions, as well as test classes that are not
  subclasses of unittest.TestCase. nose also supplies a number of
  helpful functions for writing timed tests, testing for exceptions, and
  other common use cases.
endef

VENDOR_URL = https://github.com/nose-devs/nose
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWpy-nose
SPKG_DESC = $(DESCRIPTION)

TEST_SCRIPTS =
# tests fail because some multiprocessing module doesn't like Solaris sem_open
# TEST_SCRIPTS = $(WORKSRC)/selftest.py

LICENSE = lgpl.txt
ARCHALL = 1

include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)$(datadir)/man/man1
	gmv -v $(DESTDIR)$(prefix)/man/man1/nosetests.1 $(DESTDIR)$(datadir)/man/man1
	grmdir -v $(DESTDIR)$(prefix)/man/man1
	grmdir -v $(DESTDIR)$(prefix)/man
	@$(MAKECOOKIE)
