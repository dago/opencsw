GARNAME = docbookxsl
GARVERSION = 1.69.1
PATCHLEVEL = 5.1
CATEGORIES = xtra

# for our (modified from rhel) copied in Makefile.
PREREQUISITE_PKGS = CSWgfile CSWbash

REQUIRED_PKGS = CSWsgmlcommon CSWxmlcommon CSWdocbookdtds CSWlibxml2

DESCRIPTION = Norman Walsh's XSL stylesheets for DocBook XML.
define BLURB
The DocBook XSL stylesheets are a set of stylesheets for use with an
XSLT engine (such as xsltproc or Saxon) for transforming DocBook XML
documents into other DocBookOutputFormats, such as HTML, PDF,
Microsoft HTML Help, and man pages.
endef

# docbook-xsl is housed in the docbook master project at SF.
SF_PROJ = docbook
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = docbook-xsl-$(GARVERSION).tar.bz2
DISTFILES += docbook-xsl-doc-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWdocbookxsl,postinstall preremove)

# These are listed in the same order they'd be applied during the rpm build...
# They don't apply cleanly, otherwise.
PATCHFILES  = docbook-xsl-pagesetup.patch docbook-xsl-marginleft.patch
PATCHFILES += docbook-xsl-lists.patch docbook-xsl-sp.patch
PATCHFILES += add_makefile.patch

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS =

TEST_SCRIPTS =

INSTALL_ARGS = DESTDIR=$(DESTDIR) GARVERSION=$(GARVERSION) \
			PATCHLEVEL=$(PATCHLEVEL)

#to make the package extraction happy...(we don't use the - separator)
WORKSRC = $(WORKDIR)/docbook-xsl-$(GARVERSION)

post-install-modulated:
	@(cd $(DESTDIR)/opt/csw/share/sgml/docbook; \
		ln -s xsl-stylesheets-$(GARVERSION)-$(PATCHLEVEL) \
			xsl-stylesheets )
	@$(MAKECOOKIE)

include gar/category.mk
