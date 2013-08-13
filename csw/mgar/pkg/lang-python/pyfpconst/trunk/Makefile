# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = fpconst
VERSION = 0.7.2
PACKAGES = CSWpy-fpconst
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Utilities for handling IEEE 754 floating point special values
SPKG_DESC_CSWpy-fpconst = $(DESCRIPTION)
define BLURB
  This python module implements constants and functions for working with
  IEEE754 double-precision special values.  It provides constants for
  Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
  (NegInf), as well as functions to test for these values.
endef
TEST_SCRIPTS =
ARCHALL_CSWpy-fpconst = 1
LICENSE = README
DISTFILES += changelog.CSW
DISTFILES += $(DISTNAME).tar.gz
OBSOLETED_BY_CSWpy-fpconst = CSWpyfpconst
include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(WORKDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
