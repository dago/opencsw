# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = slack
VERSION = 0.15.2
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = A glorified wrapper around rsync
define BLURB
endef
SPKG_SOURCEURL = http://code.google.com/p/slack/
MASTER_SITES = $(GOOGLE_MIRROR)
PATCHFILES  = 0001-OpenCSW-layout.patch
PATCHFILES += 0002-use-OpenCSW-perl.patch
PATCHFILES += 0003-gen_config_file-with-OpenCSW-perl.patch
PATCHFILES += 0004-use-etc-opt-csw-slack.conf.patch
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
RUNTIME_DEP_PKGS_CSWslack += CSWperl
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
ARCHALL_CSWslack = 1
include gar/category.mk
