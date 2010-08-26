# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = debian-vote
GARVERSION = 0.8
PACKAGES = CSWdebian-vote
CATALOGNAME_CSWdebian-vote = debian_vote
CATEGORIES = apps
DESCRIPTION = Condorcet voting algorithm
define BLURB
endef
SPKG_SOURCEURL = http://seehuhn.de/pages/vote
MASTER_SITES = http://seehuhn.de/media/programs/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
ARCHALL_CSWdebian-vote = 1
include gar/category.mk
