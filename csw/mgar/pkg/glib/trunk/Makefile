NAME = glib
VERSION = 1.3.15
CATEGORIES = lib

EXTRA_MODULATORS = VERSION
MODULATIONS_VERSION = 1.2.10 1.3.15

SKIP_MODULATIONS = isa-sparcv9-version-1.2.10 isa-amd64-version-1.2.10

DESCRIPTION = Utility library commonly associated with GNOME programs
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists.
endef

GNOME_SUBV_FUNC = $(shell echo $1 | awk -F. '{print $$1"."$$2}')
MASTER_SITES = $(sort $(foreach VERSION,$(MODULATIONS_VERSION),$(GNOME_ROOT)/$(GNOME_PROJ)/$(call GNOME_SUBV_FUNC,$(VERSION))/))
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_VERSION), $(NAME)-$(VERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))
PATCHFILES-1.3.15  = 0001-gtkdoc-mkhtml-returns-1-even-on-warnings.patch
PATCHFILES-1.3.15 += 0002-Don-t-break-when-index.sgml-is-not-there.patch
PATCHFILES_isa-i386-version-1.3.15 = $(PATCHFILES-1.3.15)
PATCHFILES_isa-sparcv8-version-1.3.15 = $(PATCHFILES-1.3.15)
PATCHFILES_isa-sparcv9-version-1.3.15 = $(PATCHFILES-1.3.15)

PACKAGES = CSWglib CSWglibdevel

CATALOGNAME_CSWglib = glib
CATALOGNAME_CSWglibdevel = glib_devel

SPKG_DESC_CSWglib = $(DESCRIPTION)
SPKG_DESC_CSWglibdevel = Development files for glib

RUNTIME_DEP_PKGS_CSWglib = CSWggettextrt CSWiconv
RUNTIME_DEP_PKGS_CSWglibdevel = CSWglib
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWglib)

# glib 1.x doesn't seem to be 64 bit clean
BUILD64 = 1

# Only needed for 1.3.x
SGML_CATALOG_FILES = /etc/opt/csw/sgml/catalog
EXTRA_BUILD_EXPORT-1.3.15 = SGML_CATALOG_FILES
EXTRA_BUILD_EXPORTS = $(EXTRA_BUILD_EXPORT-$(VERSION))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# There are three possible harmless tests failing for 1.3.15 64 bit, so skip for now
TEST_SCRIPTS_isa-default-version-1.2.10 = $(WORKSRC)/Makefile
TEST_SCRIPTS_isa-default-version-1.3.15 = $(WORKSRC)/Makefile
TEST_SCRIPTS = $(call modulationvalue,TEST_SCRIPTS)

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

MERGE_SCRIPTS_isa-default-version-1.2.10 = copy-only
MERGE_DIRS_isa-default-version-1.2.10 = $(libdir)
MERGE_SCRIPTS_isa-default-version-1.3.15 = copy-all
MERGE_DIRS_isa-extra-version-1.3.15 = $(libdir)
MERGE_SCRIPTS_isa-extra-version-1.3.15 = copy-relocated-only

PKGFILES_CSWglibdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWglibdevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk
