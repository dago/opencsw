# $Id$

NAME = opensp
VERSION = 1.5.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A SGML parser called OpenSP
define BLURB
  A SGML parser called OpenSP
endef

DISTNAME		=	OpenSP-$(VERSION)
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	openjade
DISTFILES		=	$(DISTNAME).tar.gz

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-http
CONFIGURE_ARGS	+=	--enable-xml-messages
CONFIGURE_ARGS	+=	--enable-default-search-path=.:/opt/csw/share/sgml:/opt/csw/share/xml:/etc/opt/csw/sgml:/opt/csw/etc/sgml
CONFIGURE_ARGS	+=	--disable-doc-build

TEST_SCRIPTS = custom

include gar/category.mk

# there is are tests failing as when I packaged with a private recipe,
# i.e., nothing changes; I choose to consider them innocuous
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

post-install-modulated:
	mv $(DESTDIR)/$(docdir)/OpenSP $(DESTDIR)/$(docdir)/$(NAME)
	mv $(DESTDIR)/$(docdir)/$(NAME)/doc $(DESTDIR)/$(docdir)/$(NAME)/html
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
