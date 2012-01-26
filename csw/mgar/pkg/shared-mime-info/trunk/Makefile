NAME = shared-mime-info
VERSION = 0.71
CATEGORIES = lib
GARTYPE = v2

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

# This is for replacing /usr/local/share by /opt/csw/share in the
# default XDG_DATA_DIRS
PATCHFILES += 0001-Set-default-XDG_DATA_DIRS-to-opt-csw-share.patch

# This is because CSWlibglib2-0-0 is only available on Solaris 10+
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS = CSWgnulinks

PACKAGES = CSWsharedmimeinfo
CATALOGNAME = shared_mime_info
CHECKPKG_OVERRIDES  = catalogname-does-not-match-pkgname|pkgname=CSWsharedmimeinfo|catalogname=shared_mime_info|expected-catalogname=sharedmimeinfo

# /usr/local does no harm here
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/mime/mime.cache
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/mime/magic
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/mime/packages/freedesktop.org.xml
# My patch does deliberately not remove /usr/share
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/share|root/opt/csw/bin/update-mime-database

SPKG_SOURCEURL = http://freedesktop.org/Software/shared-mime-info

RUNTIME_DEP_PKGS += CSWlibglib2-0-0 CSWlibintl8 CSWlibxml2-2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
