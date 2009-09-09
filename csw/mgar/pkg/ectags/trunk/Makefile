GARNAME = ctags
GARVERSION = 5.8
CATEGORIES = utils

DESCRIPTION = Exuberant Ctags: A multilanguage implementation of Ctags
define BLURB
  Ctags generates an index (or tag) file of language objects found in source
  files that allows these items to be quickly and easily located by a text
  editor or other utility. A tag signifies a language object for which an index
  entry is available (or, alternatively, the index entry created for that
  object).
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 

# Respect DESTDIR
PATCHFILES = install.diff

PACKAGES = CSWectags
CATALOGNAME = ectags

SPKG_SOURCEURL = http://ctags.sourceforge.net/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=6556
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-custom-config=$(sysconfdir)/ctags.conf

# No test suite
TEST_SCRIPTS =

EXTRA_PAX_ARGS = -s ",/ctags,/ectags,p"

include gar/category.mk
