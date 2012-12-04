NAME = gperf
VERSION = 3.0.4
GARTYPE = bts

GARCOMPILER = GNU
COMMON_PKG_DEPENDS =
INCLUDE_COMMONDIRS = 1
CATALOG_RELEASE = bratislava
CHECKPKG_OVERRIDES_CSWgperf += bad-location-of-file
CHECKPKG_OVERRIDES_CSWgperf += disallowed-path
RUNTIME_DEP_PKGS_CSWgperf += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgperf += CSWlibstdc++6
 devel
GARTYPE = v2

DESCRIPTION = A perfect hash function generator
define BLURB
  GNU gperf is a perfect hash function generator. For a given list of strings,
  it produces a hash function and hash table, in form of C or C++ code, for
  looking up a value depending on the input string. The hash function is perfect,
  which means that the hash table has no collisions, and the hash table lookup
  needs a single string comparison only.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

includ