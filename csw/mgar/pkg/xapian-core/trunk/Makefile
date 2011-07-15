NAME = xapian-core
VERSION = 1.2.6
CATEGORIES = lib

DESCRIPTION = An open source search engine library
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(VERSION)/

DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Fix-include-issue-on-Solaris-9.patch

PACKAGES += CSWxapian
CATALOGNAME_CSWxapian = xapian
SPKG_DESC_CSWxapian = An open source search engine library
RUNTIME_DEP_PKGS_CSWxapian += CSWxapianrt

PACKAGES += CSWxapianrt
CATALOGNAME_CSWxapianrt = xapian_rt
SPKG_DESC_CSWxapianrt = Xapian runtime libraries
PKGFILES_CSWxapianrt = $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWxapianrt += CSWstlport
RUNTIME_DEP_PKGS_CSWxapianrt += CSWzlib

PACKAGES += CSWxapian-dev
SPKG_DESC_CSWxapian-dev = Xapian development files
PKGFILES_CSWxapian-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWxapian-dev += $(docdir)/xapian-core/apidoc/.*
RUNTIME_DEP_PKGS_CSWxapian-dev += CSWxapian

# If we compile with Sun Studio it is impossible to build the Ruby bindings as
# TBD: Still true?

# TBD: Is this necessary
EXTRA_LD_FLAGS = -lm

BUILD64 = 1

# Can't we just pass this via EXTRA_CXXFLAGS?
BUILD_ARGS = AM_CXXFLAGS="-library=stlport4 -features=tmplife"

# We need the .la-file, otherwise xapian-config doesn't work
MERGE_EXCLUDE_LIBTOOL =

include gar/category.mk
