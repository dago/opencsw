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

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10501
UFILES_REGEX = (\d+(?:\.\d+)*)

VENDOR_URL = http://wvware.sourceforge.net

PACKAGES += CSWwmf
CATALOGNAME_CSWwmf = wmf
SPKG_DESC_CSWwmf += Library and tools for manipulating Windows metafiles
RUNTIME_DEP_PKGS_CSWwmf += CSWftype2 
RUNTIME_DEP_PKGS_CSWwmf += CSWjpeg
RUNTIME_DEP_PKGS_CSWwmf += CSWpng
RUNTIME_DEP_PKGS_CSWwmf += CSWzlib
RUNTIME_DEP_PKGS_CSWwmf += CSWwmffonts
RUNTIME_DEP_PKGS_CSWwmf += CSWiconv
RUNTIME_DEP_PKGS_CSWwmf += CSWlibxml2
RUNTIME_DEP_PKGS_CSWwmf += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWwmf += CSWlibwmflite0-2-7
CHECKPKG_OVERRIDES_CSWwmf += surplus-dependency|CSWwmffonts

PACKAGES += CSWlibwmflite0-2-7
CATALOGNAME_CSWlibwmflite0-2-7 = libwmflite0_2_7
PKGFILES_CSWlibwmflite0-2-7 += $(call baseisadirs,$(libdir),libwmflite-0\.2\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibwmflite0-2-7 += Library and tools for manipulating Windows metafiles - runtime package, libwmflite-0.2.so.7
OBSOLETED_BY_CSWlibwmflite0-2-7 = CSWlibwmf

PACKAGES += CSWlibwmf0-2-7
CATALOGNAME_CSWlibwmf0-2-7 = libwmf0_2_7
PKGFILES_CSWlibwmf0-2-7 += $(call baseisadirs,$(libdir),libwmf-0\.2\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibwmf0-2-7 += Library and tools for manipulating Windows metafiles - runtime package, libwmf-0.2.so.7
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWpng
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibwmf0-2-7 += CSWftype2
OBSOLETED_BY_CSWlibwmf0-2-7 = CSWlibwmf

PACKAGES += CSWlibwmf-dev
CATALOGNAME_CSWlibwmf-dev = libwmf_dev
SPKG_DESC_CSWlibwmf-dev += Library and tools for manipulating Windows metafiles - developer package
PKGFILES_CSWlibwmf-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibwmf-dev += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWlibwmf-dev += CSWlibwmf0-2-7
OBSOLETED_BY_CSWlibwmf-dev = CSWlibwmfdevel
CATALOGNAME_CSWlibwmfdevel = libwmf_devel_stub

PACKAGES += CSWlibwmfdoc
CATALOGNAME_CSWlibwmfdoc = libwmf_doc
# This is a legacy name
CHECKPKG_OVERRIDES_CSWlibwmfdoc += catalogname-does-not-match-pkgname|pkgname=CSWlibwmfdoc|catalogname=libwmf_doc|expected-catalogname=libwmfdoc
SPKG_DESC_CSWlibwmfdoc += Library and tools for manipulating Windows metafiles - documentation
PKGFILES_CSWlibwmfdoc = $(sharedstatedir)/doc/.*
ARCHALL_CSWlibwmfdoc = 1

PACKAGES += CSWwmffonts
CATALOGNAME_CSWwmffonts = wmf_fonts
# This is a legacy name
CHECKPKG_OVERRIDES_CSWwmffonts += catalogname-does-not-match-pkgname|pkgname=CSWwmffonts|catalogname=wmf_fonts|expected-catalogname=wmffonts
SPKG_DESC_CSWwmffonts += Library and tools for manipulating Windows metafiles - fonts
PKGFILES_CSWwmffonts = $(sharedstatedir)/libwmf/fonts/.*
ARCHALL_CSWwmffonts = 1

PACKAGES += CSWlibwmfgtk
CATALOGNAME_CSWlibwmfgtk = libwmf_gtk
# This is a legacy package name
CHECKPKG_OVERRIDES_CSWlibwmfgtk += catalogname-does-not-match-pkgname|pkgname=CSWlibwmfgtk|catalogname=libwmf_gtk|expected-catalogname=libwmfgtk
SPKG_DESC_CSWlibwmfgtk += Library and tools for manipulating Windows metafiles - GTK loader
PKGFILES_CSWlibwmfgtk = $(libdir).*/io-wmf.so
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWglib2
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWlibwmflite0-2-7
BUILD_DEP_PKGS += CSWgtk2devel

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

