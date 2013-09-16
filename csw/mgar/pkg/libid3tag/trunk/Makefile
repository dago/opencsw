NAME = libid3tag
VERSION = 0.15.1
REV = b
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library for reading and (eventually) writing ID3 tags
define BLUECTRB
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)$(REV).tar.gz
DISTFILES += id3tag.pc-GARCOMPILER = GCC4

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)$(REV)

RUNTIME_DEP_PKGS = CSWlibz1EP_PKGS = CSWzlib

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)_rev=$(REV)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	@ginstall $(WORKDIR)/id3tag.pc-$(MEMORYMODEL) $(DESTDIR)$(libdir)/pkgconfig/id3tag.pc