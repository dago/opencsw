GARNAME = asciidoc
GARVERSION = 8.4.2
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

PACKAGES = CSWasciidoc
CATALOGNAME_CSWasciidoc = asciidoc

ARCHALL_CSWasciidoc = 1

REQUIRED_PKGS_CSWasciidoc = CSWpython

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(AUTOFILES)

#it would really seem this author "doesn't get" auto* stuff.
PATCHFILES = fix-autoconf-version.patch fix-Makefile-am.patch

PREREQUISITE_PKGS = CSWautoconf

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=67797
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# until the autoconf stuff is included upstream, we'll maintain and import our
# own.
pre-configure-modulated:
	( cd $(WORKSRC); autoconf )
	@$(MAKECOOKIE)
