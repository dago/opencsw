NAME = libcddb
VERSION = 1.3.2
CATEGORIES = lib

DESCRIPTION = A C library to access data on a CDDB server
define BLURB
  Libcddb supports both the custom CDDB protocol and tunnelling the query
  and read operations over plain HTTP. It is also possible to use an HTTP
  proxy server. If you want to speed things up, you can make use of the
  built-in caching facility provided by the library.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibcddb CSWlibcddbutil

SPKG_DESC_CSWlibcddb = A C library to access data on a CDDB server
SPKG_DESC_CSWlibcddbutil = A CDDB query tool

RUNTIME_DEP_PKGS_CSWlibcddbutil = CSWlibcddb CSWlibcdio

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

http_proxy='$(http_proxy)'
EXTRA_TEST_EXPORTS = http_proxy

export http_proxy
PKGFILES_CSWlibcddbutil = $(bindir)/.*

include gar/category.mk
