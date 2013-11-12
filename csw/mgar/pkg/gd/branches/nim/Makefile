NAME    = gd
VERSION = 2.1.0
GARTYPE = bts lib
GARTYPE = v2

DESCRIPTION = A library used for dynamic image creation
define BLURB
	GD is an open source code library for the dynamic creation of 
	images by programmers. GD creates PNG, JPEG and GIF images, 
	among other formats. GD is commonly used to generate charts, 
	graphics, thumbnails, and most anything else, on the fly. 
	While not restricted to use on the web, the most common 
	applications of GD involve web site development.
endef

MAs://bitbucket.org/libgd/gd-libgd/downloads/
DISTNAME = lib$(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.xz

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWpkgconfig

PACKAGES = NIMOSSgd
CATALOGNAME_CSWgd = gd
SPKG_DESC_CSWgd = Utilities facilitating libgd for dynamic image creation
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgd += NIMOSSlibgd3

PACKAGES += NIMOSSlibgd3
CATALOGNAME_CSWlibgd3 = libgd3
SPKG_DESC_CSWlibgd3 = A library used for dynamic image creation providing libgd.so.3
PKGFILES_CSWlibgd3 += $(call pkgfiles_lib,libgd.so.3)
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibpng15-15
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibxpm4
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibz1
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgd3 += NIMOSSlibtiff5

PACKAGES += NIMOSSlibgd-dev
CATALOGNAME_CSWlibgd-dev = libgd_dev
SPKG_DESC_CSWlibgd-dev = Development files for libgd.so.3
PKGFILES_CSWlibgd-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgd-dev = NIMOSSlibgd3

CSWd+)*).tar.gz

CSW_DEFAULT_FONTPATH = $(sharedstatedir)/fonts/truetype

# This is evaluated twice, quote properly
EXTRA_CPPFLAGS = -DDEFAULCSW_DEFAULT_FONTPATH)\\\"

# For the success of the test for iconv
EXTRA_LINKER_FLAGS = -liconv

BUILD64 = 1
ISAEXEC = 1
D64_LIBS_ONLY = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-fontconfig=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-xpm=$(prefix)
CONFIGURE_ARGS += --disable-fast-install

# GD does not have a testsuite
TEST_SCRIPTS =
it comes from a default error message
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/amd64/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/pentium_pro/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv8plus/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv9/annotate/csw/include/gd.h

include gar/category.mk

# Make sure GDFONTPATH is set correctly
post-extract-modulated:
	perl -pi -e 's,/usr/share/CSWts/truetype,$(CSW_DEFAULT_FONTPATH),' \
		$(WORKSRC)/gdtestft.c \
		$(WORKSRC)/annotate.c
	perl -pi -e 's,(DEFAULT_FCSW_DEFAULT_FONTPATH):,' \
		$(WORKSRC)/gd.h
	@$(MAKECOOKIE)

