GARNAME = neon29
GARVERSION = 0.29.5
DISTNAME = neon-$(GARVERSION)
CATEGORIES = lib

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/neon/
DISTFILES  = $(DISTNAME).tar.gz

DEP_PKGS = CSWexpat CSWosslrt CSWzlib CSWggettextrt CSWpakchois CSWlibproxy CSWkrb5lib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(DISTNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat
CONFIGURE_ARGS = --with-libproxy --with-packchois

TEST_TARGET = check

include gar/category.mk
