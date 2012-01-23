NAME = libid3tag
VERSION = 0.15.1
REV = b
CATEGORIES = lib

DESCRIPTION = A library for reading and (eventually) writing ID3 tags
define BLURB
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)$(REV).tar.gz
DISTFILES += id3tag.pc-32 id3tag.pc-64

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)$(REV)

RUNTIME_DEP_PKGS = CSWzlib

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)_rev=$(REV)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	@ginstall $(WORKDIR)/id3tag.pc-$(MEMORYMODEL) $(DESTDIR)$(libdir)/pkgconfig/id3tag.pc
	@$(MAKECOOKIE)
