# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = vobject
VERSION = 0.8.1c
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python library for parsing and generating vCard and vCalendar files
define BLURB
  Long description
endef

MASTER_SITES = http://vobject.skyhouseconsulting.com/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-vobject
ARCHALL_CSWpy-vobject = 1
RUNTIME_DEP_PKGS +=CSWpy-dateutil
CHECKPKG_OVERRIDES_CSWpy-vobject += surplus-dependency|CSWpy-dateutil

include gar/category.mk

