GARNAME = xmlto
GARVERSION = 0.0.20
CATEGORIES = utils

DESCRIPTION = 
define BLURB
endef

MASTER_SITES = http://cyberelk.net/tim/data/$(GARNAME)/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxmlto)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mktemp=/opt/csw/bin/mktemp
CONFIGURE_ARGS += --with-find=/opt/csw/bin/gfind
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-getopt=/opt/csw/bin/ggetopt

include gar/category.mk

# We need this for 'tail -n'
PATH := /usr/xpg4/bin:/opt/csw/bin:$(PATH)
