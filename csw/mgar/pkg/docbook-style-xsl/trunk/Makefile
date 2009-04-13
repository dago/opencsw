GARNAME = docbookxsl
GARVERSION = 1.74.3
CATEGORIES = xtra

# for our (modified from rhel) copied in Makefile.
PREREQUISITE_PKGS = CSWgfile CSWbash

PACKAGES = CSWdocbookxsl CSWdocbookxsldoc
ARCHALL = 1

CATALOGNAME_CSWdocbookxsl = $(GARNAME)
CATALOGNAME_CSWdocbookxsldoc = $(GARNAME)doc

REQUIRED_PKGS_CSWdocbookxsl = CSWsgmlcommon CSWxmlcommon CSWdocbookdtds
REQUIRED_PKGS_CSWdocbookxsl += CSWlibxml2
REQUIRED_PKGS_CSWdocbookxsldoc = CSWdocbookxsl

PKGFILES_CSWdocbookxsldoc = $(datadir)/doc/.*

DESCRIPTION = Norman Walsh's XSL stylesheets for DocBook XML.
define BLURB
The DocBook XSL stylesheets are a set of stylesheets for use with an
XSLT engine (such as xsltproc or Saxon) for transforming DocBook XML
documents into other DocBookOutputFormats, such as HTML, PDF,
Microsoft HTML Help, and man pages.
endef

SPKG_DESC_CSWdocbookxsl = Norman Walsh's XSL stylesheets for DocBook XML
SPKG_DESC_CSWdocbookxsldoc = Documentation for the Docbook XSL stylesheets

# docbook-xsl is housed in the docbook master project at SF.
SF_PROJ = docbook
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = docbook-xsl-$(GARVERSION).tar.bz2
DISTFILES += docbook-xsl-doc-$(GARVERSION).tar.bz2
DISTFILES += CSWdocbookxsl.preremove

#use the dynamic adm script feature so we don't need to edit file at
#version change
include files/CSWdocbookxsl.postinstall

PATCHFILES += add_makefile.patch

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS = 

TEST_SCRIPTS =

INSTALL_SCRIPTS = $(WORKSRC)/Makefile.csw

INSTALL_ARGS = DESTDIR=$(DESTDIR)

#to make the package extraction happy...(we don't use the - separator)
WORKSRC = $(WORKDIR)/docbook-xsl-$(GARVERSION)

include gar/category.mk

install-%/Makefile.csw:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) -f Makefile.csw DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)