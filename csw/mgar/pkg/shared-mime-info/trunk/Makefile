NAME = shared-mime-info
VERSION = 0.71
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
DISTFILES    = $(NAME)-$(VERSION).tar.bz2

# This is because CSWlibglib2-0-0 is only available on Solaris 10+
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS = CSWgnulinks

PACKAGES = CSWsharedmimeinfo
CATALOGNAME = shared_mime_info

SPKG_SOURCEURL = http://freedesktop.org/Software/shared-mime-info

RUNTIME_DEP_PKGS = CSWggettextrt CSWlibxml2 CSWlibglib2-0-0

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
