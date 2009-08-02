# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = cfg2html
GARVERSION = 1.14r1.8
CATEGORIES = utils
DESCRIPTION = Configuration documentation generator
define BLURB
endef
SPKG_SOURCEURL = http://tech.groups.yahoo.com/group/cfg2html/
MASTER_SITES = http://tech.groups.yahoo.com/group/cfg2html/files/sun/
DISTFILES  = $(GARNAME)-sun_$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = cfg2html
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/$(GARNAME)
ARCHALL = 1

install-cfg2html:
	ginstall -d $(DESTDIR)$(datadir)/$(GARNAME)/plugins
	ginstall -d $(DESTDIR)$(datadir)/$(GARNAME)/doc
	(\
	cd $(WORKSRC); \
	for d in plugins doc html; do \
		ginstall -d $(DESTDIR)$(datadir)/$(GARNAME)/$${d}; \
		for f in plugins/*; do \
			ginstall $${f} $(DESTDIR)$(datadir)/$(GARNAME)/$${d}; \
		done; \
	done; \
	)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/cfg2html_sun.sh $(DESTDIR)$(bindir)

include gar/category.mk
