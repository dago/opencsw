NAME = exempi
VERSION = 2.1.1
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWexempi CSWexempidevel
CATALOGNAME_CSWexempi = exempi
CATALOGNAME_CSWexempidevel = exempi_devel
SPKG_DESC_CSWexempi = Exempi is an implementation of XMP
SPKG_DESC_CSWexempidevel = Exempi is an implementation of XMP - developer package

RUNTIME_DEP_PKGS_CSWexempi += CSWexpat CSWstlport CSWzlib CSWiconv
RUNTIME_DEP_PKGS_CSWexempidevel += CSWexempi

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWexempi)
BUILD_DEP_PKGS += CSWboostrt CSWboostdevel

PKGFILES_CSWexempidevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://libopenraw.freedesktop.org/wiki/Exempi

PATCHFILES += Makefiles.patch
PATCHFILES += RIFF_Support.cpp
PATCHFILES += XML_Node.cpp
PATCHFILES += configure.patch
PATCHFILES += exempi.cpp.patch
PATCHFILES += utils.cpp.patch
PATCHFILES += xmp.h.patch
PATCHFILES += boost.m4.patch

EXTRA_CXXFLAGS = -D__EXTENSIONS__ -library=stlport4
# Ugly, but need to owerwrite this since autoconf system doesn't work
EXTRA_CXXFLAGS += -DHAVE_NATIVE_TLS=0
# Autoconf doesn't find iconv, the rest is found but not runpath
EXTRA_LINKER_FLAGS = -liconv -lexpat -lz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-boost=/opt/csw

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; autoconf)
	@$(MAKECOOKIE)
