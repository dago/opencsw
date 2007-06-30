GARNAME = xmlstarlet
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = XML transformation utility
define BLURB
  XMLStarlet is a set of command line utilities (tools)
  to transform, query, validate, and edit XML documents
  and files using simple set of shell commands in similar
  way it is done for text files with UNIX grep, sed, awk,
  diff, patch, join, etc utilities.
endef

SF_PROJ = xmlstar
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxmlstarlet,)

PATCHFILES = $(GARNAME)-$(GARVERSION)-cc.patch

pre-configure:
	@echo " ==> Reconfiguring"
	@(cd $(WORKSRC); autoreconf -fi)
	@$(MAKECOOKIE)

#CONFIGURE_ARGS = $(DIRPATHS) --with-libxml-prefix=$(prefix) --with-libxslt-prefix=$(prefix) --with-libiconf-prefix=$(prefix)
CONFIGURE_ARGS = $(DIRPATHS) 

include ../category.mk
