# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cfg2html
VERSION = 1.14
PATCHLEVEL = r1.8
CATEGORIES = utils
GARTYPE = v2
DESCRIPTION = Configuration documentation generator
define BLURB
endef
SPKG_SOURCEURL = http://tech.groups.yahoo.com/group/cfg2html/
MASTER_SITES = http://tech.groups.yahoo.com/group/cfg2html/files/sun/
DISTFILES  = $(NAME)-sun_$(VERSION)$(PATCHLEVEL).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = cfg2html
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/$(NAME)
ARCHALL = 1

install-cfg2html:
	ginstall -d $(DESTDIR)$(datadir)/$(NAME)/plugins
	ginstall -d $(DESTDIR)$(datadir)/$(NAME)/doc
	(\
	cd $(WORKSRC); \
	for d in plugins doc html; do \
		ginstall -d $(DESTDIR)$(datadir)/$(NAME)/$${d}; \
		for f in plugins/*; do \
			ginstall $${f} $(DESTDIR)$(datadir)/$(NAME)/$${d}; \
		done; \
	done; \
	)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/cfg2html_sun.sh $(DESTDIR)$(bindir)

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PATCHLEVEL)
