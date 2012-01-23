NAME = polkit
VERSION = 0.96
CATEGORIES = lib

DESCRIPTION = PolicyKit
define BLURB
	Exempi is an implementation of XMP. Version 2.x is based on Adobe XMP SDK
	4.1.1 and released under a BSD-style license like Adobe's. The 3 clause
	BSD (aka New-BSD) license is compatible with GPL. The licensing is kept
	identical in order to allow two-way merging of the code (ie sending our
	change to the XMP SDK to Adobe for integration).

	The API is C based and means to be used from any language and be easier
	to maintain ABI stability. 
endef

MASTER_SITES = http://cgit.freedesktop.org/PolicyKit/snapshot/
DISTNAME  = PolicyKit-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

UFILES_REGEX = PolicyKit-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpolkit CSWpolkitdevel
CATALOGNAME_CSWpolkit = polkit
CATALOGNAME_CSWpolkitdevel = polkit_devel
SPKG_DESC_CSWpolkit = polkit is an implementation of XMP
SPKG_DESC_CSWpolkitdevel = polkit is an implementation of XMP - developer package

RUNTIME_DEP_PKGS_CSWpolkit += CSWexpat CSWstlport CSWzlib CSWiconv
RUNTIME_DEP_PKGS_CSWpolkitdevel += CSWpolkit

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWpolkit)

PKGFILES_CSWpolkitdevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://libopenraw.freedesktop.org/wiki/polkit

CONFIGURE_SCRIPTS += $(WORKSRC)/autogen.sh
#CONFIGURE_SCRIPTS += $(WORKSRC)/configure

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

#pre-configure-modulated:
#	@echo " ==> Regenerating build tools..."
#	@( cd $(WORKSRC) ; "NOCONFIGURE=1" ./autogen.sh )
#	@$(MAKECOOKIE)

#pre-configure-modulated:
#	@echo " ==> Regenerating build tools..."
#	@(cd $(WORKSRC) ; \
#		aclocal                       && \
#		autoconf                      && \
#		libtoolize --automake --force && \
#		aclocal                       && \
#		automake -a )
#	@$(MAKECOOKIE)
