GARNAME = libxml2
GARVERSION = 2.6.30
CATEGORIES = lib

DESCRIPTION = Libxml2 is the XML C parser and toolkit developed for the Gnome project
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES   += $(call admfiles,CSWpylibxml2,depend)
DISTFILES   += $(call admfiles,CSWlibxml2,depend)
#DISTFILES   += $(call admfiles,CSWlibxml2devel,depend)

# We don't have 64 bit Python yet
CONFIGURE_ARGS_32 = --with-python=$(prefix)
CONFIGURE_ARGS_64 = --without-python

CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1

NO_ISAEXEC = 1
MERGE_EXCLUDE_FILES = .*\.la

#PKGFILES_CSWlibxml2devel_EXCLUSIVE  = $(PKGFILES_DEVEL)
#PKGFILES_CSWlibxml2devel_EXCLUSIVE += $(docdir)/libxml2-$(GARVERSION)/.*
#PKGFILES_CSWlibxml2devel_EXCLUSIVE += $(sharedstatedir)/gtk-doc/.*
#PKGFILES_CSWlibxml2devel_EXCLUSIVE += $(libdir)/xml2Conf.sh
#PKGFILES_CSWlibxml2devel_EXCLUSIVE += $(call isadirs,$(libdir),xml2Conf.sh)

#PKGFILES_CSWpylibxml2_EXCLUSIVE  = $(libdir)/python/.*
#PKGFILES_CSWpylibxml2_EXCLUSIVE += $(docdir)/libxml2-python-$(GARVERSION)/.*

include ../category.mk

