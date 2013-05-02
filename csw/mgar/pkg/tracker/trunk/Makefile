# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tracker
# Tracker version after this require glib2 >= 2.35.1
VERSION = 0.15.2
GARTYPE = v2

DESCRIPTION = semantic data storage for desktop and mobile devices
define BLURB
  Tracker is a semantic data storage for desktop and mobile devices.
  Tracker uses W3C standards for RDF ontologies using Nepomuk with
  SPARQL to query and update the data.
  Tracker is a central repository of user information, that provides
  two big benefits for the user; shared data between applications
  and information which is relational to other information (for
  example mixing contacts with files, locations, activities and etc.).
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.xz
GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWlibgsf-dev
BUILD_DEP_PKGS += CSWvala
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibsqlite3-dev
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibpopplerdev
BUILD_DEP_PKGS += CSWlibgif-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibicu-devel
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibpng-dev

RUNTIME_DEP_PKGS += CSWlibuuid
RUNTIME_DEP_PKGS += CSWlibgsf
RUNTIME_DEP_PKGS += CSWzlib
RUNTIME_DEP_PKGS += CSWvala
RUNTIME_DEP_PKGS += CSWggettext
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWgio-fam-backend
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWlibsqlite3-0
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWlibz1
RUNTIME_DEP_PKGS += CSWlibpoppler
RUNTIME_DEP_PKGS += CSWlibgif4
RUNTIME_DEP_PKGS += CSWlibjpeg7
RUNTIME_DEP_PKGS += CSWlibtiff3
RUNTIME_DEP_PKGS += CSWlibicu46
RUNTIME_DEP_PKGS += CSWlibpng15-15

PATCHFILES += 0001-Force-linking-with-CC-not-CXX.patch
PATCHFILES += 0003-Replace-uuid_unparse_lower-with-uuid_unparse.patch
PATCHFILES += 0004-_XOPEN_SOURCE-hides-non-standard-stuff-__EXTENSIONS_.patch

# Packages
PACKAGES += CSWlibtracker0-16
PACKAGES += CSWlibtracker-dev
PACKAGES += CSWtracker

# Catalog names
CATALOGNAME_CSWlibtracker0-16 = libtracker0_16
CATALOGNAME_CSWlibtracker-dev = libtracker_dev

# Package descriptions
SPKG_DESC_CSWlibtracker0-16 = Gnome Tracker, libraries
SPKG_DESC_CSWlibtracker-dev = Gnome Tracker, development files
SPKG_DESC_CSWtracker        = Gnome Tracker

# Package payload
PKGFILES_CSWlibtracker0-16 += $(call pkgfiles_lib,libtracker-extract-0.16.so)
PKGFILES_CSWlibtracker0-16 += $(call pkgfiles_lib,libtracker-miner-0.16.so)
PKGFILES_CSWlibtracker0-16 += $(call pkgfiles_lib,libtracker-sparql-0.16.so)
PKGFILES_CSWlibtracker0-16 += $(call baseisadirs,$(libdir),tracker-0\.16/extract-modules/libextract-.*\.so)
PKGFILES_CSWlibtracker0-16 += $(call baseisadirs,$(libdir),tracker-0\.16/libtracker-common\.so.*)
PKGFILES_CSWlibtracker0-16 += $(call baseisadirs,$(libdir),tracker-0\.16/libtracker-data\.so.*)

PKGFILES_CSWlibtracker-dev += $(PKGFILES_DEVEL)

# Inter-package deps
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker0-16
RUNTIME_DEP_PKGS_CSWtracker        += CSWlibtracker0-16

# For gettext
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-tracker-fts
CONFIGURE_ARGS += --disable-unit-tests
CONFIGURE_ARGS += --disable-hal
CONFIGURE_ARGS += --disable-introspection
CONFIGURE_ARGS += --disable-playlist
CONFIGURE_ARGS += --disable-nautilus-extension

TEST_SCRIPTS =

include gar/category.mk

