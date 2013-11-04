# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tracker
VERSION = 0.16.3
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
# BUILD_DEP_PKGS += CSWexempidevel
BUILD_DEP_PKGS += CSWlibexif-dev

RUNTIME_DEP_PKGS_CSWtracker += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtracker += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibglib2-dev # for glib-compile-schemas
# RUNTIME_DEP_PKGS_CSWtracker += CSWexempi
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-miner0-16-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-extract0-16-0
RUNTIME_DEP_PKGS_CSWtracker += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWtracker += CSWdbus
RUNTIME_DEP_PKGS_CSWtracker += CSWdconf
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWtracker_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWtracker += $(RUNTIME_DEP_PKGS_CSWtracker_$(GARCH))

RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibicudata51
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_sparc += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0 += $(RUNTIME_DEP_PKGS_CSWlibtracker-sparql0-16-0_$(GARCH))

RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibexif12
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibiptcdata
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibpoppler-glib8
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += CSWlibtracker-common
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_sparc += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_sparc += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_sparc += CSWlibicudata51
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_sparc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0 += $(RUNTIME_DEP_PKGS_CSWlibtracker-extract0-16-0_$(GARCH))

RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-miner0-16-0 += CSWlibtracker-common

RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-miner0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-extract0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS_CSWlibtracker-dev += CSWlibtracker-common

RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtracker-common += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibtracker-common_sparc += CSWlibicudata51
RUNTIME_DEP_PKGS_CSWlibtracker-common_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtracker-common += $(RUNTIME_DEP_PKGS_CSWlibtracker-common_$(GARCH))

PATCHFILES += 0001-Force-linking-with-CC-not-CXX.patch
PATCHFILES += 0003-Replace-uuid_unparse_lower-with-uuid_unparse.patch
PATCHFILES += 0004-_XOPEN_SOURCE-hides-non-standard-stuff-__EXTENSIONS_.patch
PATCHFILES += 0005-exempi-xmp.h-is-missing-a-stdbool.h-include.patch
# Submitted upstream, should be in 0.16.4
PATCHFILES += 0002-strnlen-replacement-function.patch

# Packages
PACKAGES += CSWtracker
SPKG_DESC_CSWtracker = $(DESCRIPTION)
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWdbus
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWdconf
CHECKPKG_OVERRIDES_CSWtracker += surplus-dependency|CSWlibglib2-dev

PACKAGES += CSWlibtracker-common
SPKG_DESC_CSWlibtracker-common += $(DESCRIPTION), libtracker-common
PKGFILES_CSWlibtracker-common += $(call pkgfiles_lib,tracker-0.16/libtracker-common.so.0)
PKGFILES_CSWlibtracker-common += $(call pkgfiles_lib,tracker-0.16/libtracker-data.so.0)

PACKAGES += CSWlibtracker-extract0-16-0
SPKG_DESC_CSWlibtracker-extract0-16-0 += $(DESCRIPTION), libtracker-extract-0.16.so.0
PKGFILES_CSWlibtracker-extract0-16-0 += $(call pkgfiles_lib,libtracker-extract-0.16.so.0)
PKGFILES_CSWlibtracker-extract0-16-0 += $(call baseisadirs,$(libdir),tracker-0\.16/extract-modules/libextract-.*\.so)

PACKAGES += CSWlibtracker-miner0-16-0
SPKG_DESC_CSWlibtracker-miner0-16-0 += $(DESCRIPTION), libtracker-miner-0.16.so.0
PKGFILES_CSWlibtracker-miner0-16-0 += $(call pkgfiles_lib,libtracker-miner-0.16.so.0)

PACKAGES += CSWlibtracker-sparql0-16-0
SPKG_DESC_CSWlibtracker-sparql0-16-0 += $(DESCRIPTION), libtracker-sparql-0.16.so.0
PKGFILES_CSWlibtracker-sparql0-16-0 += $(call pkgfiles_lib,libtracker-sparql-0.16.so.0)

PACKAGES += CSWlibtracker-dev
SPKG_DESC_CSWlibtracker-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibtracker-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibtracker-dev += $(call baseisadirs,$(libdir),tracker-0\.16/libtracker-common\.so)
PKGFILES_CSWlibtracker-dev += $(call baseisadirs,$(libdir),tracker-0\.16/libtracker-data\.so)
PKGFILES_CSWlibtracker-dev += $(datadir)/vala/vapi/tracker-.*

# For gettext
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

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

# after spending a day trying to figure out why all these libs are linked unneededly only on SPARC
# I gave up and applied the overrides
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-mplayer.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-mp3.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-jpeg.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-icon.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-html.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-gif.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libxml2.so.2|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-epub.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libtracker-common.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-epub.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-epub.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libgsf-1.so.114|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-epub.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libgobject-2.0.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-epub.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libtracker-common.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-dvi.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-dvi.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-abw.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libthread.so.1|is|needed|by|/opt/csw/lib/libtracker-extract-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/libtracker-extract-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/lib/libtracker-extract-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/lib/libtracker-extract-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libicudata.so.51|is|needed|by|/opt/csw/lib/libtracker-extract-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-msoffice-xml.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libtracker-common.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-msoffice-xml.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-msoffice.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libxml2.so.2|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-msoffice.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libgobject-2.0.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-oasis.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libgsf-1.so.114|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-oasis.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-oasis.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libtracker-common.so.0|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-oasis.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libxml2.so.2|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-oasis.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libcairo.so.2|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-pdf.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-pdf.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-png.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-ps.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-text.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-tiff.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/extract-modules/libextract-totem.so|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0 += $(CHECKPKG_OVERRIDES_CSWlibtracker-extract0-16-0_$(GARCH))
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-control|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-control|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libtracker-sparql-0.16.so.0|is|needed|by|/opt/csw/bin/tracker-control|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-import|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-import|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-info|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-info|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-search|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-search|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-sparql|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-sparql|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-stats|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-stats|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/bin/tracker-tag|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/bin/tracker-tag|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/libexec/tracker-extract|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/libexec/tracker-extract|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libthread.so.1|is|needed|by|/opt/csw/libexec/tracker-extract|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libz.so.1|is|needed|by|/opt/csw/libexec/tracker-extract|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/libexec/tracker-miner-fs|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/libexec/tracker-miner-fs|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libthread.so.1|is|needed|by|/opt/csw/libexec/tracker-miner-fs|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/libexec/tracker-store|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/libexec/tracker-store|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libthread.so.1|is|needed|by|/opt/csw/libexec/tracker-store|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/libexec/tracker-writeback|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/libexec/tracker-writeback|but|never|used
CHECKPKG_OVERRIDES_CSWtracker_sparc += soname-unused|libthread.so.1|is|needed|by|/opt/csw/libexec/tracker-writeback|but|never|used
CHECKPKG_OVERRIDES_CSWtracker += $(CHECKPKG_OVERRIDES_CSWtracker_$(GARCH))
CHECKPKG_OVERRIDES_CSWlibtracker-common_sparc += soname-unused|libicudata.so.51|is|needed|by|/opt/csw/lib/tracker-0.16/libtracker-data.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-common_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/tracker-0.16/libtracker-data.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-common_sparc += soname-unused|libz.so.1|is|needed|by|/opt/csw/lib/tracker-0.16/libtracker-data.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-common += $(CHECKPKG_OVERRIDES_CSWlibtracker-common_$(GARCH))
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libicudata.so.51|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libicui18n.so.51|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libicuuc.so.51|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libintl.so.8|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libsqlite3.so.0|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_sparc += soname-unused|libz.so.1|is|needed|by|/opt/csw/lib/libtracker-sparql-0.16.so.0.1600.3|but|never|used
CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0 += $(CHECKPKG_OVERRIDES_CSWlibtracker-sparql0-16-0_$(GARCH))

include gar/category.mk
