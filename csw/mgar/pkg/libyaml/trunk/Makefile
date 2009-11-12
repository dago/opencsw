# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libyaml
GARVERSION = 0.1.3
CATEGORIES = lib
DESCRIPTION = a YAML 1.1 parser and emitter written in C
define BLURB
endef
SPKG_SOURCEURL = http://pyyaml.org/wiki/LibYAML?version=20
MASTER_SITES = http://pyyaml.org/download/libyaml/
DISTFILES  = yaml-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
WORKSRC = $(WORKDIR)/yaml-$(GARVERSION)
include gar/category.mk
