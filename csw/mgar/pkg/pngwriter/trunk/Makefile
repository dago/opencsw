NAME = pngwriter
VERSION = 0.5.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A C++ library for creating PNG images
define BLURB

endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://pngwriter.sourceforge.net

LICENSE = doc/english/LICENSE 

PACKAGES = CSWpngwriter CSWpngwriterdevel CSWpngwriterdoc
#PACKAGES += CSWpy-pngwriter
CATALOGNAME_CSWpngwriter = pngwriter
CATALOGNAME_CSWpngwriterdevel = pngwriter_devel
CATALOGNAME_CSWpngwriterdoc = pngwriter_doc
#CATALOGNAME_CSWpy-pngwriter = py_pngwriter
SPKG_DESC_CSWpngwriter = $(DESCRIPTION)
SPKG_DESC_CSWpngwriterdevel = $(DESCRIPTION) - developer package
SPKG_DESC_CSWpngwriterdoc = $(DESCRIPTION) - documentation package
#SPKG_DESC_CSWpy-pngwriter = $(DESCRIPTION) - Python bindings

RUNTIME_DEP_PKGS_CSWpngwriter = CSWggettextrt CSWiconv
RUNTIME_DEP_PKGS_CSWpngwriterdevel = CSWpngwriter
RUNTIME_DEP_PKGS_CSWpngwriterdoc = CSWpngwriter
#RUNTIME_DEP_PKGS_CSWpy-pngwriter = CSWpngwriter CSWpython

PKGFILES_CSWpngwriterdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWpngwriterdoc = $(sharedstatedir)/gtk-doc/.*
#PKGFILES_CSWpy-pngwriter = $(libdir).*/python/site-packages/.*

ARCHALL_CSWpngwriterdoc = 1

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=69758
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = Makefiles.diff

#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)

CONFIGURE_SCRIPT =
TEST_TARGET = 

include gar/category.mk
