# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = bibtex2html
VERSION = 1.97
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A collection of tools for translating from BibTeX to HTML
define BLURB
  bibtex2html is a collection of tools for translating from BibTeX to
  HTML. They allow to produce, from a set of bibliography files in
  BibTeX format, a bibliography in HTML format. Here are some
  features:

  - Handle any BibTeX style (even those producing multiple bibliographies);
  - Use additional fields like abstract, url, ps, etc. to insert web links;
  - Crossrefs are also replaced by links;
  - Sort by dates or authors, in increasing or decreasing order;
  - Read simple macros in TeX or LaTeX files;
  - Show syntax errors in BibTeX files;
  - Extract from one or several BibTeX files the set of entries
    satisfying a given criterion.
endef

MASTER_SITES = http://www.lri.fr/~filliatr/ftp/bibtex2html/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS		=	CSWocaml
BUILD_DEP_PKGS		+=	CSWtetex
BUILD_DEP_PKGS		+=	CSWhevea

RUNTIME_DEP_PKGS	=	CSWtetex
RUNTIME_DEP_PKGS	+=	CSWperl

PATCHFILES			+=	0001-installation-desination-directories.patch

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	doc

INSTALL_SCRIPTS	=	nominal
INSTALL_SCRIPTS	+=	doc

# there is no check:
SKIPTEST		=	1

REINPLACE_USRSHARE += $(mandir)/man1/aux2bib.1
REINPLACE_WHEN_USRSHARE = postinstall

CHECKPKG_OVERRIDES_CSWbibtex2html	+=	surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWbibtex2html	+=	surplus-dependency|CSWtetex

include gar/category.mk

build-nominal:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-doc:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

install-nominal:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" install
	rm -rf "$(DESTDIR)$(datadir)/$(NAME)/"*.tar.gz
	$(MAKECOOKIE)

install-doc:
	ginstall -d "$(DESTDIR)$(docdir)/$(NAME)"
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" $@
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
