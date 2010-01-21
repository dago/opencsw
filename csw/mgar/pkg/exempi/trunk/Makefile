GARNAME = exempi
GARVERSION = 2.1.1
CATEGORIES = lib

DESCRIPTION = Exempi is an implementation of XMP
define BLURB
	Exempi is an implementation of XMP. Version 2.x is based on Adobe XMP SDK
	4.1.1 and released under a BSD-style license like Adobe's. The 3 clause
	BSD (aka New-BSD) license is compatible with GPL. The licensing is kept
	identical in order to allow two-way merging of the code (ie sending our
	change to the XMP SDK to Adobe for integration).

	The API is C based and means to be used from any language and be easier
	to maintain ABI stability. 
endef

MASTER_SITES = http://libopenraw.freedesktop.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS += CSWexpat CSWstlport CSWzlib
PREREQUISITE_PKGS += CSWiconv CSWboostrt CSWboostdevel

PATCHFILES += Makefiles.patch
PATCHFILES += RIFF_Support.cpp
PATCHFILES += XML_Node.cpp
PATCHFILES += configure.patch
PATCHFILES += exempi.cpp.patch
PATCHFILES += utils.cpp.patch
PATCHFILES += xmp.h.patch
PATCHFILES += boost.m4.patch

EXTRA_CXXFLAGS = -D__EXTENSIONS__ -library=stlport4 -DHAVE_NATIVE_TLS=0
EXTRA_LINKER_FLAGS = -liconv

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-boost=/opt/csw

TEST_TARGET = check

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; autoconf)
	@$(MAKECOOKIE)
