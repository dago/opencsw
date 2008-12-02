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
MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxmlstarlet,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = $(GARNAME)-$(GARVERSION)-cc.patch

include gar/category.mk

CONFIGURE_ENV += LIBXML_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXML_CFLAGS="$(shell $(bindir)/xml2-config --cflags)"
CONFIGURE_ENV += LIBXML_LIBS="$(shell $(bindir)/xml2-config --libs)"
CONFIGURE_ENV += LIBXSLT_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXSLT_CFLAGS="$(shell $(bindir)/xslt-config --cflags)"
CONFIGURE_ENV += LIBXSLT_LIBS="$(shell $(bindir)/xslt-config --libs) -lexslt"

CONFIGURE_ARGS = $(DIRPATHS)

post-install:
	@echo " ==> Renaming program to xmlstarlet"
	@mv $(DESTDIR)$(prefix)/bin/xml $(DESTDIR)$(prefix)/bin/xmlstarlet
	@$(MAKECOOKIE)
