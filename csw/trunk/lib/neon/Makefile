GARNAME = neon
#GARVERSION = 0.25.3
GARVERSION = 0.24.7
CATEGORIES = lib

DESCRIPTION = HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWneon.gspec

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-expat

include ../category.mk
