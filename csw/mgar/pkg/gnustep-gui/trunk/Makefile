# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-gui
VERSION = 0.24.0
GARTYPE = v2

DESCRIPTION = GNUstep-core gui
define BLURB
  GNUstep-core gui framework, which provides all AppKit classes except the backend dependent. Necessary for all graphical and application-oriented development.
endef

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibgif-dev
BUILD_DEP_PKGS += libgnutls_dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibsndfile-dev
BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibaspell-dev

RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgif4
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibobjc4
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibicui18n54
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibsndfile1
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibao4
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibicudata54
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibaspell15
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgcrypt20

#this is by design
CHECKPKG_OVERRIDES_CSWgnustep-gui += surplus-dependency|CSWgnustep-make

CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR
CHECKPKG_OVERRIDES_CSWgnustep-gui += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker

#these come from our bundles
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/gclose
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Tools/gcloseall
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/gcloseall
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/make_services
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/set_show_service
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Tools/gopen
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Tools/set_show_service
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/gopen
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker
CHECKPKG_OVERRIDES_CSWgnustep-gui += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0

#we don't bind directly right now and thus shut-up the warnings. GNUstep.sh takes care of this at runtime
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput|is|not|directly|bound|to|soname|libao.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|is|not|directly|bound|to|soname|libcups.so.2
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile|is|not|directly|bound|to|soname|libsndfile.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libgif.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libicuuc.so.54
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libjpeg.so.7
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libpng15.so.15
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|is|not|directly|bound|to|soname|libtiff.so.5
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|is|not|directly|bound|to|soname|libaspell.so.15
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gclose|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gclose|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gcloseall|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gcloseall|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gcloseall|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gopen|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gopen|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/gopen|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/make_services|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/make_services|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/make_services|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/set_show_service|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/set_show_service|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/set_show_service|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-gui += no-direct-binding|/opt/csw/GNUstep/System/Tools/set_show_service|is|not|directly|bound|to|soname|libobjc.so.4


#we don't care about placement
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/set_show_service|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/gclose|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/gopen|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/gcloseall|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/make_services|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/ColorPickers/StandardPicker.bundle/StandardPicker|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/ColorPickers/NamedPicker.bundle/NamedPicker|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/ColorPickers/WheelPicker.bundle/WheelPicker|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/Sndfile.nssound/Sndfile|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/TextConverters/RTFConverter.bundle/RTFConverter|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/libgmodel.bundle/libgmodel|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/AudioOutput.nssound/AudioOutput|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSLPR.bundle/GSLPR|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/GSPrinting/GSCUPS.bundle/GSCUPS|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Libraries/libgnustep-gui.so.0.24.0|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-gui += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Services/GSspell.service/GSspell|arch_id=18|arch_name=sparcv8+




#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

# now special targets for configure, build and install so that we can source
# GNUstep.sh before
CONFIGURE_SCRIPTS = sourcegs
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = none
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

configure-sourcegs:
	$(CONFIGURE_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
