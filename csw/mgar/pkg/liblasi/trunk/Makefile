NAME = liblasi
VERSION = 1.1.0
CATEGORIES = lib

SF_PROJ      = lasi
SOURCENAME = libLASi

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
  ability to produce Postscript independent of any one application framework. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(SOURCENAME)-$(VERSION).tar.gz
DISTNAME = $(SOURCENAME)-$(VERSION)

SPKG_SOURCEURL = http://unifont.org/lasi/

PATCHFILES = liblasi-consts.diff

RUNTIME_DEP_PKGS = CSWftype2 CSWggettextrt CSWglib2 CSWpango CSWzlib

PACKAGES = CSWliblasi CSWliblasidevel CSWliblasidoc
CATALOGNAME_CSWliblasi = liblasi
CATALOGNAME_CSWliblasidevel = liblasi_devel
CATALOGNAME_CSWliblasidoc = liblasi_doc

SPKG_DESC_CSWliblasi = C++ Unicode support for PostScript
SPKG_DESC_CSWliblasidevel = C++ Unicode support for PostScript - developer package
SPKG_DESC_CSWliblasidoc = C++ Unicode support for PostScript - documentation package

RUNTIME_DEP_PKGS_CSWliblasi += CSWftype2 CSWggettextrt CSWglib2 CSWpango
RUNTIME_DEP_PKGS_CSWliblasi += CSWfconfig
RUNTIME_DEP_PKGS_CSWliblasidevel += CSWliblasi
RUNTIME_DEP_PKGS_CSWliblasidoc = 

PKGFILES_CSWliblasidevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWliblasidoc    = $(sharedstatedir)/doc/.*

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SOURCENAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# 187113 is the group_id for the liblasi project on sourceforge
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE) = 187113

BUILD64 = 1

CMAKE_CXX_FLAGS = $(CXXFLAGS)
EXTRA_COMMON_EXPORTS = CMAKE_CXX_FLAGS

include gar/category.mk

#WORKSRC = $(WORKDIR)/$(SOURCENAME)-$(VERSION)


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
	@$(MAKECOOKIE)
