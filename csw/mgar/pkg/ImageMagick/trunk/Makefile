NAME = imagemagick
VERSION = 6.6.0
GARSUBREV = 9
CATEGORIES = lib

DESCRIPTION = A comprehensive package supporting automated and interative manipulation of images
define BLURB
  ImageMagick is a robust collection of tools and libraries offered under a
  usage license to read, write, and manipulate an image in many image formats
  (over 89 major formats) including popular formats like TIFF, JPEG, PNG, PDF,
  PhotoCD, and GIF.
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/
DISTFILES  = ImageMagick-$(VERSION)-$(GARSUBREV).tar.bz2

DISTNAME = ImageMagick-$(VERSION)-$(GARSUBREV)

SPKG_SOURCEURL = http://www.imagemagick.org

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWimagemagick += CSWbzip2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWimagemagick += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagick += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWggettextrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWglib2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgraphviz
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgs
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgtk2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWilmbase
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjasper
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjbigkit
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjpeg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcairo
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfpx
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibice
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblqr
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibsm
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmf
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibx11
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxext
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxml2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWperl
RUNTIME_DEP_PKGS_CSWimagemagick += CSWpng
RUNTIME_DEP_PKGS_CSWimagemagick += CSWsunmath
RUNTIME_DEP_PKGS_CSWimagemagick += CSWtiff
RUNTIME_DEP_PKGS_CSWimagemagick += CSWzlib

BUILD_DEP_PKGS += CSWdjvulibredevel
BUILD_DEP_PKGS += CSWgraphvizdevel
BUILD_DEP_PKGS += CSWilmbasedevel
BUILD_DEP_PKGS += CSWlcmsdevel
BUILD_DEP_PKGS += CSWlibcairodevel
BUILD_DEP_PKGS += CSWlibcairodevel
BUILD_DEP_PKGS += CSWliblqrdevel
BUILD_DEP_PKGS += CSWlibwmfdevel
BUILD_DEP_PKGS += CSWopenexrdevel
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWimagemagick)

# Old modules are linked to libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xwd.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dps.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|x.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xwd.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|hrz.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|miff.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|jpeg.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|rgb.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|url.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|sfw.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|uil.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pwp.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|uyvy.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xps.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pattern.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|stegano.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|vicar.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|txt.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mpr.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|cmyk.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|msl.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ycbcr.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pdb.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|cut.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|jbig.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|inline.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|jp2.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|null.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dds.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|tiff.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|thumbnail.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|cip.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ept.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|otb.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|hald.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|gif.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|avs.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pdf.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pix.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mvg.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|exr.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|vid.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|wbmp.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pcd.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ps2.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|clip.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|tim.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mpc.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xcf.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dps.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ps3.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mono.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|raw.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pict.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pnm.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|plasma.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|meta.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|viff.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|icon.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dib.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|histogram.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|caption.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|sct.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pcl.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|fax.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mat.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|rla.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ps.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|preview.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|sgi.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|png.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|cin.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|cals.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|yuv.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|pcx.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mtv.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|magick.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xc.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dpx.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|matte.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|wpg.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|palm.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|bmp.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|avi.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|scr.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|html.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|psd.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|info.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dcm.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|fits.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dot.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ipl.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|label.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xbm.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|braille.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|ttf.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|x.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|sun.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|mpeg.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|gradient.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|rle.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|art.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|gray.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|map.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|dng.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|tile.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|xpm.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|tga.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|analyze.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|libMagick.so.10.0.4|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|libMagick++.so.2.0.0|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|libMagickWand.so.2.0.0|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|libMagickCore.so.2.0.0|libX11.so.4
CHECKPKG_OVERRIDES_CSWimagemagick += linked-against-discouraged-library|libWand.so.10.0.4|libX11.so.4

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ImageMagick-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CONFIGURE_ARGS_COMMON  = $(DIRPATHS)
CONFIGURE_ARGS_COMMON += --with-perl=$(bindir)/perl
CONFIGURE_ARGS_COMMON += --enable-shared --disable-static
CONFIGURE_ARGS_COMMON += --with-dps=yes
# Ghostscript lib is linked to Sun X11
CONFIGURE_ARGS_COMMON += --with-gslib=no
CONFIGURE_ARGS_COMMON += --x-includes=/opt/csw/X11/include
CONFIGURE_ARGS_COMMON += --x-libraries=/opt/csw/X11/lib 
# Solaris 8 and 9 doesn't have complex.h
CONFIGURE_ARGS_COMMON += --without-fftw
CONFIGURE_ARGS_COMMON += --with-modules=yes
# Let's try to use openmp and see what it does for performance
#CONFIGURE_ARGS_COMMON += --disable-openmp
CONFIGURE_ARGS_COMMON += --disable-silent-rules
# Until librsvg,graphviz and perl is 64bit
#CONFIGURE_ARGS_isa-amd64 += --without-gvc
#CONFIGURE_ARGS_isa-amd64 += --without-rsvg
#CONFIGURE_ARGS_isa-amd64 += --without-perl
#CONFIGURE_ARGS_isa-sparcv9 += --without-gvc
#CONFIGURE_ARGS_isa-sparcv9 += --without-rsvg
#CONFIGURE_ARGS_isa-sparcv9 += --without-perl

CONFIGURE_ARGS = $(CONFIGURE_ARGS_COMMON) $(foreach M,$(MODULATIONS),$(CONFIGURE_ARGS_$M))

PATCHFILES += Makefile.patch
PATCHFILES += configure.diff

# Test has to be run *after* install
#TEST_TARGET = check
TEST_TARGET = 

#Dependencies not 64-bit yet
#BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_LDFLAGS = -L./magick/.libs 
#EXTRA_LD_OPTIONS = -L./magick/.libs 
#
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/magick/.libs
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/wand/.libs
# We want to be link with Xrender from $(prefix)/X11/lib not $(prefix)/lib
# since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS += -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la
EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

STRIP_LIBTOOL=1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)

post-install-isa-sparcv8:
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.s.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.s.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.i.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.i.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)
