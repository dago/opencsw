# $Id$

gNAME	=	gcide
NAME	=	dict-$(gNAME)
VERSION	=	0.48
GARTYPE	=	v2

DESCRIPTION	=	GNU Collaborative International Dictionary of English
define BLURB
  GCIDE is based on Webster's Revised Unabridged Dictionary Version
  (published 1913) with additions from WordNet, and is proof-read
  and supplemented by volunteers from around the world.
endef

VENDOR_URL	=	http://www.fsf.org/

# there is no converter for the last version of gcide, i.e. 0.51;
# consequently, the converter and the dictionary are adapted from what
# Debian uses and stored for the moment the local repository,
# i.e. files/
DISTFILES		=	$(gNAME)-$(VERSION).tar.xz
DISTFILES		+=	converter.tar.xz
DISTFILES		+=	COPYING.DOC-1.2
LICENSE			=	COPYING.DOC-1.2
DISTNAME		=	$(NAME)

BUILD_DEP_PKGS	+=	CSWdictfmt
BUILD_DEP_PKGS	+=	CSWdictzip

RUNTIME_DEP_PKGS	+=	CSWdictd
CHECKPKG_OVERRIDES_CSWdict-gcide += surplus-dependency|CSWdictd

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-datapath=$(gNAME) --with-local-libmaa
EXTRA_LDFLAGS	+=	-Llibmaa -lmaa

TEST_SCRIPTS	=
INSTALL_SCRIPTS	=	custom

ARCHALL			=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract: other-source	=	$(gNAME)-$(VERSION)
post-extract:
	cd $(WORKSRC) && \
	mkdir -p $(gNAME) && \
	mv ../$(other-source)/* $(gNAME) && \
	rm -rf ../$(other-source)
	$(MAKECOOKIE)

post-build:
	cd $(WORKSRC) && $(MAKE) db
	$(MAKECOOKIE)

install-custom: pkgdictdir	=	$(datadir)/dictd
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdictdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/gcide.dict.dz $(DESTDIR)/$(pkgdictdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/gcide.index $(DESTDIR)/$(pkgdictdir)
	$(MAKECOOKIE)
