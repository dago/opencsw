# $Id$

NAME = albumshaper
VERSION = 2.1
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Photo album creator and photo manipulator
define BLURB
  Album Shaper strives to be the most friendly, easy to use, open source
  application for organizing, annotating, framing, enhancing, stylizing, and
  sharing your digital photos. Album Shaper embraces open formats like XML,
  JPEG, and XSLT, while supporting Windows, Mac OS X, and Unix users who speak
  a multitude of languages around the world. 
endef

DISTNAME		=	$(NAME)_$(VERSION)
WORKSRC			=	$(WORKDIR)/$(DISTNAME)_src
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.bz2
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-Adapt-OpenCSW.patch
PATCHFILES		+=	0002-Fix-extra-qualification.patch

BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibjpeg-dev
BUILD_DEP_PKGS	+=	CSWlibxml2-dev
BUILD_DEP_PKGS	+=	CSWlibxslt-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev
BUILD_DEP_PKGS	+=	CSWqt4-gxx-dev
BUILD_DEP_PKGS	+=	CSWqtgcc

GARCOMPILER		=	GCC3

CONFIGURE_SCRIPTS	=	custom
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

PACKAGES							+=	CSWalbumshaper-common
CATALOGNAME_CSWalbumshaper-common	=	albumshaper_common
SPKG_DESC_CSWalbumshaper-common		+=	$(DESCRIPTION), architecture neutral components
ARCHALL_CSWalbumshaper-common		=	1
OBSOLETED_BY_CSWalbumshaper-common	=	CSWalbumshapercommon
CATALOGNAME_CSWalbumshapercommon	=	albumshaper_common_stub

PACKAGES							+=	CSWalbumshaper
CATALOGNAME_CSWalbumshaper			=	albumshaper
SPKG_DESC_CSWalbumshaper			+=	$(DESCRIPTION)
PKGFILES_CSWalbumshaper				+=	/opt/csw/bin/AlbumShaper
PKGFILES_CSWalbumshaper				+=	/opt/csw/bin/AlbumShaper.bin
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWalbumshaper-common
CHECKPKG_OVERRIDES_CSWalbumshaper	+=	surplus-dependency|CSWalbumshaper-common
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibxslt1
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWalbumshaper		+=	CSWqtgcc

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && /opt/csw/kde-gcc/bin/qmake -spec solaris-g++ AlbumShaper.pro
	$(MAKECOOKIE)

build-custom:
	QTDIR=/opt/csw/kde-gcc \
	LD_OPTIONS="-L/opt/csw/gcc3/lib -R/opt/csw/kde-gcc/lib -L/opt/csw/kde-gcc/lib -R/opt/csw/lib -L/opt/csw/lib " \
	$(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

install-custom:
	QTDIR=/opt/csw/kde-gcc \
	INSTALL_ROOT="$(DESTDIR)" \
	$(MAKE) -C $(WORKSRC) install
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
