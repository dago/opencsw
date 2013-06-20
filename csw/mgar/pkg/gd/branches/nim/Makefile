NAME = gd
VERSION = 2.0.36RC1
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

MASTER_SITES = http://www.libgd.org/releases/
# Master site down.  This version archived at:  http://www.graphviz.org/pub/tmp/gd-2.0.36RC1.tar.gz
#     Contact:  ellson@opencsw.org
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += COMPILER = NIMOSSgd
CATALOGNAME_NIMOSSgd = gd
SPKG_DESC_NIMOSSgd = Utilities facilitating libgd for dynamic image creation
# PKGFILES is catchall
RUNTIME_DEP_PKGS_NIMOSSgd += NIMOSSlibgd2

PACKAGES += NIMOSSlibgd2
CATALOGNAME_NIMOSSlibgd2 = libgd2
SPKG_DESC_NIMOSSlibgd2 = A library used for dynamic image creation providing libgd.so.2
PKGFILES_NIMOSSlibgd2 += $(call pkgfiles_lib,libgd.so.2)
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibfontconfig1
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibfreetype6
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibjpeg7
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibpng15-15
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibxpm4
RUNTIME_DEP_PKGS_NIMOSSlibgd2 += NIMOSSlibz1

PACKAGES += NIMOSSlibgd-dev
CATALOGNAME_NIMOSSlibgd-dev = libgd_dev
SPKG_DESC_NIMOSSlibgd-dev = Development files for libgd.so.2
PKGFILES_NIMOSSlibgd-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_NIMOSSlibgd-dev = NIMOSSlibgd2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

NIMOSSd+)*).tar.gz

CSW_DEFAULT_FONTPATH = $(sharedstatedir)/fonts/truetype

# This is evaluated twice, quote properly
EXTRA_CPPFLAGS = -DDEFAULNIMOSSONTPATH=\\\"$(CSW_DEFAULT_FONTPATH)\\\"

BUILD64_LIBS_ONLY = 1
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

# This is ok as there are a number of search pathes for fonts in there.
# We madNIMOSS_DEFAULT_FONTPATH is the first one in the list.
CHECKPKG_OVERRIDES_NIMOSSPKG_OVERRIDES_CSWlibgd-dev += file-with-bad-content|/usr/share|root/opt/csw/include/gd.h

include gar/category.mk

# Make sure GDFONTPATH is set correctly
post-extract-modulated:
	perl -pi -e 's,/usr/share/NIMOSSts/truetype,$(CSW_DEFAULT_FONTPATH),' \
		$(WORKSRC)/gdtestft.c \
		$(WORKSRC)/annotate.c
	perl -pi -e 's,(DEFAULT_FNIMOSSPATH\s+"),\1$(CSW_DEFAULT_FONTPATH):,' \
		$(WORKSRC)/gd.h
	@$(MAKECOOKIE)

# The shipped libtool doesn't know about Sun Studio C++ compiler 'CC'
pre-configure-modulated:
#	grm -f $(WORKSRC)/config/ltmain.sh
#	gcp /opt/csw/share/libtool/config/ltmain.sh $(WORKSRC)/config/ltmain.sh
#	cd $(WORKSRC) && aclocal && automake
