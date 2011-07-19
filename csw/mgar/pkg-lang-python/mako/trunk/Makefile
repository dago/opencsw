# $Id$
NAME = mako
VERSION = 0.4.1
CATEGORIES = python

DESCRIPTION = Fast and lightweight templating for Python
define BLURB
  Mako is a template library written in Python. It provides a familiar,
  non-XML syntax which compiles into Python modules for maximum
  performance. Mako's syntax and API borrows from the best ideas of many
  others, including Django templates, Cheetah, Myghty, and Genshi.
  Conceptually, Mako is an embedded Python (i.e. Python Server Page)
  language, which refines the familiar ideas of componentized layout and
  inheritance to produce one of the most straightforward and flexible
  models available, while also maintaining close ties to Python calling
  and scoping semantics.
endef

VENDOR_URL   = http://www.makotemplates.org/
MASTER_SITES = http://www.makotemplates.org/downloads/
DISTNAME     = $(subst m,M,$(NAME))-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz
DISTFILES   += changelog.CSW

UPSTREAM_MASTER_SITES = http://www.makotemplates.org/download.html

ARCHALL = 1

include gar/category.mk
