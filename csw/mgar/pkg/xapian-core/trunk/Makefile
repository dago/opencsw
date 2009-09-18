GARNAME = xapian-core
GARVERSION = 1.0.12
CATEGORIES = lib

DESCRIPTION = An open source search engine library
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(GARVERSION)/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxapiancore
CATALOGNAME_CSWxapiancore = xapian_core

REQUIRED_PKGS = CSWstlport CSWzlib

EXTRA_LD_FLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_ARGS = AM_CXXFLAGS="-library=stlport4 -features=tmplife"

TEST_TARGET = check

# We need the .la-file, otherwise xapian-config doesn't work
MERGE_EXCLUDE_LIBTOOL =

include gar/category.mk
