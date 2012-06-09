#####################################################################
# OpenCSW build recipe for links
#
# Author: Yann Rouillard <yann@pleiades.fr.eu.org>
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = links
VERSION = 1.03
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Text-based WWW browser
define BLURB
   Textbased browser with frames, ssl, and menus
endef

PACKAGES = CSWlinks

RUNTIME_DEP_PKGS_CSWlinks += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlinks += CSWlibz1

###### Upstream and opencsw files information #######

MASTER_SITES = http://www.jikos.cz/~mikulas/links/download/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += changelog.CSW


##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)


include gar/category.mk

