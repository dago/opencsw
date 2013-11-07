# $Id$

NAME	=	freefont
VERSION	=	20120503
GARTYPE	=	v2

DESCRIPTION	=	GNU FreeFont
define BLURB
  provide a useful set of free scalable (i.e., OpenType) fonts
  covering as much as possible of the ISO 10646/Unicode UCS (Universal
  Character Set).
endef

MASTER_SITES	=	$(GNU_MIRROR)
DISTFILES		+=	$(NAME)-otf-$(VERSION).tar.gz
# the archives contain redundant, e.g README, which are not extracted again:
export UNZIP	=	-n
DISTFILES		+=	$(NAME)-ttf-$(VERSION).zip
DISTFILES		+=	$(NAME)-woff-$(VERSION).zip

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom
ARCHALL				=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

install-custom: pkgdocdir	=	$(DESTDIR)$(docdir)/$(NAME)
install-custom: pkgfontdir =	$(DESTDIR)$(datadir)/fonts/$(NAME)
install-custom:
	ginstall -d "$(pkgdocdir)"
	cd $(WORKSRC) && \
	ginstall \
		AUTHORS \
		ChangeLog \
		CREDITS \
		README \
		TROUBLESHOOTING \
		USAGE \
		webfont_guidelines.txt \
		$(pkgdocdir)
	ginstall -d "$(pkgfontdir)"
	cd $(WORKSRC) && \
	ginstall \
		FreeMono.otf \
		FreeMono.ttf \
		FreeMono.woff \
		FreeMonoBold.otf \
		FreeMonoBold.ttf \
		FreeMonoBold.woff \
		FreeMonoBoldOblique.otf \
		FreeMonoBoldOblique.ttf \
		FreeMonoBoldOblique.woff \
		FreeMonoOblique.otf \
		FreeMonoOblique.ttf \
		FreeMonoOblique.woff \
		FreeSans.otf \
		FreeSans.ttf \
		FreeSans.woff \
		FreeSansBold.otf \
		FreeSansBold.ttf \
		FreeSansBold.woff \
		FreeSansBoldOblique.otf \
		FreeSansBoldOblique.ttf \
		FreeSansBoldOblique.woff \
		FreeSansOblique.otf \
		FreeSansOblique.ttf \
		FreeSansOblique.woff \
		FreeSerif.otf \
		FreeSerif.ttf \
		FreeSerif.woff \
		FreeSerifBold.otf \
		FreeSerifBold.ttf \
		FreeSerifBold.woff \
		FreeSerifBoldItalic.otf \
		FreeSerifBoldItalic.ttf \
		FreeSerifBoldItalic.woff \
		FreeSerifItalic.otf \
		FreeSerifItalic.ttf \
		FreeSerifItalic.woff \
		$(pkgfontdir)
	$(MAKECOOKIE)
