# $Id$
NAME = cdrdao
VERSION = 1.2.3
GARTYPE = v2

DESCRIPTION = CD recording in DAO mode
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

# TBD: X GUI, requires gtkmm2 and libguimm2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --without-xdao
# May use external scglib later
CONFIGURE_ARGS += --with-scglib=yes

include gar/category.mk
