# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-base
VERSION = 1.24.7
GARTYPE = v2

DESCRIPTION = GNUstep-core base
define BLURB
  GNUstep-core base framework, which provides all Foundation equivalent classes, useful for all non-gui objective-c development. A prerequisite for all GNUstep tools as well as applications.
endef

MASTER_SITES += ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES += $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibgnutls-dev
BUILD_DEP_PKGS += CSWlibxml2-dev CSWlibxslt-dev
BUILD_DEP_PKGS += CSWlibiconv-dev

RUNTIME_DEP_PKGS_CSWgnustep-base += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibobjc4
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibffi5
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibiconv2

#overrides
CHECKPKG_OVERRIDES_CSWgnustep-base += surplus-dependency|CSWgnustep-make
CHECKPKG_OVERRIDES_CSWgnustep-base += file-with-bad-content|/usr/local|root/opt/csw/GNUstep/System/Library/Libraries/gnustep-base/Versions/1.24/Resources/NSTimeZones/README

#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc

#PATCHFILES += 0001-configure-tweak-align.patch

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

EXTRA_RUNPATH_DIRS = /opt/csw/GNUstep/System/Library/Libraries

#we disable linker maps (needed for gnutls)
# LINKER_MAPS =

# now special targets for configure, build and install so that we can source
# GNUstep.sh before
CONFIGURE_SCRIPTS = sourcegs
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = 
SKIPTEST ?= 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

configure-sourcegs:
	$(CONFIGURE_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

