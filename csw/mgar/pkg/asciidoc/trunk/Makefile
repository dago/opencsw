GARNAME = asciidoc
GARVERSION = 8.2.7
CATEGORIES = utils

DESCRIPTION = An Documentation Generator
define BLURB
	AsciiDoc is a text document format for writing short documents,
	articles, books and UNIX man pages. AsciiDoc files can be translated to
	HTML and DocBook markups using the asciidoc(1) command.

	AsciiDoc is highly configurable: both the AsciiDoc source file syntax
	and the backend output markups (which can be almost any type of
	SGML/XML markup) can be customized and extended by the user.
endef

AUTOFILES = configure.ac Makefile.in install-sh

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWasciidoc.gspec CSWasciidoc.depend
DISTFILES += $(AUTOFILES)

PREREQUISITE_PKGS = CSWautoconf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# until the autoconf stuff is included upstream, we'll maintain and import our
# own.
pre-configure:
	( cd $(WORKSRC); \
		for f in $(AUTOFILES); do \
			 cp ../$$f .; \
		done; \
	chmod 755 install-sh; \
	autoconf )
	@$(MAKECOOKIE)
