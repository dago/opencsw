NAME = autotrace
VERSION = 0.31.1
CATEGORIES = apps

DESCRIPTION = A program for converting bitmap to vector graphics
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://autotrace.sourceforge.net

PACKAGES = CSWautotrace CSWautotracert CSWautotracedevel CSWautotracedoc
CATALOGNAME_CSWautotrace = autotrace
CATALOGNAME_CSWautotracert = autotrace_rt
CATALOGNAME_CSWautotracedevel = autotrace_devel
CATALOGNAME_CSWautotracedoc = autotrace_doc
SPKG_DESC_CSWautotrace = $(DESCRIPTION)
SPKG_DESC_CSWautotracert = $(DESCRIPTION) - runtime package
SPKG_DESC_CSWautotracedevel = $(DESCRIPTION) - developer package
SPKG_DESC_CSWautotracedoc = $(DESCRIPTION) - API documentation package

PKGFILES_CSWautotracedevel = $(PKGFILES_DEVEL)
PKGFILES_CSWautotracert = $(PKGFILES_RT)
PKGFILES_CSWautotracedoc = $(sharedstatedir)/doc/autotrace/.*

RUNTIME_DEP_PKGS_CSWautotrace += CSWautotracert
RUNTIME_DEP_PKGS_CSWautotrace += CSWbzip2
RUNTIME_DEP_PKGS_CSWautotrace += CSWfconfig
RUNTIME_DEP_PKGS_CSWautotrace += CSWftype2
RUNTIME_DEP_PKGS_CSWautotrace += CSWimagemagick
RUNTIME_DEP_PKGS_CSWautotrace += CSWjpeg
RUNTIME_DEP_PKGS_CSWautotrace += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibice
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibsm
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibx11
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibxext
RUNTIME_DEP_PKGS_CSWautotrace += CSWlibxt
RUNTIME_DEP_PKGS_CSWautotrace += CSWpng
RUNTIME_DEP_PKGS_CSWautotrace += CSWtiff
RUNTIME_DEP_PKGS_CSWautotrace += CSWzlib
RUNTIME_DEP_PKGS_CSWautotracedevel += CSWautotracert
RUNTIME_DEP_PKGS_CSWautotracedoc += CSWautotracert

ARCHALL_CSWautotracedoc = 1

LICENSE = COPYING

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# Not until we have a 64-bit imagemagick
#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-magick
CONFIGURE_ARGS += --with-pstoedit

include gar/category.mk
