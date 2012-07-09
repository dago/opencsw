# $Id$

NAME = kakasi
VERSION = 2.3.4
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = KAnji KAna Simple Inverter
define BLURB
  KAnji KAna Simple Inverter
endef

MASTER_SITES = http://kakasi.namazu.org/stable/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
