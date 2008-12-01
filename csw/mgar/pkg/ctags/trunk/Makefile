GARNAME = ctags
GARVERSION = 5.5.4
CATEGORIES = utils

DESCRIPTION =  Exuberant ctags
define BLURB
  Ctags generates an index (or tag) file of language objects found in source
  files that allows these items to be quickly and easily located by a text
  editor or other utility. A tag signifies a language object for which an index
  entry is available (or, alternatively, the index entry created for that
  object).
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWctags.gspec CSWctags.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Respect DESTDIR
PATCHFILES += install.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-custom-config=$(sysconfdir)/ctags.conf

# No test suite
TEST_SCRIPTS =

include gar/category.mk
