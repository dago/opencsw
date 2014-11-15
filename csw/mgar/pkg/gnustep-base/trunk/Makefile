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

BUILD_DEP_PKGS_CSWgnustep-base = CSWgmake CSWgcc4objc CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-base = CSWgnustep-make

BUILD_DEP_PKGS_CSWgnustep-base += CSWlibffi-dev
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibffi5 

BUILD_DEP_PKGS_CSWgnustep-base += CSWlibicu-dev
RUNTIME_DEP_PGKS_CSWgnustep-base += CSWlibicui18n52 CSWlibicuuc52 CSWlibicudata52

RUNTIME_DEP_PGKS_CSWgnustep-base += CSWlibobjc4 CSWlibgcc-s1 CSWlibgmp10

BUILD_DEP_PKGS_CSWgnustep-base += CSWlibgnutls-dev
RUNTIME_DEP_PGKS_CSWgnustep-base += CSWlibssl1-0-0 CSWlibgnutls28 CSWlibgcrypt20

BUILD_DEP_PKGS_CSWgnustep-base += CSWlibxml2-dev CSWlibxslt-dev
RUNTIME_DEP_PGKS_CSWgnustep-base += CSWlibxslt1 CSWlibxml2-2
BUILD_DEP_PKGS_CSWgnustep-base += CSWlibiconv-dev
RUNTIME_DEP_PKGS_CSWgnustep-base += CSWlibiconv2


MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz



#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc

#PATCHFILES += 0001-configure-tweak-align.patch

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

EXTRA_RUNPATH_DIRS = /opt/csw/GNUstep/System/Library/Libraries

#we disable linker maps (needed for gnutls)
LINKER_MAPS =

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
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) ; $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) ; $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)

#overrides
CHECKPKG_OVERRIDES_CSWgnustep-base += surplus-dependency|CSWgnustep-make
CHECKPKG_OVERRIDES_CSWgnustep-base += file-with-bad-content|/usr/local|root/opt/csw/GNUstep/System/Library/Libraries/gnustep-base/Versions/1.24/Resources/NSTimeZones/README
