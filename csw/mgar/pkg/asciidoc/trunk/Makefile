NAME = asciidoc
VERSION = 8.6.6
CATEGORIES = utils

DESCRIPTION = A Documentation Generator
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

RUNTIME_DEP_PKGS_CSWasciidoc = CSWpython CSWggetopt

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(AUTOFILES)

PATCHFILES = handle-csw-etc-paths.patch
PATCHFILES += 0002-Add-opt-csw-gnu-bin-to-PATH-in-a2x.py.patch

TEST_TARGET = test

INSTALL_ARGS = vimdir=/opt/csw/etc/vim

CHECKPKG_OVERRIDES_CSWasciidoc += surplus-dependency|CSWggetopt

include gar/category.mk

# until the autoconf stuff is included upstream, we'll maintain and import our
# own.
pre-configure-modulated:
	( cd $(WORKSRC); autoconf )
	@$(MAKECOOKIE)
