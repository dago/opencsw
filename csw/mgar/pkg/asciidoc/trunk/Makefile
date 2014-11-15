NAME = asciidoc
VERSION = 8.6.9

DESCRIPTION = A Documentation Generator
define BLURB
	AsciiDoc is a text document format for writing short documents,
	articles, books and UNIX man pages. AsciiDoc files can be translated to
	HTML and DocBook markups using the asciidoc(1) command.

	AsciiDoc is highly configurable: both the AsciiDoc source file syntax
	and the backend output markups (which can be almost any type of
	SGML/XML markup) can be customized and extended by the user.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Add-opt-csw-gnu-bin-to-PATH-in-a2x.py.patch

PACKAGES = CSWasciidoc
ARCHALL_CSWasciidoc = 1
RUNTIME_DEP_PKGS_CSWasciidoc += CSWpython
RUNTIME_DEP_PKGS_CSWasciidoc += CSWggetopt
# This can not be detected by checkpkg
CHECKPKG_OVERRIDES_CSWasciidoc += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWasciidoc += surplus-dependency|CSWggetopt

TEST_TARGET = test

include gar/category.mk

