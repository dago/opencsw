# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = m17n-db
VERSION = 1.6.4
glibcVersion	=	2.17
GARTYPE = v2

DESCRIPTION = Database for the multilingual text processing library for the C language.
define BLURB
  Database for m17n
endef

MASTER_SITES	=	http://download.savannah.gnu.org/releases/m17n/
DISTFILES		=	$(DISTNAME).tar.gz
MASTER_SITES	+=	http://ftp.gnu.org/gnu/glibc/
glibcDirectory	=	glibc-$(glibcVersion)
glibcArchive	=	$(glibcDirectory).tar.xz
DISTFILES		+=	$(glibcArchive)
NOEXTRACT		=	$(glibcArchive)

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_ARGS		+=	--with-charmaps=$(glibcDirectory)/localedata/charmaps

include gar/category.mk

pre-configure:	$(DOWNLOADDIR)/$(glibcArchive)
	@echo "executing $@"
	cd $(WORKSRC) && gtar xf $(PWD)/$(DOWNLOADDIR)/$(glibcArchive) $(glibcDirectory)/localedata/charmaps
	$(MAKECOOKIE)
