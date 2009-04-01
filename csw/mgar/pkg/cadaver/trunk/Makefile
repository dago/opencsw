#####################################################################
# OpenCSW build recipe for cadaver
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

GARNAME = cadaver
GARVERSION = 0.23.2
CATEGORIES = net

DESCRIPTION = WebDAV commandline tool
define BLURB
 cadaver is a command-line WebDAV client. It supports resource upload/download/display, namespace 
 operations (copy/move), collection deletion/creation, property manipulation, and locking operations.
endef

PACKAGES = CSWcadav

REQUIRED_PKGS = CSWggettextrt CSWiconv CSWneon CSWosslrt CSWreadline CSWzlib CSWgcrypt CSWgnutls CSWgpgerr



###### Upstream and opencsw files information #######

MASTER_SITES = http://www.webdav.org/cadaver/
UPSTREAM_MASTER_SITES = http://www.webdav.org/cadaver/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWcadav.prototype
DISTFILES += changelog.CSW

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz


##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-nls

TEST_SCRIPTS =

include gar/category.mk

post-merge:
	@ginstall -D $(DOWNLOADDIR)/changelog.CSW $(PKGROOT)$(docdir)/$(GARNAME)/changelog.CSW

