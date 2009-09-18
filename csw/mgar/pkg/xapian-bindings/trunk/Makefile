GARNAME = xapian-bindings
GARVERSION = 1.0.11
CATEGORIES = lib

DESCRIPTION = Xapian bindings for SWIG and JNI
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(GARVERSION)/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxapianbindings
CATALOGNAME_CSWxapianbindings = xapian_bindings

REQUIRED_PKGS = CSWxapiancore CSWstlport

#EXTRA_LD_FLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

#BUILD_ARGS = AM_CXXFLAGS="-library=stlport4 -features=tmplife"

TEST_TARGET = check

include gar/category.mk
