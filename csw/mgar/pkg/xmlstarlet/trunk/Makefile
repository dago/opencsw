NAME = xmlstarlet
VERSION = 1.0.2
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
MASTER_SITES += http://xmlstar.sourceforge.net/downloads/
DISTFILES = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWiconv CSWlibxml2 CSWlibxslt CSWzlib   

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=66612
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

BUILD64 = 1

CONFIGURE_ENV += LIBXML_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXML_CFLAGS="$(shell $(bindir)/xml2-config --cflags)"
CONFIGURE_ENV += LIBXML_LIBS="$(shell $(bindir)/xml2-config --libs)"
CONFIGURE_ENV += LIBXSLT_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXSLT_CFLAGS="$(shell $(bindir)/xslt-config --cflags)"
CONFIGURE_ENV += LIBXSLT_LIBS="$(shell $(bindir)/xslt-config --libs) -lexslt"

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

CHECKPKG_OVERRIDES_CSWxmlstarlet += soname-not-found|libm.so.2

include gar/category.mk

post-install-modulated:
	@echo " ==> Renaming program to xmlstarlet"
	@mv $(DESTDIR)$(bindir)/xml $(DESTDIR)$(bindir)/xmlstarlet
	@$(MAKECOOKIE)
