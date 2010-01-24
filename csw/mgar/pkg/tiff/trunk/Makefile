GARNAME = tiff
GARVERSION = 3.9.2
CATEGORIES = lib

DESCRIPTION = lib and tools for Tag Image File Format
define BLURB
endef

MASTER_SITES =  http://download.osgeo.org/libtiff/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTNAME  = $(GARNAME)-$(GARVERSION)

PACKAGES = CSWtiff CSWtiffrt CSWtiffdevel CSWtiffdoc
CATALOGNAME_CSWtiff = tiff
CATALOGNAME_CSWtiffrt = tiffrt
CATALOGNAME_CSWtiffdevel = tiff_devel
CATALOGNAME_CSWtiffdoc = tiff_doc

SPKG_DESC_CSWtiff += lib and tools for Tag Image File Format
SPKG_DESC_CSWtiffrt += lib and tools for Tag Image File Format - runtime package
SPKG_DESC_CSWtiffdevel += lib and tools for Tag Image File Format - developer package
SPKG_DESC_CSWtiffdoc += lib and tools for Tag Image File Format - documentation

REQUIRED_PKGS_CSWtiff += CSWtiffrtCSWjbigkit CSWjpeg CSWzlib
REQUIRED_PKGS_CSWtiffrt += CSWjbigkit CSWjpeg CSWzlib
REQUIRED_PKGS_CSWtiffdevel += CSWtiffrt
REQUIRED_PKGS_CSWtiffdoc += 

PKGFILES_CSWtiffrt = $(PKGFILES_RT)
PKGFILES_CSWtiffdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWtiffdoc = $(sharedstatedir)/doc/.*

ARCHALL_CSWtiffdoc = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.remotesensing.org/libtiff/

# Patches from upstream (found via src.opensolaris.org), not applied for now
#PATCHFILES += libtiff-mantypo.patch
#PATCHFILES += libtiff-scanlinesize.patch
#PATCHFILES += libtiff-jpeg-scanline.patch
#PATCHFILES += libtiff-CVE-2009-2347.patch

BUILD64 = 1

STRIP_LIBTOOL = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(docdir)/tiff
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --with-zlib-include-dir=/opt/csw/include
CONFIGURE_ARGS += --with-zlib-lib-dir=/opt/csw/lib
CONFIGURE_ARGS += --with-jpeg-include-dir=/opt/csw/include
CONFIGURE_ARGS += --with-jpeg-lib-dir=/opt/csw/lib
CONFIGURE_ARGS += --with-jbig-include-dir=/opt/csw/include
CONFIGURE_ARGS += --with-jbig-lib-dir=/opt/csw/lib

include gar/category.mk
