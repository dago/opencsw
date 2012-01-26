# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gmtcoast
VERSION = 2.2.0
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = Coastline Definition Files for the Generic Mapping Tools (GMT)
define BLURB
Support data for the Generic Mapping Tools (GMT) including GSHHS coastlines, rivers, and political boundaries.
endef

SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
MASTER_SITES = ftp://ftp.soest.hawaii.edu/gmt/ ftp://gd.tuwien.ac.at/pub/gmt/

DISTFILES  = gshhs-$(VERSION).tar.bz2 

UFILES_REGEX = gshhs-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

LICENSE = LICENSE.TXT

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

# This should match value in gmt/trunk/Makefile
datadir = /opt/csw/share/gmt

## The tarballs just dump into the current directory
WORKSRC = $(WORKDIR)

OBSOLETED_BY_CSWgmtcoast += CSWgmtcoast-low
OBSOLETED_BY_CSWgmtcoast += CSWgmtcoast-high
OBSOLETED_BY_CSWgmtcoast += CSWgmtcoast-full

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	@rm -rf $(DESTDIR)$(datadir)/coast
	@ginstall -d $(DESTDIR)$(datadir)/coast
	@cp -r $(WORKSRC)/share/coast/* $(DESTDIR)$(datadir)/coast/
	@$(MAKECOOKIE)
