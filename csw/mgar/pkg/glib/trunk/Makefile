GARNAME = glib
GARVERSION = 1.3.15
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.2.10 1.3.15

DESCRIPTION = Utility library commonly associated with GNOME programs
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists.
endef

GNOME_SUBV_FUNC = $(shell echo $1 | awk -F. '{print $$1"."$$2}')
MASTER_SITES = $(sort $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GNOME_ROOT)/$(GNOME_PROJ)/$(call GNOME_SUBV_FUNC,$(VERSION))/))
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz,$(SOURCEFILES))

DEP_PKGS = CSWggettextrt CSWiconv

# glib 1.x doesn't seem to be 64 bit clean
#BUILD64 = 1
#NOISAEXEC = 1

# Only needed for 1.3.x
SGML_CATALOG_FILES = $(sysconfdir)/sgml/catalog
EXTRA_BUILD_EXPORT-1.3.15 = SGML_CATALOG_FILES
EXTRA_BUILD_EXPORTS = $(EXTRA_BUILD_EXPORT-$(GARVERSION))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

include gar/category.mk
