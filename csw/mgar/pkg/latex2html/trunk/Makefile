# $Id$

NAME = latex2html
VERSION = 2008
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A converter written in Perl that converts LATEX documents to HTML
define BLURB
  A converter written in Perl that converts LATEX documents to HTML
endef

MASTER_SITES	=	http://mirrors.ctan.org/support/latex2html/
DISTFILES		=	$(DISTNAME).tar.gz
# Debian series 7 from
# http://patch-tracker.debian.org/package/latex2html/2008-debian1-7
PATCHFILES		+=	0001-Add-url.patch
PATCHFILES		+=	0002-Don-t-use-rgb.txt-from-pstoimg.patch
PATCHFILES		+=	0003-Fix-borders-in-pstoimg.patch
PATCHFILES		+=	0004-Fix-file-pattern-in-pstoimg.patch
PATCHFILES		+=	0005-Fix-several-typos.patch
PATCHFILES		+=	0006-Use-HTML-4.0-by-default.patch
PATCHFILES		+=	0007-Fixes-bad-perl-in-l2hconf.pin.patch
PATCHFILES		+=	0008-latex2html-fix-authoraddress.patch
PATCHFILES		+=	0009-override-dvips-dot-in-filename-problem.patch
PATCHFILES		+=	0010-manual-fix-address.patch
PATCHFILES		+=	0011-Makefiles-fixes.patch
PATCHFILES		+=	0012-Fix-images-types.patch
# the following DISTFILES are patches creating new files; why GAR
# doesn't support them?
DISTFILES		+=	abnt.perl
PATCHFILES		+=	0013-Fix-romanian.patch
PATCHFILES		+=	0014-Fix-mathend-mark.patch
DISTFILES		+=	floatflt.ins
PATCHFILES		+=	0015-Fix-pdfoutput.patch
PATCHFILES		+=	0016-Fix-gs-stderr.patch
PATCHFILES		+=	0017-Pstoimg-match-gray.patch
PATCHFILES		+=	0018-Fix-spaces-in-filenames.patch
DISTFILES		+=	texexpand.1
DISTFILES		+=	latex2html.1
DISTFILES		+=	eurosym.perl
PATCHFILES		+=	0019-Match-multiline.patch
PATCHFILES		+=	0020-latex2html-fix-defined.patch
# previously private and new patches:
PATCHFILES		+=	0021-Documentation-private-1-and-3.patch
PATCHFILES		+=	0022-Run-time-style-private-2.patch
PATCHFILES		+=	0023-Installation-private-7.patch
PATCHFILES		+=	0024-TeXExpand-private-7.patch
PATCHFILES		+=	0025-Icons-installation-private-8.patch
PATCHFILES		+=	0026-pnmcrop-detection.patch
PATCHFILES		+=	0027-Adapt-makeseg.patch
PATCHFILES		+=	0028-Call-environment-defined-Perl.patch

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-texpath=$(texmflocaldir)/tex/latex/html

BUILD_DEP_PKGS		+=	CSWgs
BUILD_DEP_PKGS		+=	CSWnetpbm
BUILD_DEP_PKGS		+=	CSWperl
BUILD_DEP_PKGS		+=	CSWtetex

BUILD_SCRIPTS	=	nominal
# as strange as it seems the check and test are build actions...
BUILD_SCRIPTS	+=	check
BUILD_SCRIPTS	+=	test
BUILD_SCRIPTS	+=	documentation

TEST_SCRIPTS	=

LICENSE			=	LICENSE

RUNTIME_DEP_PKGS	+=	CSWgs
RUNTIME_DEP_PKGS	+=	CSWperl
RUNTIME_DEP_PKGS	+=	CSWnetpbm
RUNTIME_DEP_PKGS	+=	CSWtetex

ARCHALL	= 1

include gar/category.mk

build-nominal:
	$(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-check:
	$(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-test:
	$(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-documentation:
	$(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

pre-install-modulated:
	cp $(FILEDIR)/abnt.perl $(WORKSRC)/styles
	cp $(FILEDIR)/eurosym.perl $(WORKSRC)/styles
	cp $(FILEDIR)/floatflt.ins $(WORKSRC)/texinputs
	mkdir -p "$(DESTDIR)/$(sharedstatedir)/lib/$(NAME)/icons"
	$(MAKECOOKIE)

noPack	+=	*.aux
noPack	+=	*.bbl
noPack	+=	*.dat
noPack	+=	*.dvi
noPack	+=	*.glo
noPack	+=	*.gls
noPack	+=	*.idx
noPack	+=	*.ind
noPack	+=	*.index
noPack	+=	*.ist
noPack	+=	*.lof
noPack	+=	*.log
noPack	+=	*.lot
noPack	+=	*.ptr
noPack	+=	*.sty
noPack	+=	*.tex
noPack	+=	*.toc
noPack	+=	.latex2html-init
noPack	+=	Makefile*
noPack	+=	changebar
noPack	+=	changebar
noPack	+=	hthtml
noPack	+=	hthtml
noPack	+=	manual/*.aux
noPack	+=	manual/*.aux
noPack	+=	manual/*.bbl
noPack	+=	manual/*.log
noPack	+=	manual/*.pl
noPack	+=	manual/*.tex
noPack	+=	psfiles
noPack	+=	psfiles
post-install-modulated:
	ginstall --directory $(DESTDIR)/$(mandir)/man1
	ginstall $(FILEDIR)/texexpand.1 $(DESTDIR)/$(mandir)/man1
	ginstall $(FILEDIR)/latex2html.1 $(DESTDIR)/$(mandir)/man1
	ginstall --directory $(DESTDIR)/$(docdir)
	mv $(DESTDIR)/$(sharedstatedir)/lib/$(NAME)/docs $(DESTDIR)/$(docdir)/$(NAME)
	mv $(DESTDIR)/$(sharedstatedir)/lib/$(NAME)/example $(DESTDIR)/$(docdir)/$(NAME)
	cd $(DESTDIR)/$(docdir)/$(NAME) && rm -rf $(noPack)
	$(MAKECOOKIE)
