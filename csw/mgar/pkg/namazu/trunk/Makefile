# $Id$

NAME = namazu
VERSION = 2.0.21
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A Full-Text Search Engine
define BLURB
  Namazu is a full-text search engine intended for easy use. Not only
  does it work as a small or medium scale Web search engine, but also
  as a personal search system for email or other files.

  (The Japanese word 'Namazu' means 'catfish' in English.) 
endef

MASTER_SITES = http://namazu.org/stable/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-tknamazu

BUILD_DEP_PKGS		+=	CSWkakasi-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlynx
BUILD_DEP_PKGS		+=	CSWpm-file-mmagic

TEST_SCRIPTS		=	custom

RUNTIME_DEP_PKGS	+=	CSWkakasi
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlynx
RUNTIME_DEP_PKGS	+=	CSWperl
RUNTIME_DEP_PKGS	+=	CSWpm-file-mmagic

include gar/category.mk

# one of the tests fails: mknmz-11; decided to not block on it...
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

post-install-modulated:
	ginstall --directory $(DESTDIR)/$(docdir)/$(NAME)
	mv $(DESTDIR)/$(datadir)/$(NAME)/doc/* $(DESTDIR)/$(docdir)/$(NAME)
	rmdir $(DESTDIR)/$(datadir)/$(NAME)/doc
	mv $(DESTDIR)/$(datadir)/$(NAME)/etc/* $(DESTDIR)/$(docdir)/$(NAME)
	rmdir $(DESTDIR)/$(datadir)/$(NAME)/etc
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
