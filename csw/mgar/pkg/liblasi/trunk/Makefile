GARNAME = liblasi
GARVERSION = 1.1.0
CATEGORIES = lib

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
DISTFILES  = $(SOURCENAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWftype2 CSWgcc3corert CSWgcc3g++ CSWggettextrt CSWglib2 CSWpango CSWzlib

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

include gar/category.mk

WORKSRC = $(WORKDIR)/$(SOURCENAME)-$(GARVERSION)

configure-custom:
	@echo " ==> Configuring $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
		CXX=/opt/csw/gcc4/bin/g++ \
		cmake	-DCMAKE_INSTALL_PREFIX=/opt/csw \
			-DCMAKE_VERBOSE_MAKEFILE=ON \
			. )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; gmake )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; gmake  test)
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
		gmake install DESTDIR=$(DESTDIR) ; \
		mv $(DESTDIR)/opt/csw/share/doc/$(SOURCENAME)-$(GARVERSION) $(DESTDIR)/opt/csw/share/doc/$(GARNAME) ; \
		mv $(DESTDIR)/opt/csw/share/lasi$(GARVERSION)/examples $(DESTDIR)/opt/csw/share/$(GARNAME)/ ; \
		rmdir $(DESTDIR)/opt/csw/share/lasi$(GARVERSION) )
	@$(MAKECOOKIE)
