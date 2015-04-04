# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-make
VERSION = 2.6.6
GARTYPE = v2

DESCRIPTION = GNUstep-core make
define BLURB
  GNUstep-core make infrastructure and configuration files. Needed for all GNUstep setups.
endef

BUILD_DEP_PKGS = CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWgtar

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

#we override this, it is harmless, it is for Debian only
CHECKPKG_OVERRIDES_CSWgnustep-make += file-with-bad-content|/usr/share|root/opt/csw/GNUstep/System/Library/Makefiles/deb-equivs-control.template

#we have no tests anyway
SKIPTEST = 1

prefix = $(BUILD_PREFIX)/GNUstep

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-layout=gnustep 
CONFIGURE_ARGS += --with-config-file=/etc/opt/csw/GNUstep/GNUstep.conf
CONFIGURE_ARGS += TAR=gtar
#CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"

PRESERVECONF += $(sysconfdir)/installation-domains.conf

include gar/category.mk

post-install:
	( ginstall -D -m 0644 $(WORKSRC)/installation-domains.conf $(DESTDIR)$(sysconfdir)/installation-domains.conf )
