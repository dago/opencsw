GARNAME = shared-mime-info
GARVERSION = 0.70
CATEGORIES = lib

DESCRIPTION = Freedesktop.org common MIME database
define BLURB
  The shared-mime-info package contains the core database of common types and
  the *update-mime-database* command used to extend it. It requires glib2 to be
  installed for building the update command. Additionally, it uses intltool for
  translations, though this is only a dependency for the maintainers. This
  database is translated at Transifex.
endef

MASTER_SITES = http://freedesktop.org/~hadess/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://freedesktop.org/Software/shared-mime-info

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

