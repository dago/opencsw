GARNAME = xapian-core
GARVERSION = 1.0.11
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

PACKAGES = CSWxapian CSWxapianrt CSWxapiandevel
CATALOGNAME_CSWxapian = xapian
CATALOGNAME_CSWxapianrt = xapian_rt
CATALOGNAME_CSWxapiandevel = xapian_devel

SPKG_DESC_CSWxapian = An open source search engine library
SPKG_DESC_CSWxapianrt = Xapian runtime libraries
SPKG_DESC_CSWxapiandevel = Xapian development files
REQUIRED_PKGS_CSWxapianrt = CSWstlport CSWzlib
REQUIRED_PKGS_CSWxapian = CSWxapianrt
REQUIRED_PKGS_CSWxapiandevel = CSWxapian

# If we compile with Sun Studio it is impossible to build the Ruby bindings as
# Ruby is compiled with GCC.
# Compiling with GCC4 yields the error "__sync_fetch_and_add_4 not found".
GARCOMPILER = GCC3

EXTRA_LD_FLAGS = -lm

# GCC3 can not build amd64
#BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

#BUILD_ARGS = AM_CXXFLAGS="-library=stlport4 -features=tmplife"

TEST_TARGET = check

# We need the .la-file, otherwise xapian-config doesn't work
MERGE_EXCLUDE_LIBTOOL =

PKGFILES_CSWxapianrt = $(PKGFILES_RT)
PKGFILES_CSWxapiandevel = $(PKGFILES_DEVEL)
PKGFILES_CSWxapiandevel += $(docdir)/xapian-core/apidoc/.*

include gar/category.mk
