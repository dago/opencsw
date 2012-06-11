# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = hevea
VERSION = 1.10
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A fast LaTeX to HTML translator
define BLURB
  HEVEA is a LaTeX to HTML translator.  The input language is a fairly
  complete subset of LaTeX2e (old LaTeX style is also accepted) and the
  output language is HTML that is (hopefully) correct with respect to
  version 4.0 (transitional)

  Exotic symbols are translated into the so-called HTML 'entities',
  in other words into references to UNICODE chararacters.

  HEVEA understands LaTeX macro definitions. Simple user style
  files are understood with little or no modifications.
  Furthermore, HEVEA customization is done by writing LaTeX code.

  HEVEA is written in Objective Caml, as many lexers. It is quite fast
  and flexible. Using HEVEA it is possible to translate large documents
  such as manuals, books, etc. very quickly. All documents are
  translated as one single HTML file. Then, the output file can be cut
  into smaller files, using the companion program HACHA.
endef

MASTER_SITES	=	http://hevea.inria.fr/distri/
DISTFILES		= 	$(DISTNAME).tar.gz
DISTFILES		+=	CSWhevea.postinstall

LICENSE			=	LICENSE

BUILD_DEP_PKGS		=	CSWocaml
BUILD_DEP_PKGS		+=	CSWtetex

RUNTIME_DEP_PKGS	=	CSWtetex
RUNTIME_DEP_PKGS	+=	CSWnetpbm

PATCHFILES			=	0001-Fix-installation-paths.patch

CONFIGURE_SCRIPTS	=

SKIPTEST			=	1

# these are overrides for binaries called internally:
CHECKPKG_OVERRIDES_CSWhevea	+=	surplus-dependency|CSWtetex
CHECKPKG_OVERRIDES_CSWhevea	+=	surplus-dependency|CSWnetpbm
# innocuous:
CHECKPKG_OVERRIDES_CSWhevea += file-with-bad-content|/usr/local|root/opt/csw/share/doc/hevea/README
include gar/category.mk

pre-install-modulated:
	cd $(WORKSRC) && gsed -i 's:^DESTDIR=$$:DESTDIR=$(DESTDIR):' config.sh
	$(MAKECOOKIE)

post-install-modulated:
	cd $(WORKSRC) && ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall README $(DESTDIR)$(docdir)/$(NAME)
	$(MAKECOOKIE)
