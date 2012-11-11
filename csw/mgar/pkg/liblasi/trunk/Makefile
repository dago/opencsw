NAME = liblasi
VERSION = 1.1.0
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
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES = liblasi-consts.diff

VENDOR_URL = http://unifont.org/lasi/

PACKAGES += CSWliblasi0
SPKG_DESC_CSWliblasi0 = C++ Unicode support for PostScript, libLASi.so.0
PKGFILES_CSWliblasi0 = $(call pkgfiles_lib,libLASi.so.0)
RUNTIME_DEP_PKGS_CSWliblasi0 += CSWftype2
RUNTIME_DEP_PKGS_CSWliblasi0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWliblasi0 += CSWglib2
RUNTIME_DEP_PKGS_CSWliblasi0 += CSWpango
RUNTIME_DEP_PKGS_CSWliblasi0 += CSWfconfig
OBSOLETED_BY_CSWliblasi0 = CSWliblasi

PACKAGES += CSWliblasi-dev
SPKG_DESC_CSWliblasi-dev = Developer support for libLASi.so.0
PKGFILES_CSWliblasi-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWliblasi-dev += $(sharedstatedir)/doc/.*
RUNTIME_DEP_PKGS_CSWliblasi-dev += CSWliblasi0
# That is ok
CHECKPKG_OVERRIDES_CSWliblasi-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/liblasi/examples/README

BUILD64_LIBS_ONLY = 1

EXTRA_CXX_FLAGS = -lCstd -norunpath

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
		cmake	-DCMAKE_INSTALL_PREFIX="$(prefix)" \
      -DCMAKE_INSTALL_EXEC_PREFIX:PATH="$(exec_prefix)" \
      -DCMAKE_INSTALL_BINDIR:PATH="$(bindir)" \
      -DCMAKE_INSTALL_DATADIR:PATH="$(datadir)" \
      -DCMAKE_INSTALL_LIBDIR:PATH="$(libdir)" \
      -DCMAKE_INSTALL_INCLUDEDIR:PATH="$(includedir)" \
      -DCMAKE_INSTALL_INFODIR:PATH="$(infodir)" \
      -DCMAKE_INSTALL_MANDIR:PATH="$(mandir)" \
			-DCMAKE_VERBOSE_MAKEFILE=ON \
      -DCMAKE_CXX_FLAGS:STRING="$(CXXFLAGS)" \
			. )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(NAME) (custom)"
	@( cd $(WORKSRC) ; gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	@( cd $(WORKSRC) ; gmake  test)
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
		gmake install DESTDIR=$(DESTDIR) ; \
		mv $(DESTDIR)/opt/csw/share/doc/$(DISTNAME) $(DESTDIR)/opt/csw/share/doc/$(NAME) ; \
		mv $(DESTDIR)/opt/csw/share/lasi$(VERSION)/* $(DESTDIR)/opt/csw/share/doc/$(NAME)/ ; \
		rmdir $(DESTDIR)/opt/csw/share/lasi$(VERSION) )