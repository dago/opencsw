NAME = tiff
VERSION = 3.9.2
CATEGORIES = lib

DESCRIPTION = Lib and tools for Tag Image File Format
define BLURB
endef

MASTER_SITES =  http://download.osgeo.org/libtiff/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWtiff CSWtiffrt CSWtiffdevel CSWtiffdoc
CATALOGNAME_CSWtiff = tiff
CATALOGNAME_CSWtiffrt = tiff_rt
CATALOGNAME_CSWtiffdevel = tiff_devel
CATALOGNAME_CSWtiffdoc = tiff_doc

SPKG_DESC_CSWtiff += $(DESCRIPTION)
SPKG_DESC_CSWtiffrt +=  $(DESCRIPTION) - runtime package
SPKG_DESC_CSWtiffdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWtiffdoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWtiff += CSWtiffrt CSWjbigkit CSWjpeg CSWzlib
RUNTIME_DEP_PKGS_CSWtiffrt += CSWjbigkit CSWjpeg CSWzlib
RUNTIME_DEP_PKGS_CSWtiffdevel += CSWtiffrt
RUNTIME_DEP_PKGS_CSWtiffdoc += 

PKGFILES_CSWtiffrt = $(PKGFILES_RT)
PKGFILES_CSWtiffdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWtiffdoc = $(sharedstatedir)/doc/.*

ARCHALL_CSWtiffdoc = 1

CHECKPKG_OVERRIDES_CSWtiffdevel += missing-dependency|CSWtiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcmp
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|pal2rgb
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|fax2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcp
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|ppm2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffmedian
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|raw2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|thumbnail
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2ps
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|bmp2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|ras2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|rgb2ycbcr
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2bw
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcrop
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffset
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|fax2ps
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffinfo
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffdump
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2rgba
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|gif2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffdither
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffsplit
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffinfo
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2bw
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffdump
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffset
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcp
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|gif2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcrop
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|thumbnail
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffmedian
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|ppm2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|pal2rgb
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffcmp
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|rgb2ycbcr
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|raw2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|bmp2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|ras2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffdither
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|fax2ps
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|fax2tiff
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2ps
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiffsplit
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2rgba
CHECKPKG_OVERRIDES_CSWtiff += symbol-not-found|tiff2pdf

LICENSE = COPYRIGHT

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

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
