# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME			=	m17n-db
VERSION			=	1.6.4
glibcVersion	=	2.17
GARTYPE			=	v2

DESCRIPTION = Database for the multilingual text processing library for the C language.
define BLURB
  Database for the multilingual text processing library for the C language.
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

PACKAGES 						+=	CSWm17n-db
CATALOGNAME_CSWm17n-db			=	m17n_db
SPKG_DESC_CSWm17n-db			+=	$(DESCRIPTION)
OBSOLETED_BY_CSWm17n-db			=	CSWm17ndb
CATALOGNAME_CSWm17ndb			=	m17ndb_stub
ARCHALL_CSWm17ndb				=	1
ARCHALL_CSWm17n-db				=	1

include gar/category.mk

pre-configure-modulated:	$(DOWNLOADDIR)/$(glibcArchive)
	@echo "executing $@"
	/usr/bin/env -i $(BUILD_ENV) && gtar --directory=$(PWD)/$(WORKSRC) --extract --file=$(PWD)/$(DOWNLOADDIR)/$(glibcArchive) $(glibcDirectory)/localedata/charmaps
	$(MAKECOOKIE)
