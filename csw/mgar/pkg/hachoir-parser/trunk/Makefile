# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = hachoir-parser
GARVERSION = 1.2.1
CATEGORIES = python
DESCRIPTION = allows to view and edit a binary stream field by field (core)
define BLURB
  Hachoir is a Python library that allows to view and edit a binary stream
  field by field. In other words, Hachoir allows you to "browse" any binary
  stream just like you browse directories and files. A file is split in a tree
  of fields, where the smallest field is just one bit.
endef
SPKG_SOURCEURL = http://bitbucket.org/haypo/hachoir/wiki/Home
MASTER_SITES = http://cheeseshop.python.org/packages/source/h/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = hachoir_parser
ARCHALL = 1
TEST_SCRIPTS =
include gar/category.mk
