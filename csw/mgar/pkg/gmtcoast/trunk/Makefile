# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gmtcoast
VERSION = 2.1.0
CATEGORIES = apps
DESCRIPTION = Coastline Definition Files for Generic Mapping Tools
define BLURB
Support data for the Generic Mapping Tools (GMT) including GSHHS coastlines, rivers, and political boundaries.
endef

SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
MASTER_SITES = ftp://ftp.iris.washington.edu/pub/gmt/ ftp://ftp.soest.hawaii.edu/gmt/ ftp://gd.tuwien.ac.at/pub/gmt/

DISTFILES  = GSHHS$(VERSION)_coast.tar.bz2 \
	     GSHHS$(VERSION)_full.tar.bz2 \
	     GSHHS$(VERSION)_high.tar.bz2 

UFILES_REGEX = GSHHS(\d+(?:\.\d+)*)_(.*).tar.gz

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

PACKAGES += CSWgmtcoast-low
CATALOGNAME_CSWgmtcoast-low = gmtcoast_low
SPKG_DESC_CSWgmtcoast-low = Low resolution coastlines for the Generic Mapping Tools (GMT)
#PKGFILES_CSWgmtcoast-low += /opt/csw/share/coast/.*_[cli]\.cdf

PACKAGES += CSWgmtcoast-high
CATALOGNAME_CSWgmtcoast-high = gmtcoast_high
SPKG_DESC_CSWgmtcoast-high = High resolution coastlines for the Generic Mapping Tools (GMT)
PKGFILES_CSWgmtcoast-high += /opt/csw/share/coast/.*_h\.cdf

PACKAGES += CSWgmtcoast-full
CATALOGNAME_CSWgmtcoast-full = gmtcoast_full
SPKG_DESC_CSWgmtcoast-full = Full resolution coastlines for the Generic Mapping Tools (GMT)
PKGFILES_CSWgmtcoast-full += /opt/csw/share/coast/.*_f\.cdf

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	@rm -rf $(DESTDIR)$(datadir)/coast
	@ginstall -d $(DESTDIR)$(datadir)/coast
	@cp -r $(WORKSRC)/share/coast/* $(DESTDIR)$(datadir)/coast/
	@$(MAKECOOKIE)
