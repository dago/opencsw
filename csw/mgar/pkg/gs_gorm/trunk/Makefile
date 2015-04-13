# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gorm
VERSION = 1.2.20
GARTYPE = v2

DESCRIPTION = GNUstep graphical interface builder
define BLURB
  GORM (Graphical Object Relationship Modeller) is GNUstep Interface Builder equivalent to build graphically interface files.
endef

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/dev-apps/
DISTFILES  = $(DISTNAME).tar.gz


BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWgorm += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgorm += CSWlibobjc4


CHECKPKG_OVERRIDES_CSWgorm += CSWgnustep-make
CHECKPKG_OVERRIDES_CSWgorm += CSWgnustep-base
CHECKPKG_OVERRIDES_CSWgorm += CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWgorm += CSWgnustep-back


#overrides
CHECKPKG_OVERRIDES_CSWgnustep-base += surplus-dependency|CSWgnustep-make

#we don't care about placement
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Libraries/libGorm.so.1.1.0|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Libraries/libGormCore.so.1.2.20|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgorm += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Libraries/libGormObjCHeaderParser.so.1.1.0|arch_id=18|arch_name=sparcv8+


#we know bundles miss soname
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus
CHECKPKG_OVERRIDES_CSWgorm += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers


#we don't directly bind currently
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libGorm.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libGormCore.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libGormPrefs.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Gorm|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGorm.so.1.1.0|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGorm.so.1.1.0|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGormCore.so.1.2.20|is|not|directly|bound|to|soname|libGormObjCHeaderParser.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGormObjCHeaderParser.so.1.1.0|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgorm += no-direct-binding|/opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Xib.plugin/Xib
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGorm.so.1.1.0
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGorm.so.1.1.0
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/4Data.palette/4Data
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libGormObjCHeaderParser.so.1|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libGormObjCHeaderParser.so.1|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGormCore.so.1.2.20
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libGorm.so.1|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGormObjCHeaderParser.so.1.1.0
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libGormCore.so.1|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/0Menus.palette/0Menus
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/1Windows.palette/1Windows
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGormObjCHeaderParser.so.1.1.0
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Gorm.plugin/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/2Controls.palette/2Controls
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libGormPrefs.so.1|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Gorm
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/3Containers.palette/3Containers
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/Nib.plugin/Nib
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Libraries/libGormPrefs.so.1.2.20
CHECKPKG_OVERRIDES_CSWgorm += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Applications/Gorm.app/Resources/GModel.plugin/GModel


#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)


# now special targets for build and install so that we can source
# GNUstep.sh before
# configure is skipped
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = 
SKIPTEST ?= 1

include gar/category.mk

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) &&. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
