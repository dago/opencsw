# $Id$

NAME = subtitleripper
VERSION = 0.3-4
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Extracts DVD subtitles from a subtitle stream and converts them.
define BLURB
  Converter for DVD subtitles into the popular srt or VobSub file format
  used by many avi players. The program requires transcode and gocr.
endef

DISTNAME		=	$(NAME)
MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME)-$(VERSION).tgz
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-From-private-recipe.patch

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		+=	CSWlibnetpbm-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev

RUNTIME_DEP_PKGS						+=	CSWgocr
CHECKPKG_OVERRIDES_CSWsubtitleripper	+=	surplus-dependency|CSWgocr
RUNTIME_DEP_PKGS						+=	CSWgsed
CHECKPKG_OVERRIDES_CSWsubtitleripper	+=	surplus-dependency|CSWgsed
RUNTIME_DEP_PKGS						+=	CSWlibnetpbm10
RUNTIME_DEP_PKGS						+=	CSWlibpng12-0
RUNTIME_DEP_PKGS						+=	CSWlibz1

CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

install-custom: pkgshare = $(sharedstatedir)/$(NAME)
install-custom: pkgdoc = $(docdir)/$(NAME)
install-custom:
	ginstall --directory $(DESTDIR)/$(bindir)
	ginstall $(WORKSRC)/subtitle2pgm $(WORKSRC)/srttool $(WORKSRC)/subtitle2vobsub $(WORKSRC)/vobsub2pgm $(WORKSRC)/pgm2txt $(DESTDIR)/$(bindir)
	ginstall --directory $(DESTDIR)/$(pkgshare)
	ginstall --mode=0644 $(WORKSRC)/gocrfilter*.sed $(DESTDIR)/$(pkgshare)
	ginstall --directory $(DESTDIR)/$(pkgdoc)
	ginstall --mode=0644 $(WORKSRC)/ChangeLog $(WORKSRC)/README* $(DESTDIR)/$(pkgdoc)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
