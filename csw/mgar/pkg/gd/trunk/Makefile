NAME = gd
VERSION = 2.0.36RC1
CATEGORIES = lib

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

PATCHFILES += gdkanji.c.patch

#GARCOMPILER = GCC4

PACKAGES = CSWgd
CATALOGNAME_CSWgd = gd
SPKG_DESC_CSWgd = Utilities facilitating libgd for dynamic image creation
# PKGFILES is catchall
RUNTIME_DEP_pkgs_CSWgd = CSWlibgd2
RUNTIME_DEP_PKGS_CSWgd += CSWiconv
RUNTIME_DEP_PKGS_CSWgd += CSWpng
RUNTIME_DEP_PKGS_CSWgd += CSWjpeg
RUNTIME_DEP_PKGS_CSWgd += CSWzlib
RUNTIME_DEP_PKGS_CSWgd += CSWftype2
RUNTIME_DEP_PKGS_CSWgd += CSWlibgd2
RUNTIME_DEP_PKGS_CSWgd += CSWxpm
RUNTIME_DEP_PKGS_CSWgd += CSWfconfig

PACKAGES += CSWlibgd2
CATALOGNAME_CSWlibgd2 = libgd2
SPKG_DESC_CSWlibgd2 = A library used for dynamic image creation providing libgd.so.2
PKGFILES_CSWlibgd2 = $(call baseisadirs,$(libdir),libgd\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWiconv 
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWpng
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWxpm
RUNTIME_DEP_PKGS_CSWlibgd2 += CSWzlib

PACKAGES += CSWlibgd-dev
CATALOGNAME_CSWlibgd-dev = libgd_dev
SPKG_DESC_CSWlibgd-dev = Development files for libgd.so
PKGFILES_CSWlibgd-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgd-dev = CSWlibgd2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CSW_DEFAULT_FONTPATH = $(sharedstatedir)/fonts/truetype

# This is evaluated twice, quote properly
EXTRA_CPPFLAGS = -DDEFAULT_FONTPATH=\\\"$(CSW_DEFAULT_FONTPATH)\\\"

BUILD64 = 1
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

MERGE_DIRS_isa-extra = $(libdir)

# This is ok as there are a number of search pathes for fonts in there.
# We made sure that the $CSW_DEFAULT_FONTPATH is the first one in the list.
CHECKPKG_OVERRIDES_CSWlibgd-dev += file-with-bad-content|/usr/share|root/opt/csw/include/gd.h

include gar/category.mk

# Make sure GDFONTPATH is set correctly
post-extract-modulated:
	perl -pi -e 's,/usr/share/fonts/truetype,$(CSW_DEFAULT_FONTPATH),' \
		$(WORKSRC)/gdtestft.c \
		$(WORKSRC)/annotate.c
	perl -pi -e 's,(DEFAULT_FONTPATH\s+"),\1$(CSW_DEFAULT_FONTPATH):,' \
		$(WORKSRC)/gd.h
	@$(MAKECOOKIE)

# The shipped libtool doesn't know about Sun Studio C++ compiler 'CC'
pre-configure-modulated:
#	grm -f $(WORKSRC)/config/ltmain.sh
#	gcp /opt/csw/share/libtool/config/ltmain.sh $(WORKSRC)/config/ltmain.sh
#	cd $(WORKSRC) && aclocal && automake
	@$(MAKECOOKIE)

