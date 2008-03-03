GARNAME = neon
GARVERSION = 0.26.3
CATEGORIES = lib

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

# Compatibility libraries
LIBNAME = libneon.so
COMPATVERS = 24.0.7 25.0.5
COMPATLIBS = $(foreach A,i386 sparc, \
                 $(foreach V,$(COMPATVERS),$(LIBNAME).$(V).$(A).bz2))

MASTER_SITES = http://www.webdav.org/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWneon,$(ADMSTANDARD))
DISTFILES += $(call admfiles,CSWneon-devel,$(ADMSTANDARD))
#DISTFILES += $(COMPATLIBS)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat

include gar/category.mk

#post-install: install-compat-libs

install-compat-libs:
	@echo $(DISTFILES)
	@for version in $(COMPATVERS) ; do \
		ginstall -m 755 $(WORKDIR)/$(LIBNAME).$$version.$(GARCH) \
			$(DESTDIR)$(libdir)/$(LIBNAME).$$version ; \
	done
	@$(MAKECOOKIE)
