NAME = librsvg
VERSION = 2.26
GARSUBREV = 0
CATEGORIES = lib

DESCRIPTION = Scalable Vector Graphics library
define BLURB
	This is librsvg - A high performance SVG rendering library associated with the
	Gnome Project.

	If you have questions or comments about librsvg, please send email to 
	librsvg-devel@lists.sourceforge.net. Any bugs should be reported to 
	http://bugzilla.gnome.org/

	Also, more information on librsvg can be found at librsvg.sf.net
endef

SPKG_VERSION= $(VERSION).$(GARSUBREV)

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/librsvg/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).$(GARSUBREV).tar.bz2

DISTNAME = $(NAME)-$(VERSION).$(GARSUBREV)

SPKG_SOURCEURL = http://librsvg.sourceforge.net 

LICENSE = COPYING.LIB

PACKAGES = CSWlibrsvg CSWlibrsvgdevel CSWlibrsvgdoc CSWlibrsvgmozilla CSWrsvg CSWlibrsvggnome

CATALOGNAME_CSWrsvg = rsvg
CATALOGNAME_CSWlibrsvg = librsvg
CATALOGNAME_CSWlibrsvggnome = librsvg_gnome
CATALOGNAME_CSWlibrsvgdevel = librsvg_devel
CATALOGNAME_CSWlibrsvgdoc = librsvg_doc
CATALOGNAME_CSWlibrsvgmozilla = librsvg_mozilla

SPKG_DESC_CSWrsvg += SVG to raster image conversion utility
SPKG_DESC_CSWlibrsvg += Scalable Vector Graphics library
SPKG_DESC_CSWlibrsvgdevel += Scalable Vector Graphics library - developer package
SPKG_DESC_CSWlibrsvgdoc += Scalable Vector Graphics library - documentation
SPKG_DESC_CSWlibrsvggnome += Scalable Vector Graphics library - Gnome module
SPKG_DESC_CSWlibrsvgmozilla += Scalable Vector Graphics library - Mozilla plugin

RUNTIME_DEP_PKGS_CSWrsvg += CSWfconfig
RUNTIME_DEP_PKGS_CSWrsvg += CSWftype2
RUNTIME_DEP_PKGS_CSWrsvg += CSWggettextrt
RUNTIME_DEP_PKGS_CSWrsvg += CSWglib2
RUNTIME_DEP_PKGS_CSWrsvg += CSWgtk2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibatk
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibcairo
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibcroco
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibgsf
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibx11
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibxml2
RUNTIME_DEP_PKGS_CSWrsvg += CSWpango
RUNTIME_DEP_PKGS_CSWrsvg += CSWpng

RUNTIME_DEP_PKGS_CSWlibrsvg += CSWbonobo2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWftype2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWgconf2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWglib2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWiconv
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibgsf
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWpango
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWpng
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWzlib

RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWftype2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWglib2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibgsf
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWpango
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWpng

RUNTIME_DEP_PKGS_CSWlibrsvgdevel += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWlibrsvgdoc +=
RUNTIME_DEP_PKGS_CSWlibrsvgmozilla += CSWggettextrt CSWglib2

PKGFILES_CSWlibrsvg= $(PKGFILES_RT)
PKGFILES_CSWlibrsvgdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibrsvggnome = $(libdir)/gtk-2.0/.*
PKGFILES_CSWlibrsvgmozilla = $(libdir)/mozilla/.*
PKGFILES_CSWlibrsvgdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibrsvgdoc = 1

# Only if building mozilla plugin
BUILD_DEP_PKGS += CSWmozilla
BUILD_DEP_PKGS += CSWlibxml2devel

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Upstream develops on gcc only 
PATCHFILES = pdiff.patch
PATCHFILES += perceptualdiff.patch
# Upstream have missed adding some required libs
PATCHFILES += test_makefiles.patch
# gtkdoc-rebase doesn't exist (now it does)
#PATCHFILES += doc_makefile.patch

LIBS=-lm
EXTRA_COMMON_EXPORTS = LIBS

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes --enable-static=no
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# We want to be linked with Xrender from $(prefix)/X11/lib not
# $(prefix)/lib since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
#EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

# Won't work until libgsf-1 is 64bit
#BUILD64 = 1

STRIP_LIBTOOL=1

TEST_TARGET = check

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/librsvg-2.so.2.15.90.s $(INSTALLISADIR)/opt/csw/lib/librsvg-2.so.2.15.90

post-install-isa-i386:
	@cp $(FILEDIR)/librsvg-2.so.2.15.90.i $(INSTALLISADIR)/opt/csw/lib/librsvg-2.so.2.15.90
