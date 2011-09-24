# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = torque
VERSION = 3.0.2
CATEGORIES = utils
DESCRIPTION = Batch job scheduling system
define BLURB
endef
SPKG_SOURCEURL = 
MASTER_SITES = http://www.clusterresources.com/downloads/torque/
PATCHFILES += 0001-daemonize-function-prototype.patch
DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = GNU
include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
