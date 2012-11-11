# $Id$
#
# NOTE: This build description is not used.  The released CSWcommon package is
# built from a different source.

NAME = cswcommon
VERSION = 1.5
GARTYPE = v2

DESCRIPTION = Installs some useful standard CSW filesystem symlinks and files
define BLURB
endef

#MASTER_SITES = http://mirror.opencsw.org/opencsw/current/$(shell uname -p)/5.8
MASTER_SITES = http://mirror.opencsw.org/opencsw/current/sparc/5.8/
DISTFILES  = common-1.5,REV=2010.12.11-SunOS5.8-sparc-CSW.pkg

PACKAGES = common

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
