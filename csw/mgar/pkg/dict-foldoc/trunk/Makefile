# $Id$

NAME			=	dict-foldoc
MASTER_SITES	=	http://foldoc.org/
URI				=	$(MASTER_SITES)Dictionary
VERSION			=	20131123
GARTYPE			=	v2

DESCRIPTION	=	FOLDOC dictionary database
define BLURB
 This package contains the FOLDOC, the Free On Line Dictionary of
 Computing, formatted for use by the dictionary server in the dictd
 package.
endef

DISTFILES 		=	$(DISTNAME).tar.xz
DISTFILES		+=	COPYING.DOC-1.2
LICENSE			=	COPYING.DOC-1.2

BUILD_DEP_PKGS	+=	CSWcurl
BUILD_DEP_PKGS	+=	CSWdictfmt
BUILD_DEP_PKGS	+=	CSWdictzip

RUNTIME_DEP_PKGS	+=	CSWdictd
CHECKPKG_OVERRIDES_CSWdict-foldoc += surplus-dependency|CSWdictd

CONFIGURE_ARGS	=	$(DIRPATHS)

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

ARCHALL				=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# I'm not very satisfied with this method but it's the best that I can
# do without hitting the master site at each invocation of the
# make-file, directly or indirectly; this method hits the master site
# only when fetching.
pre-fetch: archive	=	$(GARCHIVEDIR)/$(DISTNAME).tar.xz
pre-fetch: checkVersion
	@/usr/bin/test -e "$(archive)" || \
	( \
		mkdir -p "$(SPKG_TMPDIR)/$(DISTNAME)" && \
		curl -s -f -o "$(SPKG_TMPDIR)/$(DISTNAME)/$(NAME)" $(URI) && \
		gtar --directory "$(SPKG_TMPDIR)" --create --xz --file="$(archive)" $(DISTNAME) \
	)
	$(MAKECOOKIE)

checkVersion:
	@originVersion=`bash -c 'gdate +"%Y%m%d" -d "$$(curl -s -I $(URI) | sed -n "s/^Last-Modified: //p")"'`; \
	if [ "$${originVersion}" = $(VERSION) ] ; \
	then \
	{ \
		true; \
	} \
	else \
	{ \
		echo "the origin version has changed $${originVersion} vs. "$(VERSION); \
		false; \
	} \
	fi

build-custom:
	cd $(WORKSRC) && \
	dictfmt	< "$(NAME)" \
			-f \
			--headword-separator %%% \
			--break-headwords \
			--allchars \
			-u $(URI) \
			-s "The Free On-line Dictionary of Computing ($(VERSION))" \
			--utf8 \
			foldoc
	cd $(WORKSRC) && \
	dictzip -v foldoc.dict
	$(MAKECOOKIE)

install-custom: pkgdictdir	=	$(datadir)/dictd
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdictdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/foldoc.dict.dz $(DESTDIR)/$(pkgdictdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/foldoc.index $(DESTDIR)/$(pkgdictdir)
	$(MAKECOOKIE)
