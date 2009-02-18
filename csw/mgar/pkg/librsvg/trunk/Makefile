GARNAME = librsvg
GARVERSION = 2.22
GARSUBREV = 3
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
DISTFILES += librsvg-2.so.2.15.90.i
DISTFILES += librsvg-2.so.2.15.90.s
DISTFILES += $(call admfiles,CSWlibrsvg,)

DISTNAME = $(GARNAME)-$(GARVERSION).$(GARSUBREV)

REQUIRED_PKGS += CSWbzip2 CSWfconfig CSWftype2 CSWggettextrt
REQUIRED_PKGS += CSWglib2 CSWgs CSWgtk2 CSWiconv CSWlibatk
REQUIRED_PKGS += CSWlibcairo CSWlibcroco CSWlibgsf
REQUIRED_PKGS += CSWlibxml2 CSWlibxml2devel CSWpango CSWpng CSWsunmath CSWzlib
REQUIRED_PKGS += CSWbonobo2 CSWgconf2 CSWgnomevfs2 CSWlibxrender CSWorbit2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Upstream develops on gcc only 
PATCHFILES = pdiff.patch
PATCHFILES += perceptualdiff.patch
# Upstream have missed adding some required libs
PATCHFILES += test_makefiles.patch
# gtkdoc-rebase doesn't exist
PATCHFILES += doc_makefile.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes --enable-static=no

TEST_TARGET = check

include gar/category.mk


post-install-isa-sparcv8:
	@cp $(FILEDIR)/librsvg-2.so.2.15.90.s $(INSTALLISADIR)/opt/csw/lib/librsvg-2.so.2.15.90

post-install-isa-i386:
	@cp $(FILEDIR)/librsvg-2.so.2.15.90.i $(INSTALLISADIR)/opt/csw/lib/librsvg-2.so.2.15.90
