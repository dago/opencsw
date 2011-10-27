NAME = wmf
VERSION = 0.2.8.4
CATEGORIES = lib

DESCRIPTION = Library and tools for manipulating Windows metafiles
define BLURB
	libwmf is a library for reading vector images in Microsoft's native Windows 
	Metafile Format (WMF) and for either (a) displaying them in, e.g., an X 
	window; or (b) converting them to more standard/open file formats such as, 
	e.g., the W3C's XML-based Scaleable Vector Graphic (SVG) format. 
endef

SF_PROJ = wvware
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = libwmf-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://wvware.sourceforge.net

PACKAGES += CSWwmf
CATALOGNAME_CSWwmf = wmf
SPKG_DESC_CSWwmf += Library and tools for manipulating Windows metafiles
RUNTIME_DEP_PKGS_CSWwmf += CSWftype2 
RUNTIME_DEP_PKGS_CSWwmf += CSWjpeg
RUNTIME_DEP_PKGS_CSWwmf += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWwmf += CSWlibz1
RUNTIME_DEP_PKGS_CSWwmf += CSWwmffonts
RUNTIME_DEP_PKGS_CSWwmf += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWwmf += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWwmf += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWwmf += CSWlibwmflite0-2-7
CHECKPKG_OVERRIDES_CSWwmf += surplus-dependency|CSWwmffonts

PACKAGES += CSWlibwmflite0-2-7
CATALOGNAME_CSWlibwmflite0-2-7 = libwmflite0_2_7
PKGFILES_CSWlibwmflite0-2-7 += $(call pkgfiles_lib,libwmflite-0.2.so.7)
SPKG_DESC_CSWlibwmflite0-2-7 += Library and tools for manipulating Windows metafiles - runtime package, libwmflite-0.2.so.7
OBSOLETED_BY_CSWlibwmflite0-2-7 = CSWlibwmf

PACKAGES += CSWlibwmf0-2-7
CATALOGNAME_CSWlibwmf0-2-7 = libwmf0_2_7
PKGFILES_CSWlibwmf0-2-7 += $(call pkgfiles_lib,libwmf-0.2.so.7)
SPKG_DESC_CSWlibwmf0-2-7 += Library and tools for manipulating Windows metafiles - runtime package, libwmf-0.2.so.7
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWftype2
OBSOLETED_BY_CSWlibwmf0-2-7 = CSWlibwmf

PACKAGES += CSWlibwmf-dev
CATALOGNAME_CSWlibwmf-dev = libwmf_dev
SPKG_DESC_CSWlibwmf-dev += Library and tools for manipulating Windows metafiles - developer package
PKGFILES_CSWlibwmf-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibwmf-dev += $(sharedstatedir)/doc/.*
RUNTIME_DEP_PKGS_CSWlibwmf-dev += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWlibwmf-dev += CSWlibwmf0-2-7
OBSOLETED_BY_CSWlibwmf-dev += CSWlibwmfdevel
CATALOGNAME_CSWlibwmfdevel = libwmf_devel_stub
OBSOLETED_BY_CSWlibwmf-dev += CSWlibwmfdoc
CATALOGNAME_CSWlibwmfdoc = libwmf_doc_stub
# These are docs only
CHECKPKG_OVERRIDES_CSWlibwmf-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libwmf/tutapi.html
CHECKPKG_OVERRIDES_CSWlibwmf-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libwmf/gd.html
CHECKPKG_OVERRIDES_CSWlibwmf-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/libwmf/tutapi.html
CHECKPKG_OVERRIDES_CSWlibwmf-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/libwmf/index.html

PACKAGES += CSWwmf-fonts
SPKG_DESC_CSWwmf-fonts += Windows metafile fonts
PKGFILES_CSWwmf-fonts = $(sharedstatedir)/libwmf/fonts/.*
ARCHALL_CSWwmf-fonts = 1
OBSOLETED_BY_CSWwmf-fonts += CSWwmffonts
CATALOGNAME_CSWwmffonts = wmf_fonts_stub

PACKAGES += CSWlibwmf-gtk
SPKG_DESC_CSWlibwmf-gtk += Library and tools for manipulating Windows metafiles - GTK loader
PKGFILES_CSWlibwmf-gtk = $(libdir).*/io-wmf.so
RUNTIME_DEP_PKGS_CSWlibwmf-gtk += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwmf-gtk += CSWglib2
RUNTIME_DEP_PKGS_CSWlibwmf-gtk += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibwmf-gtk += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWlibwmf-gtk += CSWlibwmflite0-2-7
BUILD_DEP_PKGS += CSWgtk2devel
OBSOLETED_BY_CSWlibwmf-gtk += CSWlibwmfgtk
CATALOGNAME_CSWlibwmfgtk = libwmf_gtk_stub

# This *must* be the same as in the GD package
CSW_DEFAULT_FONTPATH = $(sharedstatedir)/fonts/truetype

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x
#CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-libxml2=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-sys-gd=$(prefix)
CONFIGURE_ARGS += --with-sysfontmap=$(datadir)/fonts/fontmap
#CONFIGURE_ARGS += --with-xtrafontmap=
CONFIGURE_ARGS += --with-gsfontmap=$(datadir)/ghostscript/Resource/Init/Fontmap.GS
CONFIGURE_ARGS += --with-gsfontdir=$(datadir)/ghostscript/fonts

# These are just docs
CHECKPKG_OVERRIDES_CSWlibwmfdoc += file-with-bad-content

include gar/category.mk

# Make sure GDFONTPATH is set correctly
post-extract-modulated:
	perl -pi -e 's,/usr/share/fonts/truetype,$(CSW_DEFAULT_FONTPATH),' \
		$(WORKSRC)/src/extra/gd/gd.h \
		$(WORKSRC)/src/extra/gd/gdft.c
	@$(MAKECOOKIE)

