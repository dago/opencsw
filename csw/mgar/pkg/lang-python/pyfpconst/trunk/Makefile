# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = fpconst
VERSION = 0.7.2
PACKAGES = CSWpyfpconst
CATALOGNAME_CSWpyfpconst = py_fpconst
CATEGORIES = python
DESCRIPTION = Utilities for handling IEEE 754 floating point special values
define BLURB
  This python module implements constants and functions for working with
  IEEE754 double-precision special values.  It provides constants for
  Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
  (NegInf), as well as functions to test for these values.
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/fpconst/
MASTER_SITES = http://pypi.python.org/packages/source/f/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
TEST_SCRIPTS =
ARCHALL_CSWpy-fpconst = 1
LICENSE = README
include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
