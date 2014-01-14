# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gthumb
# VERSION = 2.10.12
VERSION = 2.12.4
SUBDIR=$(basename $(VERSION))
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = Image organizer
define BLURB
  gThumb is an image viewer and browser for the GNOME Desktop. It also includes an importer tool for transferring photos from cameras.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/gthumb/$(SUBDIR)/
DISTFILES  = $(NAME)-$(VERSION).tar.xz

GARCOMPILER = GCC4
# GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
STRIP_LIBTOOL = 1
# PATCHFILES += 0001-configure.ac.patch
# PATCHFILES += mkdtemp-patch

BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibgconf-dev
BUILD_DEP_PKGS += CSWlibexif-dev 
BUILD_DEP_PKGS += CSWlibunique-dev   
BUILD_DEP_PKGS += CSWlibharfbuzz-dev
# BUILD_DEP_PKGS += CSWlibsoupdevel 
# BUILD_DEP_PKGS += CSWgnomekeyring-dev

PACKAGES += CSWgthumb-dev
CATALOGNAME_CSWgthumb-dev = gthumb_dev
PKGFILES_CSWgthumb-dev += $(PKGFILES_DEVEL)
SPKG_DESC_CSWgthumb-dev += $(DESCRIPTION), header files

PACKAGES += CSWgthumb-data
CATALOGNAME_CSWgthumb-data = gthumb_data
PKGFILES_CSWgthumb-data += $(sharedstatedir)/gthumb/.* # $(call catalogname,$P)
PKGFILES_CSWgthumb-data += $(sharedstatedir)/gnome/.*
PKGFILES_CSWgthumb-data += $(sharedstatedir)/icons/.*
PKGFILES_CSWgthumb-data += $(sharedstatedir)/locale/.*
PKGFILES_CSWgthumb-data += $(sharedstatedir)/applications/.*
PKGFILES_CSWgthumb-data += $(sysconfdir)/gconf/schemas/.*
SPKG_DESC_CSWgthumb-data += $(DESCRIPTION), arch-independent files
ARCHALL_CSWgthumb-data = 1

PACKAGES += CSWgthumb
CATALOGNAME_CSWgthumb = gthumb
SPKG_DESC_CSWgthumb += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgthumb += CSWgthumb-data
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibz1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibsoup-gnome2-4-1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibsoup2-4-1

EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/var/lib.*
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpango1-0-0
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpng15-15
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnome-keyring0
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgstreamer0-10-0
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibsoup-gnome2-4-1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibunique1-0-0
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgstinterfaces0-10-0
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgcc-s1
# RUNTIME_DEP_PKGS_CSWgthumb += CSWlibsoup2-4-1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpangocairo1-0-0
CHECKPKG_OVERRIDES_CSWgthumb += surplus-dependency|CSWgthumb-extensions
CHECKPKG_OVERRIDES_CSWgthumb += surplus-dependency|CSWgthumb-data
OBSOLETED_BY_CSWgthumb += CSWlibgthumb

# for xmllint
EXTRA_TEST_ENV += http_proxy=http://proxy:3128

EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-gnome-3
# xmllint failed because of missing variable malrng in gnome-doc-utils.pc
SKIPTEST = 1

include gar/category.mk

# pre-configure-modulated:
# 	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
# 	cd $(WORKSRC) && aclocal
# 	cd $(WORKSRC) && autoconf --force
# 	cd $(WORKSRC) && automake -a -c -f
# 	@$(MAKECOOKIE)

PATH:=/opt/csw/gnu:$(PATH)
