# $Id$

NAME			=	calibre
VERSION			=	0.9.38
#CATEGORIES		=	python
PYTHON_VERSION	=	2_7
GARTYPE			=	v2

DESCRIPTION	=	An e-book converter and library management
define BLURB
    Calibre is an e-book manager. It can view, convert and catalog e-books 
    in all of the major e-book formats. It can also talk to e-book reader 
    devices. It can go out to the internet and fetch metadata for your books. 
    It can download newspapers and convert them into e-books for convenient 
    reading. It is cross platform, running on Linux, Windows, OS X and now
	Solaris.
endef

MASTER_SITES	=	http://download.calibre-ebook.com/$(VERSION)/
SPKG_SOURCEURL	=	$(MASTER_SITES)
DISTNAME		=	$(NAME)
DISTFILES 		=	$(NAME)-$(VERSION).tar.xz
LICENSE			=	LICENSE
PATCHFILES 		+= 	0001-solaris-extensions.patch
PATCHFILES		+= 	0002-add-timer-macros.patch
PATCHFILES		+=	0003-endianness-and-byte-order.patch
PATCHFILES		+=	0004-introduce-CSW-prefix-in-some-paths.patch

BUILD_DEP_PKGS	+=	CSWpy-sip
BUILD_DEP_PKGS	+=	CSWpython27-dev
BUILD_DEP_PKGS	+=	CSWqt4-dev
BUILD_DEP_PKGS	+=	CSWpy-pyqt
BUILD_DEP_PKGS	+=	CSWimagemagick-dev
BUILD_DEP_PKGS	+=	CSWxdg-utils
BUILD_DEP_PKGS	+=	CSWpy-lxml
BUILD_DEP_PKGS	+=	CSWpy-dateutil
BUILD_DEP_PKGS	+=	CSWpy-cssutils
BUILD_DEP_PKGS	+=	CSWpy-beautifulsoup4
BUILD_DEP_PKGS	+=	CSWpy-dnspython
BUILD_DEP_PKGS	+=	CSWpoppler-dev
BUILD_DEP_PKGS	+=	CSWlibpodofo-dev
BUILD_DEP_PKGS	+=	CSWlibwmf-dev
BUILD_DEP_PKGS	+=	CSWlibchm-dev
BUILD_DEP_PKGS	+=	CSWlibicu-dev
BUILD_DEP_PKGS	+=	CSWlibmtp-dev
BUILD_DEP_PKGS	+=	CSWpy-netifaces
BUILD_DEP_PKGS	+=	CSWpsutils
BUILD_DEP_PKGS	+=	CSWpy-cssselect

GARCOMPILER		=	GNU

CONFIGURE_SCRIPTS	=	
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibchm0
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibqtdbus4
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibmagickwand6q16hdri1
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibz1
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWcalibre 	+= CSWlibpodofo0-9-1
RUNTIME_DEP_PKGS_CSWcalibre		+=	CSWxdg-utils
CHECKPKG_OVERRIDES_CSWcalibre	+=	surplus-dependency|CSWxdg-utils
# I let the /usr/share as a fallback; /opt/csw/share is first anyway:
CHECKPKG_OVERRIDES_CSWcalibre	+=	file-with-bad-content|/usr/share|root/opt/csw/lib/calibre/calibre/linux.py
CHECKPKG_OVERRIDES_CSWcalibre	+=	file-with-bad-content|/usr/share|root/opt/csw/lib/calibre/calibre/utils/fonts/scanner.py

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

build-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
			$(BUILD_ENV) \
			OVERRIDE_CFLAGS="$(CFLAGS)" \
			OVERRIDE_LDFLAGS="$(LDFLAGS)b" \
			PODOFO_INC_DIR=$(includedir)/podofo \
			PODOFO_LIB_DIR=$(libdir) \
			$(PYTHON_EXECUTABLE) setup.py build
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && \
		/usr/bin/env -i \
			$(INSTALL_ENV) \
			OVERRIDE_CFLAGS="$(CFLAGS)" \
			OVERRIDE_LDFLAGS="$(LDFLAGS)b" \
			PODOFO_INC_DIR=$(includedir)/podofo \
			PODOFO_LIB_DIR=$(libdir) \
			$(PYTHON_EXECUTABLE) setup.py install --staging-root=$(DESTDIR)$(prefix)
	@$(MAKECOOKIE)
