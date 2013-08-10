NAME = liblasi
VERSION = 1.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = C++ Unicode support for PostScript
define BLURB
  libLASi is a library written by Larry Siden that provides a C++ stream output
  interface ( with operator << ) for creating Postscript documents that can contain
  characters from any of the scripts and symbol blocks supported in Unicode and
  by Owen Taylor's Pango layout engine. The library accomodates right-to-left
  scripts such as Arabic and Hebrew as easily as left-to-right scripts. Indic and
  Indic-derived Complex Text Layout (CTL) scripts, such as Devanagari, Thai, Lao,
  and Tibetan are supported to the extent provided by Pango and by the OpenType
  fonts installed on your system. All of this is provided without need for any
  special configuration or layout calculation on the programmer's part.

  Although the capability to produce Unicode-based multilingual Postscript
  documents exists in large Open Source application framework libraries such
  as GTK+, QT, and KDE, libLASi was designed for projects which require the
  ability to produce Postscript independent of any one application frameworkECT. 
endef

SF_PROJ = lasi
MASTER_SITES = $(SF_MIRRORS)
SOURCENAME = libLASi
DISTNAME = $(SOURCENAME)-$(VERSION)
DISTFILES  = $(DVENDOR_URL = http://unifont.org/lasi/

GARCOMPILER = GCC4

BUILD_DEP_PKGS  = CSWcmake
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWfontconfig-dev

PACKAGES += CSWliblasi1
SPKG_DESC_CSWliblasi1 = C++ Unicode support for PostScript, libLASi.so.1
PKGFILES_CSWliblasi1 = $(call pkgfiles_lib,libLASi.so.1)
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWliblasi1 += CSWpango
OBSOLETED_BY_CSWliblasi1 = CSWliblasi
si0 = CSWliblasi

PACKAGES += CSWliblasi-dev
SPKG_DESC_CSWliblasi-dev = Developer support for libLASi.so.0
PKGFILES_CSWliblasi-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWliblasi-dev += $(sharedstatedir)/doc/.*
RUNTIME_DEP_PKGS_CSWliblasi-1

BUILD64_LIBS_ONLY = 1

# It doesn't remove the no-direct-binding errors, but it shouldn't hurt either
EXTRA_LD_OPTIONS = -z nolazyload-lCstd -norunpath

CONFIGURE_INSTALL_SCRIPTS = custom
TEST_TARGET = test_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
		cmake	-DCMAKE_INSTALL_PREF	-DCMAKE_INSTALL_EXEC_PREFIX:PATH="$(exec_prefix)" \
	-DCMAKE_INSTALL_BINDIR:PATH="$(bindir)" \
	-DCMAKE_INSTALL_DATADIR:PATH="$(datadir)" \
	-DCMAKE_INSTALL_LIBDIR:PATH="$(libdir)" \
	-DCMAKE_INSTALL_INCLUDEDIR:PATH="$(includedir)" \
	-DCMAKE_INSTALL_INFODIR:PATH="$(infodir)" \
	-DCMAKE_INSTALL_MANDIR:PATH="$(mandir)" \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_CXX_COMPILER="$(CXX)" \
	EFILE=ON \
      -DCMAKE_CXX_FLAGS:STRING="$(CXXFLAGS)" \
			. )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
		gmake install DESTDIR=$(DESTDIR) ; \
		mv $(DESTDIR)/opt/csw/share/doc/$(DISTNAME) $(DESTDIR)/opt/csw/share/doc/$(NAME) ; \
		mv $(DESTDIR)/opt/csw/share/lasi$(VERSION)/* $(DESTDIR)/opt/csw/share/doc/$(NAME)/ ; \
		rmdir $(DESTDIR)/opt/csw/share/lasi$(VERSION) )