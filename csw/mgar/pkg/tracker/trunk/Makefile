# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tracker
VERSION = 1.0.0
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
DISTFILES += CSWtracker.postinstall
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
BUILD_DEP_PKGS += CSWlibiptcdata
BUILD_DEP_PKGS += CSWpoppler-dev
BUILD_DEP_PKGS += CSWlibexif-dev
BUILD_DEP_PKGS += CSWlibmediaart-dev
BUILD_DEP_PKGS += CSWpm-xml-parser
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWfontconfig-dev CSWlibfreetype-dev CSWxproto CSWsunx11devel CSWintltool

PATCHFILES += 0003-Replace-uuid_unparse_lower-with-uuid_unparse.patch
PATCHFILES += 0004-_XOPEN_SOURCE-hides-non-standard-stuff-__EXTENSIONS_.patch
PATCHFILES += 0005-exempi-xmp.h-is-missing-a-stdbool.h-include.patch

# Packages
PACKAGES += CSWtracker
SPKG_DESC_CSWtracker = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-control1-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-sparql1-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-miner1-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-extract
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWtracker += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWtracker += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtracker += CSWlibpoppler-glib8
RUNTIME_DEP_PKGS_CSWtracker += CSWlibiptcdata
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgif4
RUNTIME_DEP_PKGS_CSWtracker += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWtracker += CSWdbus
RUNTIME_DEP_PKGS_CSWtracker += CSWdconf
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibexif12
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWtracker += $(RUNTIME_DEP_PKGS_CSWtracker_$(GARCH))
# For glib-compile-shemas
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWlibglib2-dev
# Tracker needs dbus
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWdbus
# Configuration backend for Gnome stuff, used by Tracker and dbus
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWdconf

PACKAGES += CSWlibtracker-common
SPKG_DESC_CSWlibtracker-common += $(DESCRIPTION), libtracker-common
PKGFILES_CSWlibtracker-common += $(call pkgfiles_lib,tracker-1.0/libtracker-common.so.0)
PKGFILES_CSWlibtracker-common += $(call pkgfiles_lib,tracker-1.0/libtracker-data.so.0)
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibiptcdata
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibexif12
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtracker-common_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibtracker-common += $(RUNTIME_DEP_PKGS_CSWlibtracker-common_$(GARCH))

PACKAGES += CSWlibtracker-extract
SPKG_DESC_CSWlibtracker-extract += $(DESCRIPTION), libtracker-extract
PKGFILES_CSWlibtracker-extract += $(call pkgfiles_lib,tracker-1.0/libtracker-extract.so.0)
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibtracker-sparql1-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibiptcdata
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibexif12
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-extract += CSWlibglib2-0-0

PACKAGES += CSWlibtracker-miner1-0-0
SPKG_DESC_CSWlibtracker-miner1-0-0 += $(DESCRIPTION), libtracker-miner-1.0.so.0
PKGFILES_CSWlibtracker-miner1-0-0 += $(call pkgfiles_lib,libtracker-miner-1.0.so.0)
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibtracker-sparql1-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0 += $(RUNTIME_DEP_PKGS_CSWlibtracker-miner1-0-0_$(GARCH))

PACKAGES += CSWlibtracker-sparql1-0-0
SPKG_DESC_CSWlibtracker-sparql1-0-0 += $(DESCRIPTION), libtracker-sparql-1.0.so.0
PKGFILES_CSWlibtracker-sparql1-0-0 += $(call pkgfiles_lib,libtracker-sparql-1.0.so.0)
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0 += $(RUNTIME_DEP_PKGS_CSWlibtracker-sparql1-0-0_$(GARCH))

PACKAGES += CSWlibtracker-control1-0-0
SPKG_DESC_CSWlibtracker-control1-0-0 += $(DESCRIPTION), libtracker-control-1.0.so.0
PKGFILES_CSWlibtracker-control1-0-0 += $(call baseisadirs,$(libdir),libtracker-control-1\.0\.so\.0\.0\.0)
PKGFILES_CSWlibtracker-control1-0-0 += $(call baseisadirs,$(libdir),libtracker-control-1\.0\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0 += $(RUNTIME_DEP_PKGS_CSWlibtracker-control1-0-0_$(GARCH))

PACKAGES += CSWlibtracker-dev
SPKG_DESC_CSWlibtracker-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibtracker-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibtracker-dev += $(call baseisadirs,$(libdir),tracker-1\.0/libtracker-common\.so)
PKGFILES_CSWlibtracker-dev += $(call baseisadirs,$(libdir),tracker-1\.0/libtracker-data\.so)
PKGFILES_CSWlibtracker-dev += $(call baseisadirs,$(libdir),tracker-1\.0/libtracker-extract\.so)
PKGFILES_CSWlibtracker-dev += $(datadir)/vala/vapi/tracker-.*
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-control1-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-sparql1-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-miner1-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-extract

# For gettext
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

# For xproto and stuff
PKG_CONFIG_DIRS += /opt/csw/X11/lib/pkgconfig/

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-tracker-fts
CONFIGURE_ARGS += --disable-unit-tests
CONFIGURE_ARGS += --disable-hal
# FIXME: re-enable introspection? afair requires vala
CONFIGURE_ARGS += --disable-introspection
CONFIGURE_ARGS += --disable-playlist
CONFIGURE_ARGS += --disable-nautilus-extension
# exempi links with stlport while glib links with libCstd, both at once are incomp.
# and both would be linked at once in libtracker-extract, so we have to disable it
CONFIGURE_ARGS += --disable-exempi
# not needed
CONFIGURE_ARGS += --disable-miner-thunderbird
CONFIGURE_ARGS += --disable-miner-firefox


include gar/category.mk
