GARNAME = neon
GARVERSION = 0.25.5
CATEGORIES = lib

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWneon,$(ADMSTANDARD))
DISTFILES += $(call admfiles,CSWneon-devel,$(ADMSTANDARD))

# Compatibility libraries
DISTFILES += libneon.so.24.0.7.i386.gz
DISTFILES += libneon.so.24.0.7.sparc.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-expat

include ../category.mk

post-install:
	@if test -f $(WORKDIR)/libneon.so.24.0.7.$(GARCH).gz ; then \
		gunzip $(WORKDIR)/libneon.so.24.0.7.$(GARCH).gz ; \
	fi
	@if test -f $(WORKDIR)/libneon.so.24.0.7.$(GARCH) ; then \
		ginstall -m0755 \
			$(WORKDIR)/libneon.so.24.0.7.$(GARCH) \
			$(DESTDIR)$(libdir)/libneon.so.24.0.7 ; \
	fi
	@$(MAKECOOKIE)
