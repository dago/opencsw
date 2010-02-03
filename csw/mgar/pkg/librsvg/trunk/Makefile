GARNAME = librsvg
GARVERSION = 2.26
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

SPKG_VERSION= $(GARVERSION).$(GARSUBREV)

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/librsvg/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).$(GARSUBREV).tar.bz2

DISTNAME = $(GARNAME)-$(GARVERSION).$(GARSUBREV)

SPKG_SOURCEURL = http://librsvg.sourceforge.net 

LICENSE = COPYING.LIB

PACKAGES = CSWlibrsvg CSWlibrsvgdevel CSWlibrsvgdoc CSWlibrsvgmozilla

CATALOGNAME_CSWlibrsvg = librsvg
CATALOGNAME_CSWlibrsvgdevel = librsvg_devel
CATALOGNAME_CSWlibrsvgdoc = librsvg_doc
CATALOGNAME_CSWlibrsvgmozilla = librsvg_mozilla

SPKG_DESC_CSWlibrsvg += Scalable Vector Graphics library
SPKG_DESC_CSWlibrsvgdevel += Scalable Vector Graphics library - developer package
SPKG_DESC_CSWlibrsvgdoc += Scalable Vector Graphics library - documentation
SPKG_DESC_CSWlibrsvgmozilla += Scalable Vector Graphics library - Mozilla plugin

RUNTIME_DEP_PKGS_CSWlibrsvg += CSWfconfig CSWftype2 CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWglib2 CSWgtk2 CSWlibatk
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibcairo CSWlibcroco CSWlibgsf CSWlibx11
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWlibxml2 CSWpango CSWpng CSWzlib CSWorbit2
RUNTIME_DEP_PKGS_CSWlibrsvg += CSWbonobo2 CSWgconf2 CSWgnomevfs2 CSWlibxrender 
RUNTIME_DEP_PKGS_CSWlibrsvgdevel += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWlibrsvgdoc +=
RUNTIME_DEP_PKGS_CSWlibrsvgmozilla += CSWggettextrt CSWglib2

PKGFILES_CSWlibrsvgdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibrsvgmozilla = $(libdir)/mozilla/.*
PKGFILES_CSWlibrsvgdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibrsvgdoc = 1

# Only if building mozilla plugin
BUILD_DEP_PKGS += CSWmozilla
BUILD_DEP_PKGS += CSWlibxml2devel

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

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
