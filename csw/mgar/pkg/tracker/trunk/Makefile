# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tracker
# Tracker version after this require glib2 >= 2.35.1
VERSION = 0.15.2
GARTYPE = v2

DESCRIPTION = Gnome Tracker, semantic data storage
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
BUILD_DEP_PKGS += CSWpoppler-dev
BUILD_DEP_PKGS += CSWlibgif-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibuuid-dev

RUNTIME_DEP_PKGS_CSWtracker += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtracker += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWtracker += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWtracker += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWtracker += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWtracker += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWtracker += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgif4
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-miner0-16-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-extract0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWtracker
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWtracker
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibexif12
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWtracker
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker0-16-dev += CSWlibtracker-miner0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker0-16-dev += CSWtracker
RUNTIME_DEP_PKGS_CSWlibtracker0-16-dev += CSWlibtracker-extract0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker0-16-dev += CSWlibtracker-sparql0-16-0

PATCHFILES += 0001-Force-linking-with-CC-not-CXX.patch
PATCHFILES += 0002-strnlen-replacement-function.patch
PATCHFILES += 0003-Replace-uuid_unparse_lower-with-uuid_unparse.patch
PATCHFILES += 0004-_XOPEN_SOURCE-hides-non-standard-stuff-__EXTENSIONS_.patch

# Packages
PACKAGES += CSWtracker
SPKG_DESC_CSWtracker = $(DESCRIPTION)

PACKAGES += CSWlibtracker-extract0-16-0
SPKG_DESC_CSWlibtracker-extract0-16-0 += $(DESCRIPTION), libtracker-extract-0.16.so.0
PKGFILES_CSWlibtracker-extract0-16-0 += $(call baseisadirs,$(libdir),libtracker-extract-0\.16\.so\.0\.1502\.0)
PKGFILES_CSWlibtracker-extract0-16-0 += $(call baseisadirs,$(libdir),libtracker-extract-0\.16\.so\.0(\.\d+)*)

PACKAGES += CSWlibtracker-miner0-16-0
SPKG_DESC_CSWlibtracker-miner0-16-0 += $(DESCRIPTION), libtracker-miner-0.16.so.0
PKGFILES_CSWlibtracker-miner0-16-0 += $(call baseisadirs,$(libdir),libtracker-miner-0\.16\.so\.0\.1502\.0)
PKGFILES_CSWlibtracker-miner0-16-0 += $(call baseisadirs,$(libdir),libtracker-miner-0\.16\.so\.0(\.\d+)*)

PACKAGES += CSWlibtracker-sparql0-16-0
SPKG_DESC_CSWlibtracker-sparql0-16-0 += $(DESCRIPTION), libtracker-sparql-0.16.so.0
PKGFILES_CSWlibtracker-sparql0-16-0 += $(call baseisadirs,$(libdir),libtracker-sparql-0\.16\.so\.0\.1502\.0)
PKGFILES_CSWlibtracker-sparql0-16-0 += $(call baseisadirs,$(libdir),libtracker-sparql-0\.16\.so\.0(\.\d+)*)

PACKAGES += CSWlibtracker0-16-dev
SPKG_DESC_CSWlibtracker0-16-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibtracker0-16-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibtracker0-16-dev += /opt/csw/lib/libtracker-extract-0.16.so
PKGFILES_CSWlibtracker0-16-dev += /opt/csw/lib/libtracker-miner-0.16.so
PKGFILES_CSWlibtracker0-16-dev += /opt/csw/lib/libtracker-sparql-0.16.so
PKGFILES_CSWlibtracker0-16-dev += /opt/csw/lib/tracker-0.16/libtracker-common.so
PKGFILES_CSWlibtracker0-16-dev += /opt/csw/lib/tracker-0.16/libtracker-data.so



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

