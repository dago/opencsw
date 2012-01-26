NAME = librsync
VERSION = 0.9.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library with the rolling-checksum algorithm known from rsync
define BLURB
  librsync implements the rolling-checksum algorithm of remote file
  synchronization that was popularized by the rsync utility and is used in
  rproxy. This algorithm transfers the differences between 2 files without
  needing both files on the same system.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWlibrsync += CSWbzip2
RUNTIME_DEP_PKGS_CSWlibrsync += CSWlibpopt
RUNTIME_DEP_PKGS_CSWlibrsync += CSWzlib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += --enable-static=no

# delta.c contains inlined functions without storage qualifiers, treat them
# as static as the only references are within delta.c itself. Otherwise the
# linking will fail to resolve those references. See "inline functions"
#   http://docs.sun.com/app/docs/doc/820-7598/6nirjunib?a=view
EXTRA_CFLAGS = -features=no%extinl

include gar/category.mk
