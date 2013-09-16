NAME      = libid3tag
VERSION   = 0.15.1
GARSUBREV = b
GARTYPE  IES = lib
GARTYPE = v2

DESCRIPTION = A library for reading and (eventually) writing ID3 tags
define BLUECTRB
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NGARSUBAME)-$(VERSION)$(REV).tar.gz
DISTFILES += id3tag.pc-GARCOMPILER = GCC4

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)$(GARSUBREV)

RUNTIME_DEP_PKGS = CSWlibz1

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWlibid3tag0
CATALOGNAME_CSWlibid3tag0 = libid3tag0
PKGFILES_CSWlibid3tag0 += $(call baseisadirs,$(libdir),libid3tag\.so\.0\.3\.0)
PKGFILES_CSWlibid3tag0 += $(call baseisadirs,$(libdir),libid3tag\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibid3tag0 += $(DESCRIPTION), libid3tag.so.0
RUNTIME_DEP_PKGS_CSWlibid3tag0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibid3tag0 += CSWlibz1
OBSOLETED_BY_CSWlibid3tag0 += CSWlibid3tag

PACKAGES += CSWlibid3tag-dev
CATALOGNAME_CSWlibid3tag-dev = libid3tag_dev
SPKG_DESC_CSWlibid3tag-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibid3tag-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibid3tag-dev += CSWlibid3tag0

include gar/category.mkRSSPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)RSION)_rev=$(REV)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	@ginstall $(WORKDIR)/id3tag.pc-$(MEMORYMODEL) $(DESTDIR)$(libdir)/pkgconfig/id3tag.pc