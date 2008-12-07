GARNAME = libxml2
GARVERSION = 2.7.2
CATEGORIES = lib

DESCRIPTION = XML Parser Library
define BLURB
  Libxml2 is the XML C parser and toolkit developed for the Gnome project.
endef

MASTER_SITES = ftp://xmlsoft.org/libxml2/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWpylibxml2,depend)
DISTFILES   += $(call admfiles,CSWlibxml2,depend)
DISTFILES   += $(call admfiles,CSWlibxml2devel,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# We don't have 64 bit Python yet
CONFIGURE_ARGS_32 = --with-python=$(prefix)
CONFIGURE_ARGS_64 = --without-python

CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1

NO_ISAEXEC = 1
MERGE_EXCLUDE_FILES = .*\.la

PKGFILES_CSWlibxml2devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxml2devel += $(docdir)/libxml2-$(GARVERSION)/.*
PKGFILES_CSWlibxml2devel += $(sharedstatedir)/gtk-doc/.*
PKGFILES_CSWlibxml2devel += $(libdir)/xml2Conf.sh
PKGFILES_CSWlibxml2devel += $(call isadirs,$(libdir),xml2Conf.sh)

PKGFILES_CSWpylibxml2  = $(libdir)/python/.*
PKGFILES_CSWpylibxml2 += $(docdir)/libxml2-python-$(GARVERSION)/.*

include gar/category.mk

